# PDF Generator Flask microservice

This is a microservices that handles pdfkit wich uses wkhtmltopdf and makes it a microservice
to make it easy the PDF generation.

## Testing the microservice

Testing providing url to render:

```bash
curl -F "url=http://cirici.com" 'http://localhost:5000/pdf' > youramazingfile.pdf
```


Testing uploading contents:

```bash
curl -F "content=@test.html" 'http://localhost:5000/pdf' > youramazingfile.pdf
```

## Resources

[https://pypi.python.org/pypi/pdfkit]
