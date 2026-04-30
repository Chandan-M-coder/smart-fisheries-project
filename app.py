import boto3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Connect to S3
s3 = boto3.client('s3')

# Download dataset
s3.download_file('smart-fisheries-data', 'fish_data.csv', 'fish_data.csv')

# Load data
data = pd.read_csv('fish_data.csv')

# Features and label
X = data[['temperature','ph','turbidity','oxygen']]
y = data['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Test prediction
new_data = pd.DataFrame([[30, 7.5, 20, 5]], columns=['temperature','ph','turbidity','oxygen'])
prediction = model.predict(new_data)
print("Prediction:", prediction)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Connect to S3
s3 = boto3.client('s3')

# Download dataset
s3.download_file('smart-fisheries-data', 'fish_data.csv', 'fish_data.csv')

# Load data
data = pd.read_csv('fish_data.csv')

# Features and label
X = data[['temperature','ph','turbidity','oxygen']]
y = data['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Test prediction
prediction = model.predict([[30, 7.5, 20, 5]])

print("Prediction:", prediction)
def feeding_recommendation(temp, oxygen):
    if oxygen < 4:
        return "Do NOT feed (Low oxygen)"
    elif temp < 25:
        return "Feed less (Low temperature)"
    elif temp > 32:
        return "Feed moderately (High temperature)"
    else:
        return "Feed normally"
feed = feeding_recommendation(30, 5)
print("Feeding Advice:", feed)
