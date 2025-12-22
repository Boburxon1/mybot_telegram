# Python rasm
FROM python:3.11-slim

# Ishchi papka
WORKDIR /app

# Kerakli fayllarni ko‘chirish
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Barcha kodni ko‘chirish
COPY . .

# Botni ishga tushirish
CMD ["python", "bot.py"]