# 📘 KnowledgeBot – AI Study Companion

KnowledgeBot is a full-stack AI-powered study assistant designed to help students learn more effectively. It provides instant answers to study-related questions, generates structured study plans, and includes a built-in Pomodoro focus timer for productivity.

This project uses **HTML, CSS, JavaScript** for the frontend and **Python (Flask)** with **Google Gemini API** for the backend.

---

## 🚀 Features

- 🤖 AI-powered study chatbot using Google Gemini  
- 📚 Generate detailed study plans for any topic  
- ⏱️ Pomodoro focus timer (25-minute sessions)  
- 🗂️ Chat history & multiple study sessions  
- 🎨 Modern, responsive UI  
- 🔁 Retry mechanism for API calls  

---

## 🛠️ Tech Stack

### Frontend
- HTML5  
- CSS3  
- JavaScript (Vanilla JS)  
- Lucide Icons  

### Backend
- Python  
- Flask  
- Google Gemini API  

---

## 📂 Project Structure

```
KnowledgeBot/
│
├── main.py              # Flask backend
├── index.html           # Frontend UI
├── README.md            # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/knowledgebot.git
cd knowledgebot
```

### 2️⃣ Create a Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate    # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install flask google-generativeai
```

---

## 🔑 API Configuration

⚠️ **Important:** Do NOT expose your API key publicly.

Replace your API key in `main.py`:

```python
client = genai.Client(api_key="YOUR_API_KEY")
```

💡 Tip: Use environment variables instead of hardcoding the API key.

---

## ▶️ Running the Application

```bash
python main.py
```

Open your browser and go to:

```
http://localhost:8000
```

---

## 🧪 How It Works

1. User enters a question in the chat UI  
2. Frontend sends the message to the Flask backend  
3. Backend forwards the prompt to Google Gemini  
4. Gemini generates a response  
5. Response is displayed in the chat window  

---

## 📌 Future Enhancements

- User authentication  
- Database support for chat history  
- Notes/PDF upload  
- Voice-based interaction  
- Dark mode  

---

## 👩‍💻 Author

**Nidamanuri Ram Pujitha**  
B.Tech Student | Aspiring Software Engineer  

---

## ⭐ Support

If you like this project, don’t forget to ⭐ the repository!
