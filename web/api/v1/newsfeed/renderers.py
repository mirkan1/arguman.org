from django.utils.encoding import smart_str
from bson import ObjectId

from rest_framework.utils.encoders import JSONEncoder
from rest_framework.renderers import JSONRenderer


class MongoDBJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return smart_str(obj)
        return super(MongoDBJSONEncoder, self).default(obj)


class MongoDBJSONRenderer(JSONRenderer):
    encoder_class = MongoDBJSONEncoder
