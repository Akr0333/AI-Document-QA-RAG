from openai import OpenAI

SYSTEM_PROMPT = "Answer only from the supplied context. If the answer is not in context, say you do not have enough information."

def build_context(results):
    return "\n\n".join(f"[Source {i}: {item['source']}]\n{item['text']}" for i, item in enumerate(results, 1))

def answer_question(question, results, api_key, model="gpt-4o-mini"):
    if not results:
        return "No relevant information was retrieved."
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        temperature=0.1,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Context:\n{build_context(results)}\n\nQuestion: {question}"},
        ],
    )
    return response.choices[0].message.content
