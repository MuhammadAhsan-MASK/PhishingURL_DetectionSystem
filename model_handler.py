import joblib
import os
import pandas as pd
from feature_extractor import FeatureExtractor

class ModelHandler:
    def __init__(self, model_path='models/phishing_model.pkl'):
        self.model_path = model_path
        self.model = None
        self._load_model()
        
    def _load_model(self):
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
            print(f"Model loaded from {self.model_path}")
        else:
            print(f"Model not found at {self.model_path}. Please run train_model.py first.")
            
    def predict(self, url):
        if not self.model:
            # Fallback to rule-based if model is not loaded yet
            return self._rule_based_fallback(url)
            
        extractor = FeatureExtractor(url)
        features = extractor.get_features()
        
        # Convert features to DataFrame for model prediction (ensure same order as training)
        df = pd.DataFrame([list(features.values())])
        
        prediction = self.model.predict(df)[0]
        probability = self.model.predict_proba(df)[0][1] # Probability of being phishing
        
        return {
            'prediction': 'phishing' if prediction == 1 else 'safe',
            'confidence': round(probability * 100, 2) if prediction == 1 else round((1 - probability) * 100, 2),
            'features': features
        }
        
    def _rule_based_fallback(self, url):
        # Very simple fallback logic
        risk_score = 0
        if len(url) > 75: risk_score += 1
        if url.count('.') > 3: risk_score += 1
        if '@' in url: risk_score += 1
        if '-' in url: risk_score += 1
        
        is_phishing = risk_score >= 2
        return {
            'prediction': 'phishing' if is_phishing else 'safe',
            'confidence': 50.0,
            'features': {},
            'note': 'Using fallback rule-based system'
        }

if __name__ == "__main__":
    handler = ModelHandler()
    print(handler.predict("https://www.google.com"))
