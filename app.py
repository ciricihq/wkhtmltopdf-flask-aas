from flask import Flask, Response, request
from werkzeug import secure_filename
import pdfkit
app = Flask(__name__)

tmpfolder = "/tmp/"

@app.route("/pdf", methods=['POST'])
def pdf():
    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
    doc = handle_request(config)
    return Response(doc, mimetype='application/pdf')

@app.route("/jpg", methods=['POST'])
def jpg():
    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltoimage')
    doc = handle_request(config)
    return Response(doc, mimetype='image/jpg')


def handle_request(config):
    # We are getting the url to generate from a form parameter
    options = {}
    options = request.values.getlist('options', type=float)
    print(options)

    # Converting post options group to dictionary
    listname = 'options'
    options = dict()
    for key, value in request.form.items():
        if key[:len(listname)] == listname:
            options[key[len(listname)+1:-1]] = value

    if ('url' in request.form):
        print("URL provided: " + request.form['url'])
        pdf = pdfkit.from_url(str(request.form['url']), output_path=False, configuration=config, options=options)

    # If we are receiving the html contents from a uploaded file
    elif ('content' in request.files):
        print("File provided: " + str(request.files['content']))
        f = request.files['content']
        f.save(tmpfolder + secure_filename(f.filename))

        pdf = pdfkit.from_file(tmpfolder + secure_filename(f.filename), output_path=False, configuration=config, options=options)

    return pdf

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
