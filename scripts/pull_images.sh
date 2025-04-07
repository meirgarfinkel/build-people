#!/bin/bash
set -e

echo "Pulling new Docker image..."
cd /home/ec2-user/build-people
docker-compose -f docker-compose.prod.yml pull
