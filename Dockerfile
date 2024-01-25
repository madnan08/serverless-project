# Stage 1: Build Stage
FROM python:3.8-slim as builder

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y unixodbc unixodbc-dev freetds-dev freetds-bin tdsodbc

# Copy only the requirements file to leverage Docker cache
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime Stage
FROM python:3.8-slim

WORKDIR /app

# Copy installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/

# Copy the entire application, including frontend files
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run run.py when the container launches
CMD ["python", "run.py"]

