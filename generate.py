from openai import AsyncOpenAI
import requests

token = "sk-0ac1badfc7804bdf9111fc33937d6b53"

client = AsyncOpenAI(api_key=token,
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


async def ai_get_balanc():
    url = "https://api.deepseek.com/user/balance"

    payload = {}
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    balance = response.json()["balance_infos"][0].get("total_balance")

    return balance
