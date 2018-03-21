FROM python:alpine

MAINTAINER Genar Trias <genar@cirici.com>

RUN apk add --update --no-cache wkhtmltopdf --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ \
        --allow-untrusted && \
    apk add xvfb

WORKDIR /

COPY app.py /app.py
COPY requeriments.txt /requeriments.txt

RUN pip install -r requeriments.txt

EXPOSE 80

CMD ["python","app.py"]
