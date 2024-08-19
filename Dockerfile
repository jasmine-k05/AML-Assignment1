FROM python:3.10-slim-bullseye
COPY . .

RUN python3 -m pip install -r requirements.txt
WORKDIR ./src
EXPOSE 8501

CMD ["python3", "-m", "streamlit", "run", "app.py"]
