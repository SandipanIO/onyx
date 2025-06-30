# Use official Python image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc build-essential git

# Copy all files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r backend/requirements/default.txt

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Start the app
CMD ["python", "-m", "backend.onyx.server"]
