from fastapi import FastAPI, Query
from onyx_ingest import get_answer_from_docs, get_hint_from_docs  # Make sure these exist

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Onyx AI is running 🎉"}

@app.get("/ask")
def ask_cody(question: str = Query(..., description="Your HTML/CSS-related question")):
    answer = get_answer_from_docs(question)
    return {"answer": answer}

@app.get("/hint")
def get_hint(topic: str = Query(..., description="Topic to get a hint about")):
    hint = get_hint_from_docs(topic)
    return {"hint": hint}
