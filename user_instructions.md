# ⚙️ Instructions to Run the Project

## 🪴 1️⃣ Setup and Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/YourUsername/plant-leaf-disease-detection.git
   cd plant-leaf-disease-detection
Install Dependencies
Make sure Python 3.11 or later is installed.
Then install all required libraries using:

bash
Copy code
pip install -r requirements.txt
Download the Dataset and Model

Dataset and trained model are provided via Google Drive.

Download link: (Add your Google Drive link here)

After downloading:

Extract dataset into a folder named dataset/

Place the trained model file (plant_disease_detector_v2.keras) in:

Copy code
model/
🌿 2️⃣ Running the Streamlit Web App
To launch the prediction app:

bash
Copy code
streamlit run code/streamlit_app.py
Then open the link shown in the terminal (e.g. http://localhost:8501) in your web browser.

💻 Inside the App:
Upload a clear image of a plant leaf (.jpg, .png, .jpeg).

The app will:

Check image clarity (detects blurriness).

Predict whether the leaf is Healthy or Diseased.

Display the disease name and confidence score.

🧠 3️⃣ Model Training (Optional)
To retrain the model yourself:

Open the Colab notebook:

bash
Copy code
code/plant_disease_training_colab.ipynb
Run all cells in Google Colab (enable GPU).

The trained model will be saved as:

Copy code
plant_disease_detector_v2.keras
🪄 4️⃣ Project File Overview
File / Folder	Description
code/plant_disease_training_colab.ipynb	Model training & evaluation notebook
code/streamlit_app.py	Streamlit web app for predictions
docs/project_documentation.pdf	Detailed report
docs/presentation_slides.pptx	Project presentation
requirements.txt	List of Python dependencies
assets/	Screenshots & sample images
model/	Saved trained model
dataset_link/README.md	Contains dataset & model links

🌾 5️⃣ Notes
Use clear, focused leaf images for accurate results.

Blurry or dark images may reduce prediction accuracy.

The app uses MobileNetV2 for efficient and accurate detection.

For retraining, GPU is recommended.
