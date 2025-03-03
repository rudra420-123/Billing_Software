
# BillingSoftware 🧾
A simple and responsive billing system built with **Flask** for managing and generating bills for a Biriyani shop. This app allows you to select items, calculate the total, and generate a printable bill.

---

## 📋 Features
- **Auto-generate bill numbers** sequentially.
- **Responsive UI** with HTML, CSS.
- Save bills as `.txt` files in the `bills` folder.
- Automatic opening of the browser when the app starts.
- User-friendly and easy to use.

---

## 🛠 Requirements
Make sure you have **Python 3.8+** installed. Then, install the necessary packages:
```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt` file, create one with this command:
```bash
pip freeze > requirements.txt
```

---

## ⚙️ How to Run the App Locally
1. **Clone the repository**:
   ```bash
   git clone https://github.com/rudra420-123/Billing_Software.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd BillingSoftware
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app**:
   ```bash
   python app.py
   ```

5. **Open your browser** (if it doesn’t open automatically) and go to:
   ```
   http://127.0.0.1:5000/
   ```

---

## 🗂 Project Structure
```
BillingSoftware/
├── app.py               # Main Python file for Flask app
├── requirements.txt     # Dependencies for the project
├── README.md            # Project documentation
├── bills/               # Folder to save generated bills
├── templates/           # HTML files
│   ├── index.html
├── static/              # CSS, JS, and images
│   ├── css/
│       ├── style.css
```

---

## 🚀 Building the `.exe` File (Optional)
To create an executable file using **PyInstaller**, run:
```bash
pyinstaller --name BillingSoftware --onefile --add-data "templates;templates" --add-data "static;static" --add-data "bills;bills" app.py
```

- Find the `.exe` file in the `dist` folder.

---

## 🔧 Troubleshooting
1. **Flask not found error**:
   ```bash
   pip install flask
   ```

2. **Dependencies not installing**:
   ```bash
   pip install -r requirements.txt
   ```
---
# Happy Billing! 🧾😊