# Base python package
FROM python:slim

# Working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install the dependencies
RUN pip3 install -r requirements.txt

# Copy the files
COPY . .

# Executable commands
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
