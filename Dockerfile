FROM python:3.9

RUN python -m pip install --upgrade pip && python -m pip install aiogram==2.23.1

COPY . .

CMD ["python", "main.py"]
