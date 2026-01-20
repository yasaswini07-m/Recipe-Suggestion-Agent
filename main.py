Python# main.py: FastAPI backend for the app.
# Handles serving the frontend and the /suggest API endpoint.

from fastapi import FastAPI, Form, Request  # FastAPI core for app, form handling, and requests.
from fastapi.responses import HTMLResponse, JSONResponse  # Response types for HTML and JSON.
from fastapi.staticfiles import StaticFiles  # For serving static files (e.g., CSS/JS if added).
from fastapi.templating import Jinja2Templates  # Jinja for rendering HTML templates.
from agent import run_agent  # Import the agent function from agent.py.
import os  # For potential env vars (though not used here directly).

# Initialize FastAPI app.
app = FastAPI()

# Mount static files directory (optional; create 'static' folder for CSS/JS).
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja templates from 'templates' directory.
templates = Jinja2Templates(directory="templates")

# Root endpoint: Serves the index.html frontend.
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})  # Render index.html with request context.

# Suggest endpoint: Handles POST form data, runs agent, returns JSON.
@app.post("/suggest")
async def suggest_recipe(ingredients: str = Form(...), preferences: str = Form(default="")):  # Form fields: ingredients required, preferences optional.
    prompt = f"Ingredients: {ingredients}. Preferences: {preferences}."  # Construct prompt for agent.
    try:
        result = await run_agent(prompt)  # Run the agent asynchronously.
        return JSONResponse(content=result.dict())  # Convert Pydantic model to dict and return as JSON.
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)  # Return error JSON on failure
