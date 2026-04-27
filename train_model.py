import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os
from feature_extractor import FeatureExtractor

# Sample URLs for initial training (Real projects would use PhishTank/Alexandria datasets)
data = [
    ("https://www.google.com", 0),
    ("https://www.amazon.com", 0),
    ("https://www.facebook.com", 0),
    ("https://www.apple.com", 0),
    ("https://www.microsoft.com", 0),
    ("https://www.github.com", 0),
    ("https://www.stackoverflow.com", 0),
    ("https://www.youtube.com", 0),
    ("https://www.wikipedia.org", 0),
    ("https://www.linkedin.com", 0),
    ("http://login-paypal.com.secure-update.php", 1),
    ("http://verify-appleid.com", 1),
    ("http://192.168.1.1/login.html", 1),
    ("http://amazon-security-check.ru", 1),
    ("http://free-bitcoins.xyz", 1),
    ("http://bank-of-america-verify.net", 1),
    ("http://netflix-payment-update.com", 1),
    ("http://secure-entry-alibaba.cn", 1),
    ("http://steam-community-login.org", 1),
    ("http://google-account-recovery-system.top", 1)
]

def train():
    features_list = []
    labels = []
    
    print("Extracting features from training data...")
    for url, label in data:
        extractor = FeatureExtractor(url)
        features = extractor.get_features()
        features_list.append(list(features.values()))
        labels.append(label)
        
    df = pd.DataFrame(features_list)
    
    X = df
    y = labels
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training Random Forest model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100}%")
    
    # Save the model
    if not os.path.exists('models'):
        os.makedirs('models')
    
    joblib.dump(model, 'models/phishing_model.pkl')
    print("Model saved to models/phishing_model.pkl")

if __name__ == "__main__":
    train()
