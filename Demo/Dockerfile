FROM python:3.9-slim

# Set the working directory
WORKDIR /etl

# Install dependencies
COPY requirements.txt /etl/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the ETL script into the container
COPY . /etl/

CMD ["python", "etl_script.py"]
