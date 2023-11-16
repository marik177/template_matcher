import aiohttp
import asyncio


async def make_async_request(url, data, headers):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data, headers=headers) as response:
            print(f"Status Code: {response.status}")
            print("Response Content:")
            print(await response.text())


async def main(url, headers, list_data):
    tasks = [make_async_request(url, data, headers) for data in list_data]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    url = 'http://127.0.0.1:5000/get-form'
    headers = {'Content-Type': 'application/json'}

    list_data = [
        {
            "my_email": "123@ya.ru",
            "my_phone": "+71234567890",
            "my_date": "16.11.2023",
            "text": "qwerty"
        },
        {
            "my_email": "123@ya.ru",
            "my_phone": "+71234567890",
            "my_date": "16.11.2023",
            "bad_field": "test data",
        },
        {
            "no_email": "123@ya.ru",
            "no_phone": "+71234567890",
            "no_date": "16.11.2023",
        },
        {
            "order_email": "123@ya.ru",
            "order_phone": "+71234567890",
            "order_date": "16.11.2023",
        },
    ]

    asyncio.run(main(url, headers, list_data))
