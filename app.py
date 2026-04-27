from flask import Flask, request, jsonify, render_template
from model_handler import ModelHandler
import os

app = Flask(__name__)
handler = ModelHandler()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    url = data.get('url')
    
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    # Basic URL validation
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
        
    try:
        result = handler.predict(url)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Ensure static and template folders exist (already handled in setup)
    app.run(debug=True, port=5000)
