from pipeline import retrieve, store
import openai

def agent(prompt):
    context = retrieve(prompt)
    final_prompt = "Context:\n" + "\n".join(context) + "\nUser:" + prompt

    reply = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":final_prompt}]
    )
    store(prompt)
    store(reply["choices"][0]["message"]["content"])
    return reply["choices"][0]["message"]["content"]
