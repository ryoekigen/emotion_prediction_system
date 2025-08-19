# ================== Base image ==================
FROM python:3.9-slim

# ================== Set working directory ==================
WORKDIR /app

# ================== Install dependencies ==================
# Prevents python from writing pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install pip dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ================== Copy project files ==================
COPY ./app ./app

# ================== Expose FastAPI port ==================
EXPOSE 8000

# ================== Start FastAPI app ==================
# --host 0.0.0.0 makes it accessible outside the container
# --reload is optional (useful in dev, not in prod)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]