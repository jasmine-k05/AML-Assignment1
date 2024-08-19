FROM python:3.10-slim-bullseye
COPY . .

WORKDIR ./src
RUN python3 -m pip install -r requirements.txt
EXPOSE 8000

CMD ["python3", "inference.py"]