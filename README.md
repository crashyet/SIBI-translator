# SIBI Detector

SIBI Translator is an open-source project that aims to recognize and translate hand gestures based on the Indonesian Sign Language System (SIBI). Make sure you have Python installed before using this program. Here's how to install it.

## Install this program

### Cloning this repository

```bash
git clone https://github.com/crashyet/SIBI-translator.git
cd SIBI-translator
```

### Install Dependency

```bash
pip install -r requirements.txt
```

## How To Use It
### Collect Data

Use this script to obtain images as a dataset.

```bash
python3 collect_dataset.py
```

Note: If you already have a dataset, you can copy and paste it into the data folder. If the folder doesn't exist, you can create it first.

```bash
mkdir data
```

### Create Dataset
```bash
python3 create_dataset.py
```

This script functions to process the dataset in the data folder and save it in a file called <b>data.create</b>.

### Training Dataset
```bash
python3 training.py
```

This script is used to train a gesture classification model.

### Training Dataset
```bash
python3 main.py
```

Run the script to detect and predict hand gestures in real-time.
