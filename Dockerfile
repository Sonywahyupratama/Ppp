FROM ubuntu:latest

# Memperbarui paket dan menginstal "xh", Python, dan screen
RUN apt-get update && \
    apt-get install -y python-pip screen
ENV PYTHONUNBUFFERED=1

WORKDIR /app
RUN chmod 777 /app

# Menyalin file "p.py" dan "bash.sh" ke dalam container
COPY p.py .
COPY bash.sh .
RUN chmod +x /app/bash.sh

RUN pip install aiohttp 
RUN pip install faker
RUN pip install requests


# Menjalankan skrip Python saat container berjalan (opsional)
CMD ["bash", "bash.sh"]
