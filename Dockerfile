FROM python:latest

RUN mkdir /app/

WORKDIR /app/

COPY . .

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python", "app.py", "docker"]