from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Onyx AI is running 🎉"}

@app.get("/ask")
def ask_cody(question: str):
    return {"answer": f"You asked: '{question}'. Cody says: Keep going, you're doing great!"}

@app.get("/hint")
def get_hint(topic: str):
    return {"hint": f"Here's a hint about {topic}: Think of it like solving a puzzle 🧩"}

@app.post("/submit-project")
def submit_project(data: dict):
    return {"status": "received", "message": "Project submitted successfully 🚀"}
