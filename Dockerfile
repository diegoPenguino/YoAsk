FROM python:3.9
WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 3000
CMD [ "flask", "run","--host","0.0.0.0","--port","3000"]
