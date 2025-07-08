import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score

df = pd.read_csv("sample_data.csv")

X = df[["temperature", "pressure", "engine_rpm"]]
y = df["code"]

# Split the data (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train the model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Test with a new sample
sample_input = pd.DataFrame({"temperature": [135], "pressure": [2.2], "engine_rpm": [1900]})
predicted_code = model.predict(sample_input)
print("\nPredicted fault code for input sample:", predicted_code[0])

# Show top 3 probable fault codes (multi-label scenario)
probas = model.predict_proba(sample_input)
top_n_idx = probas[0].argsort()[-3:][::-1]
top_codes = model.classes_[top_n_idx]
print("\nMost probable fault codes (top 3):", top_codes)

