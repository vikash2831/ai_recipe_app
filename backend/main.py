from fastapi import FastAPI
from pydantic import BaseModel
import os
import groq
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load API key from .env inside backend folder
load_dotenv(dotenv_path="./backend/.env")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY is missing. Please check your environment variables.")

client = groq.Client(api_key=GROQ_API_KEY)

app = FastAPI()

# Enable CORS (allow frontend to call backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Fix "404 Not Found" error
@app.get("/")
def read_root():
    return {"message": "✅ AI Recipe Generator API is running!"}

class RecipeRequest(BaseModel):
    ingredients: list

@app.post("/generate_recipe/")
def generate_recipe(request: RecipeRequest):
    prompt = f"Create a unique recipe using these ingredients: {', '.join(request.ingredients)}. Include a title, ingredient list, and step-by-step instructions."

    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[{"role": "user", "content": prompt}]
    )

    return {"recipe": response.choices[0].message.content}
