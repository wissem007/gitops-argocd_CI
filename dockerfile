FROM python:3.8-slim-buster
RUN pip install flask
WORKDIR /app
COPY . .
EXPOSE 5000
ENTRYPOINT [ "python", "app.py" ]