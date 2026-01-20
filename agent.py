Python# agent.py: Defines the AI agent using Langchain for generating structured recipe suggestions.
# It uses a Pydantic model for output structure and OpenRouter's free LLM via Langchain.

from pydantic import BaseModel, Field  # Pydantic for defining structured output schemas.
from langchain_openai import ChatOpenAI  # Langchain wrapper for OpenAI-compatible APIs (like OpenRouter).
from langchain_core.prompts import ChatPromptTemplate  # For creating prompt templates.
from langchain_core.output_parsers import PydanticOutputParser  # Parser to enforce Pydantic structure on LLM output.
import os  # For accessing environment variables like API keys.

# Define the structured output model for the recipe.
class RecipeOutput(BaseModel):
    recipe_name: str = Field(description="Name of the suggested recipe")  # Recipe title.
    required_ingredients: list[str] = Field(description="List of ingredients needed")  # Ingredients required.
    instructions: list[str] = Field(description="Step-by-step cooking instructions")  # Cooking steps.
    prep_time: str = Field(description="Estimated preparation time")  # Time estimate, e.g., "20 minutes".
    dietary_notes: str = Field(description="Notes on dietary suitability based on preferences")  # Notes like "Vegan-friendly".

# Initialize the LLM using OpenRouter's API.
# Replace the model if needed; this is a free one.
llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",  # OpenRouter base URL.
    api_key=os.environ['OPENROUTER_API_KEY'],  # API key from environment (set in Colab or Vercel).
    model="meta-llama/llama-3.1-8b-instruct:free"  # Free model; can swap to others from OpenRouter.
)

# Parser to convert LLM output to the Pydantic model.
parser = PydanticOutputParser(pydantic_object=RecipeOutput)

# Prompt template: System message for agent behavior, with placeholder for user input.
prompt = ChatPromptTemplate.from_messages([
    ("system", 
     "You are a helpful recipe suggestion agent. "  # Core instructions for the AI.
     "Based on the user's available ingredients and preferences (e.g., vegan, quick), "
     "suggest a simple, creative recipe. Keep it realistic and tasty. "
     "If preferences are not provided, assume general healthy options. "
     "Format your response as JSON matching this structure: {format_instructions}"),  # Enforce JSON output.
    ("human", "{input}")  # User-provided prompt (ingredients + preferences).
])

# Chain: Prompt -> LLM -> Parser (combines them into a runnable chain).
chain = prompt | llm | parser

# Async function to run the agent.
async def run_agent(input_text: str):
    try:
        # Invoke the chain with input and format instructions for Pydantic.
        result = await chain.ainvoke({"input": input_text, "format_instructions": parser.get_format_instructions()})
        return result  # Returns the parsed RecipeOutput object.
    except Exception as e:
        print(f"Agent error: {str(e)}")  # Log errors for debugging (visible in Colab or server logs).
        raise  # Re-raise for API to handle
