from openai import AsyncOpenAI


client = AsyncOpenAI(api_key="sk-0ac1badfc7804bdf9111fc33937d6b53",
                     base_url="https://api.deepseek.com")


async def ai_generate(text: str):
    completion = await client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": text},
        ],
        stream=False
    )

    print(completion)
    return completion.choices[0].message.content
