from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response

from profiles.models import Profile
from .serializers import UserProfileSerializer
from profiles.signals import follow_done, unfollow_done
from api.v1.arguments.serializers import ContentionSerializer
from premises.models import Contention
from profiles.forms import ProfileUpdateForm


class UserProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = UserProfileSerializer
    lookup_field = 'username__iexact'
    lookup_url_kwarg = 'username'

    @action(detail=True, methods=['get'])
    def authenticated_user(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def update_profile(self, request, *args, **kwargs):
        instance = self.get_object()
        form = ProfileUpdateForm(request.data, instance=instance)
        if form.is_valid():
            form.save()
            return Response(self.serializer_class(instance).data)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


class UserFollowViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = UserProfileSerializer
    lookup_field = 'username__iexact'
    lookup_url_kwarg = 'username'

    @action(detail=True, methods=['post'])
    def follow(self, request, *args, **kwargs):
        user = self.get_object()
        if user.id == request.user.id:
            return Response({'message': "Kedini takip edemezsin."},
                            status=status.HTTP_400_BAD_REQUEST)

        if user.followers.filter(pk=request.user.pk).exists():
            return Response(
                {'message': "Zaten bu kullaniciyi takip ediyorsun"},
                status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user)
        follow_done.send(sender=self, follower=request.user, following=user)
        return Response(status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['delete'])
    def unfollow(self, request, *args, **kwargs):
        user = self.get_object()
        if not request.user.following.filter(id=user.id).exists():
            return Response(
                {'message': "Takibi birakmadan once takip etmen gerekiyor."},
                status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(user)
        unfollow_done.send(sender=self, follower=request.user, following=user)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get'])
    def followings(self, request, *args, **kwargs):
        user = self.get_object()
        page = self.paginate_queryset(user.following.all())
        serializer = self.get_pagination_serializer(page)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def followers(self, request, *args, **kwargs):
        user = self.get_object()
        page = self.paginate_queryset(user.followers.all())
        serializer = self.get_pagination_serializer(page)
        return Response(serializer.data)


class UserArgumentsView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ContentionSerializer
    lookup_field = 'username__iexact'
    lookup_url_kwarg = 'username'

    @action(detail=True, methods=['get'])
    def user_arguments(self, request, *args, **kwargs):
        user = self.get_object()
        arguments = user.contention_set.filter()
        if not(self.request.user.is_authenticated and
                user == self.request.user):
            arguments = arguments.filter(is_published=True)
        page = self.paginate_queryset(arguments)
        serializer = self.get_pagination_serializer(page)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def user_contributed(self, request, *args, **kwargs):
        user = self.get_object()
        page = self.paginate_queryset(Contention.objects.filter(
            premises__user=user, is_published=True).exclude(user=user))
        serializer = self.get_pagination_serializer(page)
        return Response(serializer.data)


profile_detail = UserProfileViewset.as_view(
    {'get': 'retrieve'}
)
profile_me = UserProfileViewset.as_view(
    {'get': 'authenticated_user', 'put': 'update_profile'},
    permission_classes=(permissions.IsAuthenticated,)
)
profile_followers = UserFollowViewset.as_view(
    {'get': 'followers'}
)
profile_followings = UserFollowViewset.as_view(
    {'get': 'followings'}
)
profile_follow = UserFollowViewset.as_view(
    {'post': 'follow', 'delete': 'unfollow'},
    permission_classes=(permissions.IsAuthenticated,)
)
user_arguments = UserArgumentsView.as_view(
    {'get': 'user_arguments'},
)
user_contributed_arguments = UserArgumentsView.as_view(
    {'get': 'user_contributed'},
)
