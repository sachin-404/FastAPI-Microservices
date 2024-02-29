FROM python:3.10.13-slim

RUN mkdir -p /app
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN python -m textblob.download_corpora
COPY . /app/
EXPOSE 8000
CMD [ "python", "main.py" ]