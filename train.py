from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# 1. Load the data
iris = load_iris()
X = iris.data      # measurements: 150 rows × 4 columns
y = iris.target    # species as numbers: 0, 1, 2

# 2. Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Train the model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# 4. Check how good it is on data it has never seen
accuracy = accuracy_score(y_test, clf.predict(X_test))
print(f"Test accuracy: {accuracy:.2%}")

# 5. Save the model + species names into one file
joblib.dump(
    {"model": clf, "target_names": [str(n) for n in iris.target_names]},
    "model.joblib",
)
print("Saved model.joblib")