docker build --network=host --no-cache -t cssidatabackend .
docker tag cssidatabackend chasec2331/cssidatabackend:latest
docker push chasec2331/cssidatabackend
