# S3 Bucket List Viewer Using Boto3

This project is a simple web application that retrieves and displays the list of objects stored in an AWS S3 bucket using Flask, Boto3, and JavaScript. It provides a REST API to fetch the bucket contents and a frontend to display them.

## 🚀 Features
- Fetch and display S3 bucket file list.
- Uses Flask to create a REST API.
- Frontend interacts with the API using JavaScript.
- CORS enabled to allow frontend requests.

---

## 🛠️ Setup and Execution Guide

### 1️⃣ Prerequisites
Ensure you have the following installed:
- Python 3
- AWS CLI (Configured with your credentials)
- Flask & Boto3

### 2️⃣ Clone the Repository
```sh
git clone <your-repo-url>
cd bucketlist
```

### 3️⃣ Set Up a Virtual Environment
```sh
python3 -m venv myenv
source myenv/bin/activate  # On Windows, use myenv\Scripts\activate
```

### 4️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
If `requirements.txt` is missing, manually install:
```sh
pip install flask boto3 flask_cors
```

### 5️⃣ Configure AWS Credentials
Ensure your AWS CLI is configured:
```sh
aws configure
```
Provide your AWS Access Key, Secret Key, Region, and Output format.

### 6️⃣ Run the Flask Server
```sh
python bucketlist.py
```
Your API will start at `http://0.0.0.0:5000/list-files`.

### 7️⃣ Open the Frontend
- Open `index.html` in a browser.
- The website will fetch and display S3 bucket file list.

---

## 📌 API Endpoint
### `GET /list-files`
Fetches and returns the list of files stored in the S3 bucket.
#### **Response Example:**
```json
{
  "files": [
    "image1.jpg",
    "document.pdf",
    "profile.png"
  ]
}
```

---

## 🎯 Deployment (Optional)
To run this on a cloud server (e.g., AWS EC2):
1. SSH into your instance.
2. Set up the environment as above.
3. Run `python bucketlist.py &` to keep it running in the background.

For production, use **Gunicorn**:
```sh
pip install gunicorn
nohup gunicorn -w 4 -b 0.0.0.0:5000 bucketlist:app &
```

---

## 💡 Future Enhancements
- Add file upload feature.
- Implement authentication for bucket access.
- Improve UI/UX.

---

### 🎉 **Contributions & Feedback**
Feel free to fork the repo and submit pull requests. Let me know if you have any questions or suggestions! 🚀

# BucketList
