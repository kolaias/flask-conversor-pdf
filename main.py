import os
from flask import Flask, request, send_from_directory
from werkzeug.utils import secure_filename
from convert import docx_to_pdf

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['docx_file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            output_file = os.path.splitext(filename)[0] + '.pdf'
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_file)

            docx_to_pdf(os.path.join(app.config['UPLOAD_FOLDER'], filename), output_path)
            return send_from_directory(app.config['UPLOAD_FOLDER'], output_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
