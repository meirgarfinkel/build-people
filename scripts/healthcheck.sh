#!/bin/bash
set -e

echo "Validating service health..."
sleep 5  # Give containers a moment to start
curl -f http://localhost/health/ || exit 1
