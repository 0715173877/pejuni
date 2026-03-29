#!/bin/bash

# Exit on error
set -e

echo "🚀 Starting deployment..."

# Pull latest changes
git pull origin main

# Install dependencies (adjust based on your stack)
# For Node.js:
# npm install --production

# For Python:
# pip install -r requirements.txt

# Run migrations if needed
# python manage.py migrate

# Restart your application
# For PM2 (Node.js):
# pm2 restart app

# For Gunicorn (Python):
# sudo systemctl restart your-app

# For Nginx:
# sudo systemctl reload nginx

echo "✅ Deployment complete!"
