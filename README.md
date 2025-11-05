# "Inquote" API

An AI-powered API that generates **intellectual quotes, principles, effects, and phenomena** across various scientific and philosophical fields.  
Built with **FastAPI** and powered by **Groq**.

---

## 🚀 Features

- Fetch random insightful quotes or theories  
- Filter by **field** (e.g., *psychology*, *physics*, *chemistry*, *mathematics*, *philosophy*)  
- Filter by **type** (e.g., *effect*, *principle*, *theory*, *phenomenon*, *quote*)  
- Search for specific keywords  
- Lists supported fields and types  
- JSON-only API — perfect for integration with web or mobile apps  

---

## ⚙️Local Setup

```bash
git clone https://github.com/ghasty1/Inquote.git
cd Inquote
pip install -r requirements.txt
uvicorn main:app --reload
```

Then visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive API documentation.

---
## Live API
Visit [Inquote Online](https://inquote.onrender.com/)
## 🧾 Endpoints

### 🔹 `GET /random`
Get a random inspirational quote.

**Example Request:**
```bash
GET /random
```

**Example Response:**
```json
{
  "name": "The Barnum Effect",
  "field": "psychology",
  "type": "effect",
  "quote": "People tend to believe vague, general statements about themselves are uniquely true.",
  "summary": "Explains why horoscopes and personality tests feel so personal."
}
```

---

### 🔹 `GET /random/{type}/{field}`
Get a random quote filtered by **type** and **field**.

**Example Request:**
```bash
GET /random/effect/psychology
```

**Example Response:**
```json
{
  "name": "The Halo Effect",
  "field": "psychology",
  "type": "effect",
  "quote": "Our impression of one positive trait influences how we see all others.",
  "summary": "Attractive or charismatic people are often assumed to be more capable or kind, regardless of evidence."
}
```

**Errors:**
- `400 Bad Request` → Invalid field or type

---

### 🔹 `GET /quote/{field}`
Get a random quote filtered by **field** only.

**Example Request:**
```bash
GET /quote/physics
```

**Example Response:**
```json
{
  "name": "The Butterfly Effect",
  "field": "physics",
  "type": "phenomenon",
  "quote": "Small causes can have large, unpredictable consequences.",
  "summary": "A principle from chaos theory that shows how tiny changes can lead to massive outcomes."
}
```

**Errors:**
- `400 Bad Request` → Field Not Supported

---

### 🔹 `GET /fields`
Retrieve a list of supported academic fields.

**Example Response:**
```json
{
  "fields": ["psychology", "physics", "chemistry", "mathematics", "philosophy"]
}
```

---

### 🔹 `GET /types`
Retrieve a list of supported concept types.

**Example Response:**
```json
{
  "types": ["effect", "principle", "theory", "phenomenon", "quote"]
}
```

---

### 🔹 `GET /search/{keyword}`
Search for a quote by keyword.  
The API returns a concept or quote relevant to the search term.

**Example Request:**
```bash
GET /search/memory
```

**Example Response:**
```json
{
  "name": "The Mandela Effect",
  "field": "psychology",
  "type": "phenomenon",
  "quote": "Collective false memories occur when many people recall events differently from how they actually happened.",
  "summary": "Shows how human memory can be influenced by suggestion and social reinforcement."
}
```

---

## 🧩 Supported Fields
| Field | Description |
|--------|-------------|
| psychology | Human mind and behavior |
| physics | Laws of nature and energy |
| chemistry | Reactions and molecular structures |
| mathematics | Patterns, logic, and equations |
| philosophy | Human thought and reasoning |

---

## 🧩 Supported Types
| Type | Description |
|--------|-------------|
| effect | Observable behavioral or physical outcome |
| principle | Foundational rule or guiding law |
| theory | Conceptual explanation based on reasoning |
| phenomenon | Naturally occurring event or pattern |
| quote | Memorable intellectual statement |

---

## ⚠️ Error Responses

| Status | Meaning | Cause |
|--------|----------|--------|
| 400 | Bad Request | Unsupported field or type |
| 500 | Server Error | Internal Groq API or parsing issue |

---

## 💡 Example Use Case
Integrate this API into:
- Educational apps for daily scientific facts  
- AI writing assistants to generate smart insights  
- Chatbots for thought-provoking responses  
- Websites showing random “Did you know?” facts  

---

## 🧠 Tagline
> “Because sounding smart should be effortless.”

---

## 🧾 License
MIT License © 2025 Your Name / Smart Concepts API
