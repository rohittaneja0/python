# Use a lightweight official Python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /tmp

# Copy only the requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port Flask runs on (default is 5000)
EXPOSE 5000

RUN chgrp -R 0 /tmp && chmod -R g=u /tmp

USER 1001
RUN chown -R 1001:0 /tmp

RUN chmod 755 /tmp/

# Start the application using flask
CMD ["flask", "--app", "main", "run", "--host", "0.0.0.0"]
