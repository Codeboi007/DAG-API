# DAG API

**DAG (Data Augmentation Generator) API** is a modular Flask web application that allows users to upload and augment datasets of various types: images, text, audio, and tabular (CSV). The processed output is returned directly via the browser.

---

## Features

* Image Augmentation — rotate, flip, brightness adjustments
* Text Augmentation — synonym replacement, word deletion
* Audio Augmentation — pitch shifting, noise addition, time stretching
* Tabular Augmentation — Gaussian noise, row duplication
* Simple user interface built with Jinja2 templates
* Modular backend logic for easy maintenance and expansions

---

## Project Structure

```
dag_api/
├── app.py
├── requirements.txt
├── augment/
│   ├── image.py
│   ├── text.py
│   ├── audio.py
│   └── tabular.py
├── templates/
│   ├── home.html
│   ├── image.html
│   ├── text.html
│   ├── audio.html
│   ├── tabular.html
│   └── video.html
├── static/
│   └── style.css
└── uploads/
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/dag-api.git
cd dag-api
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask server

```bash
python app.py
```

Then visit `http://localhost:5000` in your browser.

---

## Use Cases

* Generate synthetic variations of images for machine learning
* Enrich NLP datasets with basic text augmentations
* Add noise or shift pitch on audio clips for training
* Modify tabular datasets for robustness testing

---

## Technologies Used

* Python 3.9+
* Flask and Jinja2
* Torch and Torchvision
* Pillow
* Librosa and SoundFile
* Pandas and NumPy
* Scikit-learn (optional for future features)

---

## Planned Improvements

* Video augmentation support
* Cloud integration for file uploads/downloads
* Augmentation history per session
* Result previews before download