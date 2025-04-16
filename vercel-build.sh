#!/bin/bash
set -e

# Print versions
echo "Node version: $(node -v)"
echo "NPM version: $(npm -v)"
echo "Python version: $(python --version 2>&1)"

# Build the frontend
echo "Building frontend..."
cd frontend
npm install
npm run build
cd ..

# Print success message
echo "Build completed successfully!" 