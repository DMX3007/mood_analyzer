# Use a Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port for Flask
EXPOSE 5001

# Run the Flask app
CMD ["python", "sentiment_analysis.py"]
