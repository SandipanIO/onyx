# Use Python 3.10 slim image
FROM python:3.10-slim

# Set root working directory
WORKDIR /app

# Copy everything into the container
COPY . .

# Set PYTHONPATH so that onyx modules inside backend/ are importable
ENV PYTHONPATH="${PYTHONPATH}:/app/backend"

# Go into backend directory
WORKDIR /app/backend

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements/default.txt

# Start FastAPI using uvicorn
CMD ["uvicorn", "onyx.server:app", "--host", "0.0.0.0", "--port", "10000"]
