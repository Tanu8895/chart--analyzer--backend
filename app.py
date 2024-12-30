import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Chart Analyzer API!"

@app.route('/analyze', methods=['POST'])
def analyze_chart():
    if 'image' not in request.files:
        return jsonify({"signal": "No image uploaded!"})

    image = request.files['image']
    image_path = f"./uploads/{image.filename}"
    image.save(image_path)

    # Placeholder for processing logic
    signal = "Trade (Up)" if image.filename.endswith('.png') else "No Trade"
    return jsonify({"signal": signal})

if __name__ == '__main__':
    # Port configuration
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
