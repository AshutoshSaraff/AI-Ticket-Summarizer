import google.generativeai as genai

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv(
    "GOOGLE_API_KEY"
)

class AIClient:

    def __init__(self):

        genai.configure(
            api_key=API_KEY
        )

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def generate_summary(self, ticket): #generate AI Output
        prompt = prompt = f"""
Analyze the support ticket below.

Return ONLY valid JSON.

{{
    "summary": "",
    "priority": "",
    "category": "",
    "platform": "",
    "next_steps" :[]
}}

Ticket:
{ticket}
"""

        try:

            response = self.model.generate_content(
                prompt
            )
            import json
            
            clean_text = response.text.replace(
                "```json",
                ""
            ).replace(
                "```",
                ""
            ).strip()

            data = json.loads(clean_text)

            print(type(data))
            print(data)
            return data
        
        except Exception as error:

            print(
                f"AI Error: {error}"
            )

            return None