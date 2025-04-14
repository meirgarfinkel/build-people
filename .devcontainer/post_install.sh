#!/bin/bash

chown -R appuser:appuser /home/appuser/.ssh
chmod 700 /home/appuser/.ssh
find /home/appuser/.ssh -type f -name "id_*" ! -name "*.pub" -exec chmod 600 {} +

# Navigate to theme/static_src directory
pushd theme/static_src || exit

# Install dependencies for theme/static_src
npm install

# Run dev script
npm run dev

popd

# Set Git configuration
git config --global --add safe.directory /app
git config --global user.email "meirgarfinkel@gmail.com"
git config --global user.name "Meir Garfinkel"

source /app/.bash_aliases
