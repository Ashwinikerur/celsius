FROM python:3.14.0
WORKDIR /celsius
COPY . .
CMD ["python", "celsius_to_fahrenheit.py"]
