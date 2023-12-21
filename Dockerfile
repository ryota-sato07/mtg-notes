# Use the official image as a parent image
FROM python:3.11.6

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required dependencies
RUN pip install openai==1.3.7 moviepy pydub python-dotenv

# Install ffmpeg and clean up
RUN apt-get update && apt-get install -y ffmpeg \
    && rm -rf /var/lib/apt/lists/*
