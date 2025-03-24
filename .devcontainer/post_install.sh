#!/bin/bash

chown -R docker:docker /home/docker/.ssh
chmod 700 /home/docker/.ssh
chmod 600 /home/docker/.ssh/id_* || true

# Install main dependencies
npm install

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
