from fastapi import FastAPI
from pydantic import BaseModel
import os
import groq
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = groq.Client(api_key=GROQ_API_KEY)

app = FastAPI()

# Enable CORS (allow frontend to call backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

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
