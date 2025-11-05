import uvicorn
from fastapi import FastAPI
from random import choice
from ai import generate_quote
from fastapi.responses import JSONResponse, RedirectResponse

random_type = choice(["effect", "principle", "theory", "phenomenon", "quote"])
random_field = choice(["psychology", "physics", "chemistry", "mathematics", "philosophy", "inspirational"])
app = FastAPI( title="Smart Concepts API",
    description="""
    An AI-powered API that generates fascinating quotes, effects, and principles from various fields of study.

    Features:
    - AI-driven concept generation via Groq
    - Structured JSON responses  
    - Auto-generated Swagger UI and ReDoc documentation  
    """,
    version="1.0.1")


@app.get("/")
def root():
    """Smart Concepts API Documentation."""
    return RedirectResponse(url="/docs")

@app.get("/random")
def random():
    """Get a random inspirational quote."""
    message = generate_quote("inspirational", random_type)
    return JSONResponse(content=message)

@app.get("/random/{type}/{field}")
def random_type_field(type: str, field: str):
    """Get a random quote by type and field."""
    if field not in ["psychology", "physics", "chemistry", "mathematics", "philosophy"]:
        return JSONResponse(content={"error": "Field Not Supported"}, status_code=400)
    elif type not in ["effect", "principle", "theory", "phenomenon", "quote"]:
        return JSONResponse(content={"error": "Type Not Supported"}, status_code=400)
    else:
        message = generate_quote(field, type)
        return JSONResponse(content=message)

@app.get("/quote/{field}")
def get_quote(field: str):
    """Get a random quote by field."""
    if field not in ["psychology", "physics", "chemistry", "mathematics", "philosophy", "inspirational"]:
        return JSONResponse(content={"error": "Field Not Supported"}, status_code=400)
    else:
        message = generate_quote(field, random_type)
        return JSONResponse(content=message)

@app.get("/fields")
def get_fields():
    """Get supported fields."""
    fields = ["psychology", "physics", "chemistry", "mathematics", "philosophy", "inspirational"]
    return JSONResponse(content={"fields": fields})

@app.get("/types")
def get_types():
    """Get supported types."""
    types = ["effect", "principle", "theory", "phenomenon", "quote"]
    return JSONResponse(content={"types": types})

@app.get("/search/{keyword}")
def search_quote(keyword: str):
    """Search for a quote by keyword."""
    message = generate_quote(keyword, random_type)
    return JSONResponse(content=message)
@app.get("/health")
def health_check():
    """Health check endpoint."""
    return JSONResponse(content={"status": "ok"})

@app.get("/short-quote")
def short_quote(max_char: int = 40):
    """Get a short inspirational quote."""
    message = generate_quote("inspirational", random_type, max_char=max_char)
    return JSONResponse(content=message)



if __name__ == "__main__":
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
