# friendlyhello
# Based on Docker tutorial
# https://docs.docker.com/get-started/part2/#define-a-container-with-a-dockerfile
# To build image:
# docker build -t friendlyhello .

# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]