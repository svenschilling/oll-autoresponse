import asyncio
from ollama import AsyncClient

async def chat():
    client = AsyncClient(base_url='http://localhost:11434')
    response = await client.chat(model='qwen2.5-coder:32b', messages=[
        {
            "role": "user", 
            "content": "is the sky blue?"
        },
        stream=True
    ]):
    print(response.message.content)

asyncio.run(chat())
