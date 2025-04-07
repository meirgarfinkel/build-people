#!/bin/bash
set -e

echo "Starting containers..."
cd /home/ec2-user/build-people
docker-compose -f docker-compose.prod.yml up -d
