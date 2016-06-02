PDF Generator Flask microservice
================================

[![Docker Pulls][docker pulls svg]][docker hub]
[![License][license svg]][license]

This is a microservices that handles pdfkit wich uses wkhtmltopdf and makes it a microservice
to make it easy the PDF generation.

Manual install
--------------

```bash
pip install -r requeriments.txt
```

### Starting server

```bash
python app.py
```

### Build Docker container

```bash
docker build -t ciricihq/wkhtmltopdf-aas .
```

### Starting Docker container

```bash
docker run -d --name wkhtmltopdf-aas -p <hostport>:80 ciricihq/wkhtmltopdf-aas
```

Docker hub installation
-----------------------

~~~bash
docker run -d --name wkhtmltopdf-aas -p <hostport>:80 ciricihq/wkhtmltopdf-aas
~~~

Builds are automatically generated from github. So there's no need tu push the
images again.

Testing the microservice
------------------------

Testing providing url to render:

```bash
curl -F "url=http://cirici.com" 'http://localhost:5000/pdf' > youramazingfile.pdf
```


Testing uploading contents:

```bash
curl -F "content=@test.html" 'http://localhost:5000/pdf' > youramazingfile.pdf
```

You want to generate images? No problem just change the ``pdf`` endpoint to ``jpg``

Resources
---------

https://pypi.python.org/pypi/pdfkit

[docker hub]: https://hub.docker.com/r/ciricihq/wkhtmltopdf-aas/
[license]: https://github.com/ciricihq/wkhtmltopdf-flask-aas/blob/master/LICENSE.md
[docker pulls svg]: https://img.shields.io/docker/pulls/ciricihq/wkhtmltopdf-aas.svg?style=flat-square
[license svg]: https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square
