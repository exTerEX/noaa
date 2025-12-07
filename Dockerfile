FROM python:3.14-slim

LABEL org.opencontainers.image.source="https://github.com/exTerEX/noaa"
LABEL org.opencontainers.image.description="NOAA Climate Data Online API Client"
LABEL org.opencontainers.image.licenses="MIT"

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy project files
COPY pyproject.toml uv.lock* ./
COPY noaa/ ./noaa/

# Install dependencies
RUN uv pip install --system --no-cache .

# Default command
CMD ["python", "-c", "from noaa import NOAA; print('NOAA API Client ready')"]