FROM python:3.11.6-slim

# Environment variables
ENV PYTHONUNBUFFERED=1

# Uvicorn configuration
ENV UVICORN_HOST=0.0.0.0
ENV UVICORN_PORT=8000
ENV UVICORN_RELOAD=true


RUN apt-get update \
    # dependencies for building Python packages && cleaning up unused files
    && apt-get install -y build-essential \
    libcurl4-openssl-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/*


# Python dependencies
RUN pip install --upgrade pip setuptools

WORKDIR /app/

# Copy project
COPY ./ ./

RUN pip install -r requirements.txt

EXPOSE $UVICORN_PORT

ENTRYPOINT ["python"]
CMD ["-m", "uvicorn", "src.main:app"]
