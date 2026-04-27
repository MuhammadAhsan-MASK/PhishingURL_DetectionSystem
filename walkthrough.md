# Phishing Detection System Walkthrough

I have successfully developed and verified the **Phishing Detection System**. This tool provides real-time URL analysis using a Random Forest machine learning model and a premium, dark-themed web interface.

## 🚀 Key Features Accomplished

- **Intelligent Detection**: Uses a Scikit-Learn Random Forest model trained on common phishing patterns.
- **Dynamic Feature Extraction**: Analyzes URL length, subdomains, SSL status, and malicious character patterns in real-time.
- **Premium UI**: Dark glassmorphism design with responsive elements, glowing accents, and smooth transitions.
- **API Integrated**: Flask-driven backend providing seamless communication between the ML model and the frontend.

## 🧪 Verification Results

I tested the application with both safe and known phishing-style URLs to ensure accuracy.

````carousel
![Safe URL Scan (google.com)](/C:/Users/M. Ahsan/.gemini/antigravity/brain/59e0e893-0b70-4b89-a507-1a5cadf92c5d/google_scan_result_1777213160424.png)
<!-- slide -->
![Phishing URL Scan (malicious example)](/C:/Users/M. Ahsan/.gemini/antigravity/brain/59e0e893-0b70-4b89-a507-1a5cadf92c5d/phishing_scan_result_1777213184852.png)
````

### 🛠️ Technical Details
- **Backend**: Python 3.13, Flask 3.1.0
- **Machine Learning**: Scikit-Learn (Random Forest Classifier)
- **Frontend**: Vanilla HTML5, CSS3 (Glassmorphism), JavaScript (ES6)

## 📦 How to Run
1. Ensure dependencies are installed: `pip install -r requirements.txt`
2. Run the server: `python app.py`
3. Access the dashboard at `http://127.0.0.1:5000`
