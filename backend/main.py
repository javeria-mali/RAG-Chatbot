from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .auth import register_user, login_user

import os
import shutil

from utils.document_loader import extract_text
from utils.text_splitter import split_text


app = FastAPI()


# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------- Models ----------------

class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


class ChatRequest(BaseModel):
    question: str


# ---------------- Home ----------------

@app.get("/")
def home():
    return {
        "message": "RAG Chatbot API is running!"
    }


# ---------------- Register ----------------

@app.post("/register")
def register(request: RegisterRequest):

    success, message = register_user(
        request.name,
        request.email,
        request.password
    )

    return {
        "success": success,
        "message": message
    }


# ---------------- Login ----------------

@app.post("/login")
def login(request: LoginRequest):

    success, message = login_user(
        request.email,
        request.password
    )

    return {
        "success": success,
        "message": message
    }


# ---------------- Upload Document ----------------

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    os.makedirs("documents", exist_ok=True)

    file_path = os.path.join("documents", file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "success": True,
        "message": f"{file.filename} uploaded successfully!"
    }


# ---------------- Chat / RAG ----------------

@app.post("/chat")
def chat(request: ChatRequest):

    question = request.question.lower().strip()

    if not os.path.exists("documents"):
        return {
            "success": False,
            "answer": "No documents found. Please upload a PDF or TXT document first."
        }

    all_chunks = []

    for filename in os.listdir("documents"):

        file_path = os.path.join("documents", filename)

        try:
            text = extract_text(file_path)

            chunks = split_text(text)

            all_chunks.extend(chunks)

        except Exception:
            continue

    if not all_chunks:
        return {
            "success": False,
            "answer": "I couldn't read any text from the uploaded documents."
        }

    # Simple keyword-based retrieval
    question_words = set(question.split())

    scored_chunks = []

    for chunk in all_chunks:

        chunk_lower = chunk.lower()
        score = 0

        for word in question_words:
            if len(word) > 2 and word in chunk_lower:
                score += 1

        scored_chunks.append((score, chunk))

    scored_chunks.sort(
        key=lambda x: x[0],
        reverse=True
    )

    best_chunks = [
        chunk for score, chunk in scored_chunks[:3]
        if score > 0
    ]

    if not best_chunks:
        return {
            "success": True,
            "answer": "Sorry, I couldn't find relevant information in your uploaded documents."
        }

    answer = "\n\n".join(best_chunks)

    return {
        "success": True,
        "answer": answer
    }