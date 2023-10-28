FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y
RUN apt-get install -y python3-pip
RUN apt install python3-pip
RUN apt install dash
RUN pip3 install matplotlib
RUN pip3 install dash-ag-grid
RUN pip3 install dash-bootstrap-components
RUN pip3 install pandas

WORKDIR /usr/app/src
COPY  main.py ./
COPY  manifest.yaml ./
COPY 1000_Sales_Records.csv ./
CMD ["python3","./main.py"]