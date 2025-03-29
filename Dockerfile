FROM python:3
WORKDIR /app
COPY random_number.py /app/random_number.py
CMD ["python", "/app/random_number.py"]