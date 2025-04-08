#!/bin/bash
set -e

cd /home/ec2-user/build-people

echo "Creating nginx config"
mkdir -p nginx

cat <<EOF > nginx/nginx.conf
server {
    listen 80;
    server_name buildpeople.app www.buildpeople.app;
    
    location /static/ {
        alias /app/staticfiles/;
        expires 1y;
        access_log off;
        add_header Cache-Control "public";
    }

    location / {
        proxy_pass http://web:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
EOF

echo "Starting containers..."
docker-compose -f docker-compose.prod.yml up -d --remove-orphans
