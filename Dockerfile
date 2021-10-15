FROM python:3.8-alpine
EXPOSE 5000/tcp
WORKDIR /yacng
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY /yacng .
CMD [ "python", "./app.py" ]