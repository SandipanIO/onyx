# Use Python 3.10 slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy entire backend folder into container
COPY . .

# Go into backend directory
WORKDIR /app/backend

# Add Python path so that "onyx" is importable
ENV PYTHONPATH="${PYTHONPATH}:/app/backend"

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements/default.txt

# Start FastAPI using uvicorn
CMD ["uvicorn", "onyx.server:app", "--host", "0.0.0.0", "--port", "10000"]
