docker-compose build && 
docker-compose up -d &&
docker logs argumanorg-web-1 --tail 50 -f