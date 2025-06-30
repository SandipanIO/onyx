# Use Python 3.10 slim image
FROM python:3.10-slim

# Set working directory to backend
WORKDIR /app/backend

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    git \
    curl \
 && rm -rf /var/lib/apt/lists/*

# Copy everything into the container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements/default.txt

# Start the FastAPI app using uvicorn
CMD ["uvicorn", "onyx.server:app", "--host", "0.0.0.0", "--port", "10000"]
