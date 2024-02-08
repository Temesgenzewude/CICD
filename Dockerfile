FROM python:3.11-alpine

# Set the working directory

WORKDIR /app

# Copy requirements.txt file to the working directory

COPY requirements.txt .

# Install the requirements

RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory

COPY . .

# Command to run on container start

CMD [ "python", "main.py" ]
