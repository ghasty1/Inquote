import uvicorn
from fastapi import FastAPI
from random import choice
from ai import generate_quote
from fastapi.responses import JSONResponse, RedirectResponse

fields = ["psychology", "physics", "chemistry", "mathematics", "philosophy", "inspirational"]
types = ["effect", "principle", "theory", "phenomenon", "quote", "syndrome"]
random_type = choice(types)
random_field = choice(fields)
app = FastAPI( title="Smart Concepts API",
    description="""
    An AI-powered API that generates fascinating quotes, effects, and principles from various fields of study.

    Features:
    - AI-driven concept generation via Groq
    - Structured JSON responses  
    - Auto-generated Swagger UI and ReDoc documentation  
    """,
    version="1.0.2")


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
    if field not in fields:
        return JSONResponse(content={"error": "Field Not Supported"}, status_code=400)
    elif type not in types:
        return JSONResponse(content={"error": "Type Not Supported"}, status_code=400)
    else:
        message = generate_quote(field, type)
        return JSONResponse(content=message)

@app.get("/quote/{field}")
def get_quote_field(field: str):
    """Get a random quote by field."""
    if field not in fields:
        return JSONResponse(content={"error": "Field Not Supported"}, status_code=400)
    else:
        message = generate_quote(field, random_type)
        return JSONResponse(content=message)


@app.get("/quote/{type}")
def get_quote_type(type: str):
    """Get a random quote by type."""
    if type not in types:
        return JSONResponse(content={"error": "Type Not Supported"}, status_code=400)
    else:
        message = generate_quote(random_field, type)
        return JSONResponse(content=message)

@app.get("/fields")
def get_fields():
    """Get supported fields."""
    return JSONResponse(content={"fields": fields})

@app.get("/types")
def get_types():
    """Get supported types."""
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
def short_quote(char: int = 53):
    """Get a short inspirational quote."""
    message = generate_quote("inspirational", random_type, char=char)
    return JSONResponse(content=message)



if __name__ == "__main__":
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


