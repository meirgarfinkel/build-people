#!/bin/bash
set -e

echo "Stopping running containers..."
cd /home/ec2-user/build-people
docker-compose -f docker-compose.prod.yml down || true

echo "Disk usage before cleanup:"
df -h

# Clean up EC2 instance
echo "Cleaning up unused resources..."
docker system prune -a -f --volumes
docker builder prune -a -f
docker volume prune -f
docker network prune -f
docker container prune -f
docker image prune -a -f

sudo find /var/log -type f -size +100M -exec rm -f {} \;

# Check disk usage again after cleanup
echo "Disk usage after cleanup:"
df -h
