# Use the official Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set PYTHONPATH to include the working directory
ENV PYTHONPATH=/usr/src/app

# Command to run Robot Framework tests
ENTRYPOINT ["robot"]
CMD ["--outputdir", "reports", "tests/"]
