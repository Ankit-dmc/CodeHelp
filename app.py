import json
import os
from flask import Flask, render_template, request
from groq import Groq  # Official Groq Python SDK -> pip install groq

app = Flask(__name__)

# ---------------------------------------------------------------------------
# GROQ API SETUP (read this first)
# ---------------------------------------------------------------------------
# 1. Get a free API key (no credit card needed): https://console.groq.com/keys
# 2. Set it as an environment variable BEFORE running this app:
#       Mac/Linux:  export GROQ_API_KEY="gsk_xxxxxxxxxxxxxxxxxxxx"
#       Windows:    setx GROQ_API_KEY "gsk_xxxxxxxxxxxxxxxxxxxx"
# 3. The Groq() client below automatically picks up GROQ_API_KEY from the
#    environment, so you don't have to paste your key into the code.
# ---------------------------------------------------------------------------
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Free, fast model hosted by Groq. You can swap this for another model
# from https://console.groq.com/docs/models (e.g. "llama-3.1-8b-instant"
# for even faster/cheaper responses).
GROQ_MODEL = "llama-3.3-70b-versatile"

    # -----------------------------------------------------------------
    # >>> THE ACTUAL API CALL <<<
    # This is the only place this app talks to the internet.
    # - "system" message  = instructions that steer the model's behavior
    # - "user" message    = the real input (the code to explain)
    # The request goes to Groq's servers, the model runs there, and we
    # get the finished text back in `response`.
    # -----------------------------------------------------------------

def analyze_code(code: str):
    if not code or not code.strip():
        return None
    prompt= f"""
    You are and expert software engineer and coding interviewer.
    Analyse the following code
    IMPORTANT:
    - Keep the explanation simple and beginner friendly.
    - Assume the user is learning programming.
    - Explain concepts in simple terms.
    - Be accurate and do not guess.

    Return ONLY valid JSON in exactly this format:

    {{
    "explanation": "",
    "time_complexity": {{
        "complexity": "",
        "reason": ""
    }},
    "space_complexity": {{
        "complexity": "",
        "reason": ""
    }},
    "bugs": [],
    "optimizations": [],
    "concepts_used": [],
    "difficulty": ""
    }}

    Rules:
    - difficulty must be one of:
    Easy, Medium, Hard.

    - If there are no bugs:
    ["No obvious bugs found."]

    - If there are no optimizations:
    ["No significant optimizations needed."]

    Code:

    {code}
    """
    try:
        response=client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ],
            temperature=0.2,
            max_tokens=1200,
        )
        content=response.choices[0].message.content
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()
        return json.loads(content)
    except json.JSONDecodeError:
        return {
            "error":"the ai returned invalid json"
        }
    except Exception as e:
        return{
            "error":str(e)
        }
    
@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    code = ""

    if request.method == "POST":
        code = request.form.get("code", "")
        result = analyze_code(code)  # <-- triggers the Groq API call above

    return render_template("index.html", result=result, code=code)


if __name__ == "__main__":
    app.run(debug=True)