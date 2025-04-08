#!/bin/bash
set -e

echo "Logging into Docker Hub..."

# Load environment variables from .env file
set -o allexport
source /home/ec2-user/build-people/.env
set +o allexport

# Non-interactive Docker login using environment variables
echo "$DOCKERHUB_TOKEN" | docker login --username "$DOCKERHUB_USERNAME" --password-stdin

echo "Pulling new Docker image..."
cd /home/ec2-user/build-people
docker-compose -f docker-compose.prod.yml pull
