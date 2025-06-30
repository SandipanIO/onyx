# Use Python 3.10 slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy everything
COPY . .

# Move to backend directory
WORKDIR /app/backend

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements/default.txt

# ✅ Make sure Python can recognize onyx package
ENV PYTHONPATH=/app/backend

# Run the FastAPI app
CMD ["uvicorn", "onyx.server:app", "--host", "0.0.0.0", "--port", "10000"]
