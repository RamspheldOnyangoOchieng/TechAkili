# Use Python 3.10 (or your preferred version)
FROM python:3.10

# Install system dependencies (including Rust)
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    curl \
    libssl-dev \
    libffi-dev

# Install Rust (required for some Python packages)
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:$PATH"

# Create and activate virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
