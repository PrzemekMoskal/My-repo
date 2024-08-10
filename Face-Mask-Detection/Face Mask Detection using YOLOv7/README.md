```markdown
# Face Mask Detection Deep Learning Model using YOLOv7

## Overview

The Face Mask Detection System is a YOLOv7-based deep learning model trained to accurately recognize whether individuals in images and videos are wearing face masks or not. I wish to upgrade this system to being deployed as a web application using Flask, enabling real-time mask detection through a user-friendly interface.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Training Process](#model-training-process)
- [Evaluation and Analysis](#evaluation-and-analysis)
- [Inference and Deployment](#inference-and-deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

- Real-time face mask detection in images and videos.
- User-friendly web interface for uploading and processing files.
- Detailed performance metrics and visualizations.
- Efficient video compression and display.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/saleena-18/Face-X/Face-Mask-Detection/Face-Mask-Detection-using-YOLOv7.git
    cd Face-Mask-Detection-using-YOLOv7
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Download the trained model weights:**
    - Place the `best.pt` file in the `weights` directory.


## Project Structure

```
facemask-detection/
│
├── app/
│   ├── static/
│   ├── __init__.py
│   └── utils.py
│
├── weights/
│   └── best.pt
|   |__ last.pt
│
├── data/
│   ├── custom.yaml
│   └── hyp.scratch.p5.yaml
│
├── train.py
├── test.py
├── detect.py
├── requirements.txt
├── README.md
└── run.py
```

## Model Training Process

### Training Phase:
- **Configuration Setup:** The model is trained using the `train.py` script with specified parameters for workers, batch size, epochs, image size, configuration file, dataset details, hyperparameters, and device allocation.
- **Model Training:** The YOLOv7 architecture is employed for 120 epochs, customized for the face mask detection task.

### Evaluation and Analysis:
- **Analysis and Metrics:** Post-training, the model's performance is evaluated using the `test.py` script, generating various metrics and visualizations like predictions, results, confusion matrices, and precision-recall curves.

### Inference and Deployment:
- **Model Deployment:** The trained model is utilized for real-time inference on images and videos using the `detect.py` script.
- **Video Compression:** Resultant videos from the detection process are compressed using FFmpeg for efficient storage and display.

## Future upgrade

**Running the Flask application:**
    ```bash
    flask run
    ```
Once the Flask application is running, you can access the web interface at `http://127.0.0.1:5000/`. Use the interface to upload images or videos for face mask detection.

## License

This project is licensed under the MIT License.
```