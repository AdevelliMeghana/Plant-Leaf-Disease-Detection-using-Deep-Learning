# 🌿 Plant Leaf Disease Detection using Deep Learning  

## 📘 Overview  
This project presents a **deep learning–based system** for detecting diseases in plant leaves using the **MobileNetV2** architecture.  
It helps farmers and agricultural researchers quickly identify crop diseases by analyzing leaf images.  

The model is trained on a dataset of **70,000+ images** from **38 disease categories** (including healthy leaves) and achieves **over 94% multi-class accuracy**.  
A **Streamlit web app** allows users to upload an image and instantly view disease predictions and confidence scores.

---

## 🧠 Features  
- ✅ Detects **38 different plant diseases**  
- 🌱 Trained using **MobileNetV2 (Transfer Learning)**  
- ⚙️ **Streamlit Web App** for real-time prediction  
- 🧩 Checks for image clarity before prediction  
- 📈 Achieved **99% accuracy** for healthy/diseased classification  
- 💾 Modular and reusable code design  

---

## 🧰 Tech Stack  
- **Language:** Python 3.11  
- **Frameworks & Libraries:** TensorFlow, Keras, OpenCV, NumPy, Matplotlib, Streamlit  
- **Development Environment:** Google Colab  
- **Deployment:** Streamlit Web App  

---

## 📂 Project Structure  
plant-leaf-disease-detection/
│
├── code/
│ ├── plant_disease_training_colab.ipynb ← Model training (Google Colab)
│ └── streamlit_app.py ← Streamlit deployment code
│
├── docs/
│ ├── project_documentation.pdf ← Full report
│ └── presentation_slides.pptx ← Presentation
│
├── dataset_link/README.md ← Dataset & model download link
├── user_instructions.md ← Step-by-step execution guide
├── requirements.txt ← Python dependencies
├── assets/ ← Screenshots & sample images
└── README.md ← This file

---

## ⚙️ How to Run  

### 1️⃣ Setup  
1. Clone the repository  
   ```bash
   git clone https://github.com/YourUsername/plant-leaf-disease-detection.git
   cd plant-leaf-disease-detection
   
Install dependencies
pip install -r requirements.txt
2️⃣ Run the Streamlit App
streamlit run code/streamlit_app.py


Upload a clear image of a plant leaf and get instant results with the disease name, health status, and confidence score.

📊 Model Performance
Metric	Result
Training Accuracy	97.8%
Validation Accuracy	94.6%
Healthy vs Diseased Detection	99%
Architecture	MobileNetV2 (Transfer Learning)
📸 Screenshots
<img width="1732" height="684" alt="image" src="https://github.com/user-attachments/assets/3e154bdb-4ff3-43f8-a8a5-b4d60c61d279" />
![Uploading image.png…]()

🔮 Future Enhancements

Add treatment recommendations for each disease

Extend dataset with new plant species

Deploy on mobile using TensorFlow Lite for offline access

Include voice-based assistant for ease of use

👩‍💻 Authors

245622737001 – Adevelli Meghana
245622737006 – Bhavagnya Kandunuri
245622737301 – Abraboina Harshitha

Guided by K. V. Nanda Kishore

🪴 Acknowledgment

Developed as a Mini Project under the Department of Computer Science and Engineering.

🏷 Tags

Deep Learning · Computer Vision · TensorFlow · Keras · Streamlit · Plant Disease Detection · Agriculture AI.
