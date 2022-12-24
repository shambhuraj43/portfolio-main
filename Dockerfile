FROM python:3.10-slim-buster
ENV PYTHONNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "portfolio_website/manage.py", "runserver", "0.0.0:8000"]


