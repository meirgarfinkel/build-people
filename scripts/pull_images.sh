#!/bin/bash
set -e

echo "Logging into Docker Hub..."
# Non-interactive Docker login using environment variables
echo "$DOCKERHUB_TOKEN" | docker login --username "$DOCKERHUB_USERNAME" --password-stdin

echo "Pulling new Docker image..."
cd /home/ec2-user/build-people
docker-compose -f docker-compose.prod.yml pull
