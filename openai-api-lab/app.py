from google import gemini
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Create Gemini client
client = gemini(
    api_key=os.getenv("gemini_api_key")
)

# Send request to the model
response = client.responses.create(
    model="gemini-1.5-turbo",
    input="Explain artificial intelligence in simple terms."
)

# Display the response
print(response.output_text)