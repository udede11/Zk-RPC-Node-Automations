FROM ubuntu:latest

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Run a command that keeps the container running
CMD ["tail", "-f", "/dev/null"]
