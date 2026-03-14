import random
from openai import OpenAI

MODEL_NAME = "openai/gpt-4o-mini"

stoic_themes = [
    "Focus on a piercing truth about self-mastery and the cost of awareness.",
    "Reflect deeply on memento mori and the shortness of life.",
    "Explore equanimity — how to remain undisturbed by externals.",
    "Delve into amor fati and loving what fate brings.",
    "Examine perception: how our judgments create suffering.",
    "Reflect on character being revealed (not made) by adversity.",
    "Contemplate indifference to opinion, fame, or approval.",
    "Explore the difference between pain and the suffering we choose.",
    "Focus on virtue as the only true good in a chaotic world.",
    "Reflect on time, death, and living without regret.",
    "Examine power, control, and what we can truly influence.",
    "Contemplate relationships and becoming the right person.",
]


def generate_quote(template: str) -> str:
    theme = random.choice(stoic_themes)
    prompt = f"{theme}\n\n{template}"

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=ECHO_CANVAS_OPEN_ROUTER_API_KEY,
    )
    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>",
            "X-Title": "<YOUR_SITE_NAME>",
        },
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
    )
    return completion.choices[0].message.content
