# CLAUDE.md - AI Compliance App

## 🎯 What is this project?

A simple AI chatbot that helps check if documents follow the rules (compliance). It can answer questions and compare your documents with regulations.

## 🛠️ Tools We Use

### Backend (Server)
- **Python** - Programming language
- **UV** - Install Python packages super fast
- **FastAPI** - Create API endpoints easily
- **Hugging Face** - AI models for chatbot

### Frontend (Website)
- **React** - Build the user interface
- **Tailwind** - Make it look pretty

### Other Tools
- **Firebase** - User login/signup
- **Docker** - Package everything to run anywhere
- **GitHub Actions** - Auto-deploy when you push code

## 📁 Project Structure (Simple View)

```
ai_compliance_app/
│
├── src/compliance_ai/        # Backend code
│   ├── main.py              # Start here! Main app file
│   ├── api/routes/          # API endpoints (chatbot, compliance)
│   └── services/            # AI logic (chatbot, document analysis)
│
├── frontend/                 # React website
│   └── src/
│       └── components/      # UI components (Chatbot, Dashboard)
│
├── data/                    # Your documents go here
│   ├── offers/
│   └── regulations/
│
├── tests/                   # Test your code
├── .env                     # Secret keys (don't share!)
└── README.md
```

## 🚀 How to Start (Step by Step)

### Step 1: Install UV (Package Manager)

**Mac/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Step 2: Setup Backend

```bash
# Go to project folder
cd ai_compliance_app

# Create virtual environment
uv venv

# Activate it
source .venv/bin/activate     # Mac/Linux
.venv\Scripts\activate        # Windows

# Install everything
uv pip install -e .
```

### Step 3: Create .env file

Create a file called `.env` and add:

```env
# Basic settings
DEBUG=true
API_PORT=8000

# AI Model (free and small)
HF_MODEL_NAME=sentence-transformers/all-MiniLM-L6-v2

# Firebase (get from Firebase Console)
FIREBASE_PROJECT_ID=your-project-id
```

### Step 4: Run the Backend

```bash
uvicorn compliance_ai.main:app --reload
```

✅ Open http://localhost:8000 - You should see "Hello World" or API docs!

### Step 5: Setup Frontend

```bash
# Go to frontend folder
cd frontend

# Install packages
npm install

# Start website
npm run dev
```

✅ Open http://localhost:5173 - Your React app is running!

## 📝 Basic Files You Need

### 1. `pyproject.toml` (Python Dependencies)

```toml
[project]
name = "compliance-ai"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "fastapi",
    "uvicorn",
    "transformers",
    "sentence-transformers",
]
```

### 2. `main.py` (Backend Entry Point)

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Compliance API is running!"}

@app.post("/api/chat")
def chat(message: str):
    # Your chatbot logic here
    return {"response": f"You said: {message}"}
```

### 3. `App.jsx` (Frontend Entry Point)

```jsx
function App() {
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">AI Compliance Chatbot</h1>
      <p>Ask me about regulations!</p>
    </div>
  )
}
```

## 🧪 How to Test

```bash
# Run tests
pytest

# Check code quality
black .          # Format code
ruff check .     # Find errors
```

## 🎯 Main Features (What It Does)

### 1. Chatbot 💬
User asks: "What is regulation X?"
Bot answers using AI

### 2. Compliance Check ✅
Upload document → Compare with rules → Get report

### 3. Dashboard 📊
See statistics and reports

## 🔧 Common Commands

```bash
# Start backend
uvicorn compliance_ai.main:app --reload

# Start frontend
cd frontend && npm run dev

# Install new package (backend)
uv pip install package-name

# Install new package (frontend)
npm install package-name
```

## ❗ Troubleshooting

**Problem:** `uv: command not found`
- **Solution:** Install UV again (Step 1)

**Problem:** Port 8000 already in use
- **Solution:** Kill the process or use different port: `--port 8001`

**Problem:** Module not found
- **Solution:** Make sure virtual environment is activated

## 📚 Learn More

### For Backend:
- FastAPI: https://fastapi.tiangolo.com/
- UV: https://docs.astral.sh/uv/

### For Frontend:
- React: https://react.dev/
- Tailwind: https://tailwindcss.com/

### For AI:
- Hugging Face: https://huggingface.co/docs

## 🎓 Next Steps (After You're Comfortable)

1. Add authentication (Firebase)
2. Connect to database (save chat history)
3. Deploy online (Docker + Cloud)
4. Add monitoring (see errors)

## 💡 Tips for Beginners

- **Start small**: Get chatbot working first, then add features
- **Test everything**: Run your code after each change
- **Read errors**: Error messages tell you what's wrong
- **Use Google**: Everyone searches for help, it's normal!
- **Ask for help**: Share error messages when you're stuck

## 📞 Need Help?

- Check this file first
- Read error messages carefully
- Google the error
- Ask your team or mentor

---

**Remember**: Everyone starts as a beginner! Take it one step at a time. 🚀

**Start here**: Get the backend running (Step 2-4), then worry about the rest!