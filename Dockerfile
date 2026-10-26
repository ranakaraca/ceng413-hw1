# Base image for Python
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Create and switch to a non-root user for security
RUN useradd --create-home --uid 10001 appuser
USER appuser

# Expose port
EXPOSE 8080

# Set env variable
ENV APP_ENV=Production

# Run the app
ENTRYPOINT ["python", "app.py"]