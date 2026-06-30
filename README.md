# Cat vs Dog Image Classification using Support Vector Machine (SVM)

## Project Overview

This project is a Machine Learning application that classifies images as either Cats or Dogs using the Support Vector Machine (SVM) algorithm.

The images are resized, flattened into feature vectors, and used to train an SVM classifier. The trained model is then evaluated using accuracy, a classification report, and a confusion matrix.

---

## Features

- Image classification using SVM
- Image preprocessing with OpenCV
- Image resizing (64 x 64)
- Flattening images into feature vectors
- Train/Test split
- Model evaluation
- Accuracy score
- Classification report
- Confusion matrix

---

## Technologies Used

- Python
- OpenCV
- NumPy
- Scikit-learn

---

## Project Structure

```
Task03_Cat_Dog_SVM/
│
├── model.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── test_set/
    └── test_set/
        ├── cats/
        └── dogs/
```

---

## Dataset

This project uses a Cats and Dogs image dataset stored inside the `test_set` folder.

Dataset structure:

```
test_set/
└── test_set/
    ├── cats/
    └── dogs/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Cat-Dog-Image-Classification-SVM.git
```

Move into the project folder

```bash
cd Cat-Dog-Image-Classification-SVM
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python model.py
```

---

## Sample Output

```
Loading Images...

Images Loaded Successfully!

Training Model...

Training Completed!

Accuracy : 0.525

Classification Report

Confusion Matrix
```

---

## Model Details

Algorithm: Support Vector Machine (SVM)

Image Size: 64 x 64

Libraries:
- OpenCV
- NumPy
- Scikit-learn

---

## Future Improvements

- Train on a larger dataset
- Improve accuracy using feature engineering
- Implement CNN for better performance
- Add a Streamlit or Flask web interface

---

## Author

Khushi

B.Tech Student

Python Developer

Machine Learning Enthusiast

---

## License

This project is created for educational and learning purposes.
