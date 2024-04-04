# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the static directory
COPY static /app/static

# Install the dependencies
# Note: psycopg2-binary is used for PostgreSQL database connection
RUN pip install --no-cache-dir flask psycopg2-binary

RUN pip install requests


# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variables for Flask to run in production mode
ENV FLASK_ENV=production
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

