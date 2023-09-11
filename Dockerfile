# Gunakan gambar Ubuntu sebagai dasar
FROM ubuntu:latest

# Memperbarui paket dan instal paket yang diperlukan
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1

# Membuat direktori kerja
WORKDIR /app

# Menyalin file "p.py" dan "bash.sh" ke dalam container
COPY p.py .
COPY bash.sh .

# Memberikan izin yang sesuai pada file bash.sh
RUN chmod +x /app/bash.sh

# Install dependensi Python
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Menjalankan skrip Python saat container berjalan (opsional)
CMD ["bash", "bash.sh"]
