import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE

# Load the dataset
data = pd.read_csv(r"C:\Users\abhis\OneDrive\Desktop\finance_data_final.csv", encoding='latin1')

# Separate features (X) and target variable (y)
X = data.drop(columns=['class', 'Companies'])
y = data['class']

# Apply SMOTE oversampling to the data
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_resampled)

# Initialize KFold with 3 folds
kf = KFold(n_splits=3, shuffle=True, random_state=42)

# Lists to store accuracy and error rate 
accuracies = []
error_rates = []

# Initialize the confusion matrix
conf_matrix = np.zeros((3, 3))

for train_index, test_index in kf.split(X_scaled):
    X_train_fold, X_test_fold = X_scaled[train_index], X_scaled[test_index]
    y_train_fold, y_test_fold = y_resampled[train_index], y_resampled[test_index]

    # Initialize KNN classifier
    knn_classifier = KNeighborsClassifier(n_neighbors=5)

    # Train the KNN classifier
    knn_classifier.fit(X_train_fold, y_train_fold)

    # Predict on the test fold 
    y_pred_fold = knn_classifier.predict(X_test_fold)

    # Calculate accuracy and error rate for the fold
    accuracy_fold = accuracy_score(y_test_fold, y_pred_fold) * 100
    error_fold = 100 - accuracy_fold

    # Update the confusion matrix
    conf_matrix += confusion_matrix(y_test_fold, y_pred_fold)

    accuracies.append(accuracy_fold)
    error_rates.append(error_fold)

# Calculate average accuracy and error rate
avg_accuracy = np.mean(accuracies)
avg_error_rate = np.mean(error_rates)

print("Average Accuracy:", round(avg_accuracy))
print("Average Error Rate:", round(avg_error_rate))

# Print classification report
print(classification_report(y_test_fold, y_pred_fold))

# Plot confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, cmap='Blues', fmt='g', cbar=False)
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.title('Confusion Matrix')
plt.show()

# Calculate precision and recall from confusion matrix
precision = conf_matrix[1, 1] / (conf_matrix[1, 1] + conf_matrix[0, 1])  # TP / (TP + FP)
recall = conf_matrix[1, 1] / (conf_matrix[1, 1] + conf_matrix[1, 0])     # TP / (TP + FN)

print("Precision:", precision)
print("Recall:", recall)

# Print cross-validation scores
print("Cross-Validation Scores:", accuracies)
print("Mean Accuracy after validation:", round(avg_accuracy))

# Plot accuracy and error rate
plt.figure(figsize=(4, 4))
plt.bar(['Accuracy', 'Error Rate'], [avg_accuracy, avg_error_rate], color=['green', 'red'])
plt.ylim(0, 100)
plt.ylabel('Percentage')
plt.title('Accuracy and Error Rate')
plt.show()
