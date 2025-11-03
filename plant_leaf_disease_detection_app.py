import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import cv2

# Load the model
model = load_model("plant_disease_detector_v2.keras")

# Class labels
class_names = [
    'Apple__Apple_scab', 'Apple_Black_rot', 'Apple__Cedar_apple_rust', 'Apple__healthy',
    'Blueberry_healthy', 'Cherry(including_sour)_Powdery_mildew', 'Cherry_(including_sour)healthy',
    'Corn(maize)_Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)Common_rust',
    'Corn_(maize)_Northern_Leaf_Blight', 'Corn_(maize)healthy', 'Grape_Black_rot',
    'Grape_Esca(Black_Measles)', 'Grape__Leaf_blight(Isariopsis_Leaf_Spot)', 'Grape___healthy',
    'Orange__Haunglongbing(Citrus_greening)', 'Peach__Bacterial_spot', 'Peach__healthy',
    'Pepper,bell_Bacterial_spot', 'Pepper,_bell_healthy', 'Potato__Early_blight',
    'Potato__Late_blight', 'Potato_healthy', 'Raspberry__healthy', 'Soybean__healthy',
    'Squash_Powdery_mildew', 'Strawberry__Leaf_scorch', 'Strawberry__healthy',
    'Tomato_Bacterial_spot', 'Tomato__Early_blight', 'Tomato__Late_blight',
    'Tomato_Leaf_Mold', 'Tomato__Septoria_leaf_spot',
    'Tomato__Spider_mites Two-spotted_spider_mite', 'Tomato__Target_Spot',
    'Tomato__Tomato_Yellow_Leaf_Curl_Virus', 'Tomato__Tomato_mosaic_virus',
    'Tomato___healthy'
]

# Check image blurriness
def is_blurry(image):
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    lap_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    return lap_var < 100

# Preprocess image
def preprocess_image(img):
    img = img.resize((224, 224))
    img_array = img_to_array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

# Streamlit App
st.title("🌿 Plant Disease Detection App")
st.write("Upload a clear image of a plant leaf to check if it's healthy or diseased.")
st.write("The system uses a deep learning model (MobileNetV2) to identify the disease.")

# Upload image
uploaded_file = st.file_uploader("Upload a leaf image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    with st.expander("📷 Uploaded Image (Click to Hide)", expanded=True):
        st.image(image, caption="Uploaded Leaf Image", use_container_width=True)

    # Check image clarity
    if is_blurry(image):
        st.warning("🔍 The uploaded image seems blurry. Please upload a clearer image.")
    else:
        processed_img = preprocess_image(image)
        prediction = model.predict(processed_img)
        predicted_index = np.argmax(prediction)
        confidence = float(np.max(prediction)) * 100
        predicted_class = class_names[predicted_index]

        # Confidence check
        if confidence < 70:
            st.warning("⚠ The model is not confident about this prediction. Try a clearer image.")
        else:
            leaf_status = "Healthy" if "healthy" in predicted_class.lower() else "Diseased"

            st.markdown(
                f"### 🩺 **Leaf Health Status:** {leaf_status}"
            )
            st.markdown(
                f"### 🦠 **Predicted Class:** {predicted_class}"
            )
            st.markdown(
                f"### 📊 **Confidence Score:** {confidence:.2f}%"
            )
