from groq import Groq
import json
from pydantic import BaseModel, Field
from enum import Enum
import os
from dotenv import load_dotenv


load_dotenv()

def generate_quote(field: str, type: str, char: int= None) -> dict:
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    class SupportedField(str, Enum):
        psychology = "psychology"
        physics = "physics"
        chemistry = "chemistry"
        mathematics = "mathematics"
        philosophy = "philosophy"
        inspirational = "inspirational"


    class SupportedType(str, Enum):
        effect = "effect"
        principle = "principle"
        theory = "theory"
        phenomenon = "phenomenon"
        quote = "quote"
        syndrome = "syndrome"

    class QuoteResponse(BaseModel):
        name: str = Field(..., description="The name of the concept, law, or theory.")
        field: SupportedField = Field(..., description="The academic domain (must be one of the supported fields).")
        type: SupportedType = Field(..., description="The classification: effect, principle, theory, phenomenon, or quote.")
        quote: str = Field(..., description="The actual quote, statement, or law text.")
        summary: str = Field(..., description="A short summary or explanation.")
        author: str | None = Field(None, description="The person who proposed or inspired it.")
        time: str | None = Field(None, description="Year or era when it was introduced.")

    system_prompt = """You are an intelligent academic curator who specializes in collecting short, fascinating, and thought-provoking concepts from diverse fields — psychology, physics, chemistry, and mathematics.

                    Your task is to produce a profound, precise, real, or academically recognized entries such as laws, effects, phenomena, principles, theories, or memorable quotes that sound insightful, profound, or surprisingly true.

                    Each entry must be random and include the **actual name and quote or statement itself**, followed by a clear, intellectual **summary** explaining its meaning or application.If you receive a random word search, you should return a quote related to that word.

                    Return your response strictly in **valid JSON format** using this schema:

                    {
                      "name": "<the name of the concept, law, theory, or effect>",
                      "field": "<psychology | physics | chemistry | mathematics| Philosophy>",
                      "type": "<effect | principle | theory | phenomenon | quote>",
                      "quote": "<the actual phrase, law, or saying itself>",
                      "author": "<the original author or source of the quote or concept, if known; otherwise use 'Unknown'>",
                      "time": "<the year or period when the concept was first introduced or the quote was made>",
                      "summary": "<1–3 sentences explaining what the statement means, why it’s interesting, or how it applies to human behavior or real life.>"
                    }

                    Guidelines:
                    - The quote must be **authentic** or a commonly accepted phrasing of the concept (e.g. “The Butterfly Effect”, “Occam’s Razor”, “The Dunning–Kruger Effect”).
                    - The summary should read like an intelligent, well-crafted encyclopedia note — concise but insightful.
                    - Focus on entries that either reveal hidden truths, describe human behavior, or express principles of science, logic, or art.
                    - No reasoning steps or commentary outside the JSON. The output must be valid JSON only.
    """
    response = client.chat.completions.create(
        temperature=0.9,
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {"role": "user",
             "content": f"Provide a quote in {field} area of type {type} with {char} characters. If {char} is None, provide a random length."
             },
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "QuoteResponse",
                "schema": QuoteResponse.model_json_schema(),
            }
        }

    )

    response_generation = QuoteResponse.model_validate(json.loads(response.choices[0].message.content))
    parsed_response = response_generation.model_dump()

    return parsed_response



