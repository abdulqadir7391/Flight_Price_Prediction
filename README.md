# ✈️ Flight Price Prediction
This project predicts the price of a flight ticket based on user-selected inputs--
such as **airline**, **source city**, **destination**, and **number of stops**.  
Built using **Machine Learning** and presented through a **Streamlit UI**.
This tool helps understand how travel variables affect flight cost.

---

## 📂 Project Structure
Flight_Price_Prediction/
│
├── Outputs/ # Example UI screenshots and results
│ ├── Final Prediction.jpg
│ ├── Flight Destination Location.jpg
│ ├── Flight Names.jpg
│ ├── Flight Source Location.jpg
│ └── Flight Stops.jpg
│
├── templates/ # Templates folder (unused in Streamlit version)
│ └── index.html
│
├── apps.py # Streamlit app file
├── feature_names.pkl # Model feature mapping file
├── flight_price.xlsx # Dataset used for training
├── new.ipynb # Notebook for model experimentation
└── README.md # Project documentation

## 🧠 Model Details
- Model Type: **Regression Model**
- Library: `scikit-learn`
- Saved as: `flight_price_model.pkl`
- Encoding: **One-hot encoding** for categorical features such as:
  - Airline  
  - Source  
  - Destination  
  - Number of stops  

The model predicts the estimated ticket price in **Indian Rupees (₹).**
