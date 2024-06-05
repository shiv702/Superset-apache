# Use the official Apache Superset image
FROM apache/superset:latest

# Install Redis and Python (if not already included) and other dependencies
USER root
RUN apt-get update && \
    apt-get install -y redis-server python3 && \
    rm -rf /var/lib/apt/lists/*

# Copy the Superset configuration
COPY ./superset_config.py /app/pythonpath/superset_config.py

# Generate a SECRET_KEY and append it to the configuration file before running upgrade
RUN echo "SECRET_KEY = '$(python3 -c "import os; print(os.urandom(24).hex())")'" >> /app/pythonpath/superset_config.py

# Install Python packages for Google Sheets integration
RUN pip install gspread oauth2client

# Copy the entrypoint script and make it executable
COPY entrypoint.sh /entrypoint.sh
COPY start.sh /start.sh
RUN chmod +x /entrypoint.sh
RUN chmod +x /start.sh

# Switch back to superset user and initialize Superset
USER superset
#RUN superset db upgrade
#RUN superset init

# Expose the port Superset is running on
EXPOSE 8088

# Start Superset using Gunicorn
ENTRYPOINT ["/entrypoint.sh"]
#CMD ["gunicorn", "--bind", "0.0.0.0:8088", "superset.app:create_app()"]
CMD ["gunicorn", "--bind", "0.0.0.0:8088", "--timeout", "120", "superset.app:create_app()"]
