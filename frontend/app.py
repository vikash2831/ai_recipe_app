import streamlit as st
import requests
import base64

# Function to load and encode background image
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Load the background image
bg_image = get_base64_image("food-background.jpg")  # Use your actual image file name

# Custom CSS for Full-Screen Background, Bold Fonts, and UI Styling
st.markdown(f"""
    <style>
    /* Full-screen background */
    .stApp {{
        background: url("data:image/jpeg;base64,{bg_image}") no-repeat center center fixed;
        background-size: cover;
    }}



    /* Title */
    .title {{
        font-size: 42px;
        font-weight: bold;
        color: #FF4500;
        font-family: 'Arial', sans-serif;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3);
    }}

    /* Subtitle */
    .subtitle {{
        font-size: 20px;
        font-weight: bold;
        color: white;
        font-family: 'Arial', sans-serif;
        margin-bottom: 20px;
    }}

    /* Input Label */
    .input-label {{
        font-size: 22px;
        font-weight: bold;
        color: white;
        font-family: 'Arial', sans-serif;
        margin-bottom: 10px;
    }}


    /* Generate Button */
    .stButton>button {{
        background-color: #333333;
        color: white;
        font-size: 20px;
        font-weight: bold;
        padding: 12px 28px;
        border-radius: 12px;
        border: none;
        cursor: pointer;
        transition: 0.3s;
        box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.2);
    }}
    .stButton>button:hover {{
        background-color: white;
        transform: scale(1.05);
        color:black;
    }}


    /* Recipe Title */
    .recipe-title {{
        font-size:40px;
        font-weight: bold;
        color: white;
        text-align: center;
        margin-bottom: 15px;
    }}

    /* Recipe Text */
    .recipe-text {{
     background-color:#333333;
        padding: 10px;
        border-radius: 12px;
        border: 5px solid white;
        box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2);
        font-size: 60px;
        font-weight: bold;
        color: white;
        line-height: 1.6;
        margin-top: 20px;
        margin-left: 20px; 
    }}
    .stTextArea textarea {{
        font-size: 16px;
        padding: 10px;
        border-radius: 8px;
        border: 5px solid white;
        background-color:#333333;
    }}

    
    </style>
""", unsafe_allow_html=True)

# Wrapper for centered content
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Title
st.markdown('<h1 class="title">🧑‍🍳 CHEF BOT </h1>', unsafe_allow_html=True)
st.markdown('<h4 class="subtitle">List your ingredients and discover a personalized recipe just for you!✨</h4>', unsafe_allow_html=True)

# User Input
st.markdown('<h2 class="input-label">📝 Enter ingredients </h2>', unsafe_allow_html=True)
ingredients = st.text_area("",placeholder= "Eg :Chicken,Rice,Egg")


# Generate Button
if st.button("SEARCH🔍"):
    response = requests.post("https://ai-recipe-app-1.onrender.com/generate_recipe/", json={"ingredients": ingredients.split(",")})
    
    if response.status_code == 200:
        recipe_text = response.json()["recipe"]
        st.markdown("<hr style='border: 0; height: 2px; background-color: white; margin-top: 20px; margin-bottom: 20px;'>", unsafe_allow_html=True)
        st.markdown('<h2 class="recipe-title">✨Here is your recipe:</h2>', unsafe_allow_html=True)
        st.markdown(f'<h5 class="recipe-text">{recipe_text}</h5>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("❌ Error generating recipe. Please try again.")

# Close the wrapper div
st.markdown('</div>', unsafe_allow_html=True)

