# 🥦 Food Waste Tracker

A simple and practical **Python + Streamlit web app** that helps users **track groceries and reduce food waste** by monitoring expiry dates.  
Color-coded alerts highlight items that are **expired** or **about to expire**, encouraging smarter food usage and sustainability.

---

## 🚀 Features

✅ Add food items with:
- Name  
- Category (e.g. Dairy, Meat, Fruit, etc.)  
- Quantity  
- Storage location (Fridge, Freezer, Pantry)  
- Expiry date  

✅ Automatically:
- Calculates days left until expiry  
- Highlights **expired (red)** and **soon-to-expire (orange)** items  
- Sorts by expiry date for easy viewing  

✅ Manage your items:
- View all stored foods in an interactive table  
- Delete used or unwanted items  
- Stores data locally using SQLite  

---

## 🖼 Preview

*(Add a screenshot or GIF of your app here if possible!)*  
Example:  
![App Screenshot](screenshot.png)

---

## 🧰 Tech Stack

- **Python 3.10+**
- **Streamlit** – for the interactive web interface  
- **SQLite** – for local data persistence  
- **Pandas** – for data handling and table display  

---

## 🗂 Project Structure

FOOD-WASTE-TRACKER/
│
├── app.py # Main Streamlit app
├── db.py # Database logic (CRUD operations)
├── requirements.txt # Project dependencies
├── .gitignore # Files to ignore (cache, DB, etc.)
└── README.md # This file

yaml
Copy code

---

## ⚙️ Installation & Usage

### 1️⃣ Clone this repository
```bash
git clone https://github.com/YOUR-USERNAME/food-waste-tracker.git
cd food-waste-tracker
2️⃣ Create a virtual environment (optional but recommended)
bash
Copy code
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run the app
bash
Copy code
streamlit run app.py
5️⃣ Open in your browser
By default, Streamlit runs on:
👉 http://localhost:8501

🧠 How It Works
When you add a food item, it’s saved to a local SQLite database (fridge.db).

Each time the app loads, it reads the data, computes how many days remain until expiry, and displays results in tables.

Items expiring in ≤3 days are highlighted in orange.

Expired items are highlighted in red.

You can delete items when you’ve used them or they’re no longer needed.

🌟 Possible Future Improvements
💡 Planned next steps:

🔔 Email reminders for soon-to-expire foods

🍽 Recipe suggestions using a public recipe API

📊 Analytics dashboard (e.g. category stats, waste trends)

📱 Mobile-friendly layout

☁️ User accounts or cloud sync

📸 Example Use Case
“I always forget what’s hiding in my fridge!
This app helps me track expiry dates and reminds me to use up ingredients before they go bad — saving money and reducing waste.”

🌐 Live Demo
If deployed on Streamlit Cloud, add your link here:
👉 Live App Demo

🧑‍💻 Author
Your Name

💼 LinkedIn

🐙 GitHub

✉️ your.email@example.com

🪪 License
This project is open-source and available under the MIT License.

⭐ If you found this project interesting, give it a star on GitHub!