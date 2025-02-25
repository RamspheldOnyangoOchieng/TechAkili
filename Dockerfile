# Use Python 3.10 (or change to 3.11 if needed)
FROM python:3.10

# Install MySQL/MariaDB client headers
RUN apt-get update && apt-get install -y default-libmysqlclient-dev

# Create and activate virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
