FROM python:3.9.17-slim
RUN pip install flask
WORKDIR /app
COPY /.vscode/app.py .
EXPOSE 5000
ENTRYPOINT [ "python", "app.py" ]