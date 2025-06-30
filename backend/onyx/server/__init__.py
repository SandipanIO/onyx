from fastapi import FastAPI, Request
from onyx_ingest import answer_with_gemini, get_hint_from_docs  # Make sure these functions exist

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Onyx AI is running 🎉"}

@app.get("/ask")
async def ask_cody(question: str):
    answer = await answer_with_gemini(question)  # Gemini-powered response
    return {"answer": answer}

@app.get("/hint")
async def get_hint(topic: str):
    hint = await get_hint_from_docs(topic)  # Doc-based hint generation
    return {"hint": hint}

@app.post("/submit-project")
async def submit_project(data: dict):
    return {"status": "received", "message": "Project submitted successfully 🚀"}
