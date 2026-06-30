import os
import cv2
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

dataset_path = "test_set/test_set"
categories = ["cats", "dogs"]
data = []
labels = []

print("Loading Images...")

for category in categories:

    folder = os.path.join(dataset_path, category)

    for image_name in os.listdir(folder)[:500]:

        image_path = os.path.join(folder, image_name)

        try:

            image = cv2.imread(image_path)

            if image is None:
             continue

            image = cv2.resize(image, (32, 32))

            data.append(image)
            labels.append(category)

        except:
            pass

print("Images Loaded Successfully!")
print("Total Images Loaded:", len(data))

# Convert to NumPy array

data = np.array(data)
labels = np.array(labels)

print("Dataset Shape :", data.shape)

# Flatten Images

data = data.reshape(len(data), -1)

print("Flatten Shape :", data.shape)

# Split Dataset

X_train, X_test, y_train, y_test = train_test_split(
    data,
    labels,
    test_size=0.2,
    random_state=42
)

print("Training Images :", len(X_train))
print("Testing Images :", len(X_test))

# Train SVM

print("\nTraining Model...")

model = SVC(kernel="linear", max_iter=1000)
model.fit(X_train, y_train)

print("Training Completed!")

# Prediction

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print("\nAccuracy :", accuracy)

print("\nClassification Report")

print(classification_report(y_test, prediction))

print("\nConfusion Matrix")

print(confusion_matrix(y_test, prediction))
