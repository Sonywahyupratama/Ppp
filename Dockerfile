FROM alpine:latest
 
# Memperbarui paket dan menginstal "xh"
RUN apk update && \
    apk add xh

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

# Menyalin file "p.py" ke dalam container
COPY p.py /app/p.py

# Mengatur direktori kerja
WORKDIR /app

RUN pip3 install aiohttp 
RUN pip3 install faker
RUN pip3 install requests


# Menjalankan skrip Python saat container berjalan (opsional)
CMD ["python", "p.py"]
