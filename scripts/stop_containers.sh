#!/bin/bash
set -e

echo "Stopping running containers..."
cd /home/ec2-user/build-people
docker-compose -f docker-compose.prod.yml down || true
