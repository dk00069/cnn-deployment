from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 

@app.route("/")
def home():
    return "Waste Classifier API is running!"

# Load model once at startup
model = tf.keras.models.load_model("waste_final.h5")

# Define your class labels
class_labels = ["Cardboard", "Glass", "Metal", "Paper", "Plastic", "Trash"]  # update if needed

@app.route("/")
def home():
    return "Waste Classifier API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    img = Image.open(io.BytesIO(file.read())).convert("RGB").resize((224, 224))
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)

    predictions = model.predict(img_array)
    predicted_class = class_labels[np.argmax(predictions)]
    confidence = float(np.max(predictions))

    return jsonify({
        "prediction": predicted_class,
        "confidence": round(confidence * 100, 2)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)