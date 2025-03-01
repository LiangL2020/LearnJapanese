"""
Date: 2/11/2025 
Initial idea: create a panel that asks user to one write haragana/katakana and repeats 
Subtasks: 
- needs to write a ML model that learns haragana and katakana 
- create a panel that collects hand written data to train the model 
"""
import os
import numpy as np
import cv2
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

model_type = "svm"
char_type = ['hiragana', 'katakana']
data_dir = os.path.join('.', 'data', char_type[0])
X, y = [], []
labels = []
label_index = {}

for file in os.listdir(data_dir):
    if file.endswith('.png'):
        label = file.split('_')[0]  # Extract label from filename
        img_path = os.path.join(data_dir, file)
        
        # Read and preprocess image
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (32, 32))  # Resize to fixed size
        img = img.flatten() / 255.0  # Normalize and flatten
        
        # Store data
        if label not in label_index:
            label_index[label] = len(labels)
            labels.append(label)
        
        X.append(img)
        y.append(label_index[label])

# Convert to numpy arrays
X = np.array(X)
y = np.array(y)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

# Train model
# model = KNeighborsClassifier(n_neighbors=5)
# model = SVC(kernel='linear', probability=True)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save trained model
model_dir = os.path.join('.', 'model', char_type[0])
os.makedirs(model_dir, exist_ok=True)
model_path = os.path.join(model_dir, f'{model_type}_model.pkl')
joblib.dump(model, model_path)
print(f"Model saved as {model_path}")

# Evaluate model
y_pred = model.predict(X_test)
unique_classes = sorted(set(y_test) | set(y_pred)) 
filtered_labels = [labels[i] for i in unique_classes] 
cm = confusion_matrix(y_test, y_pred, labels=unique_classes)

print("Confusion Matrix:")
print(cm)
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=labels))

# Plot confusion matrix
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix")
plt.show()
