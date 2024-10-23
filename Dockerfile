FROM python:3.12

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8013

ENV PYTHONUNBUFFERED=1

CMD ["python3", "main.py"]