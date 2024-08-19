FROM python:3.10-slim-bullseye
COPY . .
RUN python3 -m pip install -r requirements.txt
WORKDIR ./src
EXPOSE 8000

CMD ["python3", "inference.py"]