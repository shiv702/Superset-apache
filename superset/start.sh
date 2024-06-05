#!/bin/bash

# Start Redis in the background
redis-server --daemonize yes

# Upgrade the database schema to the latest version
superset db upgrade

# Initialize Superset (roles, permissions)
superset init

# Create the admin user if not already present
ADMIN_EXISTS=$(superset fab list-users | grep "admin@example.com" | wc -l)
if [ "$ADMIN_EXISTS" -eq "0" ]; then
    echo "Creating admin user..."
    superset fab create-admin \
        --username admin \
        --firstname Superset \
        --lastname Admin \
        --email admin@example.com \
        --password admin
else
    echo "Admin user already exists, skipping creation."
fi

# Start the Superset application
superset run -p 8088 --with-threads --reload --debugger

