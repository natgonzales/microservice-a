# stores images locally

from flask import Flask, send_file, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) 

# variables 
UPLOAD_FOLDER = 'images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# directory
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# check if file is in allowed extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# upload route: checks if there is a file in the upload request
# validates file, saves to upload folder
@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['file']

    if file and allowed_file(file.filename):
        filename = file.filename
        try:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            app.logger.info(f'File {filename} uploaded successfully')
            return jsonify(message='File uploaded successfully', filename=filename), 201
        except Exception as e:
            app.logger.error(f'Error saving file: {e}')
            return jsonify(message='Error saving file'), 500

    app.logger.error('Invalid file type')
    return jsonify(message='Invalid file type'), 400

# check if file exists, sends file
@app.route('/images/<filename>')
def get_image(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        return send_file(file_path)
    app.logger.error('File not found')
    return jsonify(message='File not found'), 404

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
