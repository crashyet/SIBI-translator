import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data
with open('./data.create', 'rb') as f:
    data_dict = pickle.load(f)

data = np.array(data_dict['data'])
labels = np.array(data_dict['labels'])

# Split data
x_train, x_test, y_train, y_test = train_test_split(
    data, labels, test_size=0.2, stratify=labels, shuffle=True
)

# Train model
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Evaluate
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'{accuracy * 100:.2f}% of samples were classified correctly!')

# Save model
with open('model.training', 'wb') as f:
    pickle.dump({'model': model}, f)
