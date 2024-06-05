#!/bin/bash
# Start Redis in the background
redis-server --daemonize yes

# Execute the CMD from the Dockerfile, e.g., start Superset
exec "$@"

