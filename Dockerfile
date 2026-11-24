FROM python:3.14-slim
#starts from a small official Linux image that already has Python 3.14. slim = minimal size.
WORKDIR /app
#creates the folder /app inside the container and works from there, like mkdir + cd.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#installs your libraries. --no-cache-dir keeps the image smaller.
COPY . .
#copies the rest of your project (code, tests) into /app.
RUN python train.py
#trains the model while building, so the image always contains a model that matches its library versions.
EXPOSE 8000
#notes that the app uses port 8000. This is documentation only.
CMD ["sh", "-c", "uvicorn apphi:myapi --host 0.0.0.0 --port ${PORT:-8000}"]

#the command that runs when the container starts. This is your usual uvicorn command, with two differences:
#--host 0.0.0.0 → required in Docker. It means "accept connections from outside the container". Without it, the API only listens inside the container and your browser can't reach it.
#there is No --reload, since that's for development only.


