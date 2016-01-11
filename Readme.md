# PDF Generator Flask microservice

This is a microservices that handles pdfkit wich uses wkhtmltopdf and makes it a microservice
to make it easy the PDF generation.

## Manual install

```bash
pip install -r requeriments.txt
```

## Starting server

```bash
python server.py
```

## Build Docker container

```bash
docker build -t cirici/wkhtmltopdf-aas .
```

## Starting Docker container

```bash
docker run -d --name wkhtmltopdf-aas -p <hostport>:5000 cirici/wkhtmltopdf-aas
```

## Testing the microservice

Testing providing url to render:

```bash
curl -F "url=http://cirici.com" 'http://localhost:5000/pdf' > youramazingfile.pdf
```


Testing uploading contents:

```bash
curl -F "content=@test.html" 'http://localhost:5000/pdf' > youramazingfile.pdf
```

You want to generate images? No problem just change the ``pdf`` endpoint to ``jpg``

## Resources

https://pypi.python.org/pypi/pdfkit
