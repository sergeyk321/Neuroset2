FROM python:latest

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY . .

RUN set -xe \
&& apt-get update \
&& apt-get install python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 80
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]