from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Compliance API is running!"}

@app.post("/api/chat")
def chat(message: str):
    # Your chatbot logic here
    return {"response": f"You said: {message}"}
