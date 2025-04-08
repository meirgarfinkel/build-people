#!/bin/bash
set -e

echo "Logging into Docker Hub..."
docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD

echo "Pulling new Docker image..."
cd /home/ec2-user/build-people
docker-compose -f docker-compose.prod.yml pull
