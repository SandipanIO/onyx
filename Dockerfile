# Set working directory
WORKDIR /app

# Copy all code
COPY . .

# Change working dir to backend
WORKDIR /app/backend

# Set PYTHONPATH so Python knows where to import from
ENV PYTHONPATH=/app/backend

# Install deps
RUN pip install --upgrade pip
RUN pip install -r requirements/default.txt

# Set Python path so that `onyx` is correctly recognized as a module
ENV PYTHONPATH=/app/backend

# Run app
CMD ["uvicorn", "onyx.server:app", "--host", "0.0.0.0", "--port", "10000"]
