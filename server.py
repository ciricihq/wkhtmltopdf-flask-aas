from flask import Flask, Response, request
import pdfkit
app = Flask(__name__)

config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')

@app.route("/pdf", methods=['POST'])
def pdf():
    # We are getting the url to generate from a form parameter
    if ('url' in request.form):
        print("URL provided: " + request.form['url'])
        pdf = pdfkit.from_url(str(request.form['url']), output_path=False, configuration=config)

    # If we are receiving the html contents from a uploaded file
    elif ('content' in request.files):
        print("File provided: " + request.files['content'])
        f = request.files['content']
        pdf = pdfkit.from_file(f, output_path=False, configuration=config)

    else:
        print(request.files)

    if (pdf):
        return Response(pdf, mimetype='application/pdf')
    else:
        return Response("error")

@app.route("/jpg", methods=['POST'])
def jpg():
    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltoimage')
    pdf = pdfkit.from_url('http://google.com', False, configuration=config)
    return Response(pdf, mimetype='image/jpg')

if __name__ == "__main__":
    app.run(debug=True)
