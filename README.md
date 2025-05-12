# 🏔️ COM727 Everest Chatbot

This project is an AI-based intent classification chatbot built for the **COM727 - Artificial Intelligence** module. The chatbot is trained to answer a wide range of questions related to **Mount Everest**, such as its location, height, climbers, risks, and more.

It includes:
- Training the chatbot model using intent data
- Evaluating its performance with precision, recall, F1-score
- Running an interactive chatbot in the terminal

---

## 📁 Project Structure

COM727_Everest_Chatbot/
│
├── chatbot/
│ ├── chatbot.py # Main chatbot script (user interacts here)
│ └── intents.json # Data file containing patterns and responses
│
├── model/
│ ├── training.py # Trains the model and saves all artifacts
│ ├── evaluate_model.py # Evaluates the model and generates reports
│ ├── chatbot_model.keras # Trained neural network model
│ ├── words.pkl # Preprocessed vocabulary used in BoW
│ ├── classes.pkl # All predicted tags (labels)
│ ├── training_data.pkl # Saved training features and labels
│ └── training_history.pkl # Tracks loss and accuracy per epoch
│
├── evaluation/
│ ├──evaluation_report.csv # Generated classification metrics (CSV)
│ ├──evaluation_table.png # Table of metrics (PNG image)
│ └── evaluation_metrics_chart.png# Chart of precision, recall, f1-score
│
├── requirements.txt # List of required Python packages
└── README.md # Project documentation (this file)


---

## ⚙️ Setup Instructions

### ✅ Step 1: Clone the project

```bash
git clone https://github.com/yourusername/COM727_Everest_Chatbot.git
cd COM727_Everest_Chatbot


# 2. Create a virtual environment
python3 -m venv venv

# 3. Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# 4. Install required packages
pip install -r requirements.txt

# (Optional) If you didn’t freeze "requirements.txt" or "requirements.txt" is missing.
pip install tensorflow keras scikit-learn nltk matplotlib dataframe_image


