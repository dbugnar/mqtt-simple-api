# mqtt-simple-api

# Docker run cmd

docker build -t mqtt-api:latest .
docker run -ti -v /var/run/docker.sock:/var/run/docker.sock -e DB=<mongodb database> -p 12344:12344 --rm --name mqtt-api mqtt-api
