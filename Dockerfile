FROM debian:jessie

MAINTAINER Genar Trias <genar@cirici.com>

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    gdebi \
    wget \
    python-pip

WORKDIR /tmp

RUN wget --no-check-certificate https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.jessie_amd64.deb && \
    gdebi --n wkhtmltox_0.12.5-1.jessie_amd64.deb && \
    rm wkhtmltox_0.12.5-1.jessie_amd64.deb

RUN ln -s /usr/local/bin/wkhtmltopdf /usr/bin/wkhtmltopdf
RUN ln -s /usr/local/bin/wkhtmltoimage /usr/bin/wkhtmltoimage

WORKDIR /

COPY app.py /app.py
COPY requeriments.txt /requeriments.txt

RUN pip install -r requeriments.txt

EXPOSE 80

CMD ["python","app.py"]
