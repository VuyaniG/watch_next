FROM python:latest

ADD watch_next.py .

COPY movies.txt .
CMD python watch_next.py