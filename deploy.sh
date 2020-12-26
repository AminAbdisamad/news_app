#! /bin/bash

# Create Images
docker build -t aminux/news_app .
docker build -t aminux/news_app_nginx ./nginx

# Push Images to docker hub
docker push aminux/news_app
docker push aminux/news_app_nginx

# Make sure its executable
# chmod +x deploy.sh

# run like this 
# ./deploy.sh


# After you deploy your project to docker hub 
# ssh to the server and pull images from docker hub
# docker pull aminux/news_app
# docker pull aminux/news_app_nginx

# and finally run 
# docker-compose up -d