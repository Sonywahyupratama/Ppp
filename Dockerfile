# Gunakan gambar Python sebagai dasar
FROM python:3.x

# Memperbarui paket dan instal paket yang diperlukan
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

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
RUN pip install -r requirements.txt

# Menjalankan skrip Python saat container berjalan (opsional)
CMD ["bash", "bash.sh"]
