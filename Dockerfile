FROM ubuntu:latest
RUN apt update -y && apt install -y python3 python3-pip dash
WORKDIR /app 
COPY . . 
RUN pip3 install -r requirements.txt 
CMD ["python3","./main.py"]