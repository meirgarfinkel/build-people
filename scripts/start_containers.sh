#!/bin/bash
set -e

cd /home/ec2-user/build-people

echo "Creating nginx configuration..."

cat <<EOF > nginx/nginx.conf
server {
    listen 80;
    server_name buildpeople.app www.buildpeople.app;
    return 301 https://\$host\$request_uri;
}

server {
    listen 443 ssl;
    server_name buildpeople.app www.buildpeople.app;

    ssl_certificate /etc/nginx/ssl/cloudflare.crt;
    ssl_certificate_key /etc/nginx/ssl/cloudflare.key;

    location /static/ {
        alias /app/staticfiles/;
    }

    location / {
        proxy_pass http://web:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto https;
    }
}
EOF

echo "Starting containers..."
docker-compose -f docker-compose.prod.yml up -d --remove-orphans

sleep 5

echo "Running migrations..."
docker-compose -f docker-compose.prod.yml exec web uv run python manage.py migrate --noinput
