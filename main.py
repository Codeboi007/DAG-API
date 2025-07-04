from flask import Flask, render_template, request, send_file
import os
from werkzeug.utils import secure_filename

from logic import image as image_aug
from logic import text as text_aug
from logic import audio as audio_aug
from logic import tabular as tabular_aug

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/logic/image', methods=['GET', 'POST'])
def image():
    if request.method == 'POST':
        file = request.files['file']
        augmentation = request.form.get('augmentation')
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        output_path = image_aug.augment(file_path, augmentation)
        return send_file(output_path, as_attachment=True)

    return render_template('image.html')


@app.route('/logic/text', methods=['GET', 'POST'])
def text():
    if request.method == 'POST':
        text_input = request.form.get('text')
        augmentation = request.form.get('augmentation')
        result = text_aug.augment(text_input, augmentation)

        return f"<b>Original:</b> {text_input}<br><b>Augmented:</b> {result}"

    return render_template('text.html')


@app.route('/logic/audio', methods=['GET', 'POST'])
def audio():
    if request.method == 'POST':
        file = request.files['file']
        augmentation = request.form.get('augmentation')
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        output_path = audio_aug.augment(file_path, augmentation)
        return send_file(output_path, as_attachment=True)

    return render_template('audio.html')

@app.route('/logic/tabular', methods=['GET', 'POST'])
def tabular():
    if request.method == 'POST':
        file = request.files['file']
        augmentation = request.form.get('augmentation')
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        output_path = tabular_aug.augment(file_path, augmentation)
        return send_file(output_path, as_attachment=True)

    return render_template('tabular.html')


if __name__ == '__main__':
    app.run(debug=True)
