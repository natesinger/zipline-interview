FROM python:3.11-bullseye

RUN [ "mkdir", "-p", "/wsgi", "/frontend"]

COPY "gui/wsgi/" "/wsgi"
COPY "gui/frontend/" "/frontend"
COPY "simulation" "/simulation"

RUN ["pip3", "install", "-r", "/wsgi/requirements.txt"]

WORKDIR "/simulation"
RUN ["python3", "run.py"]
RUN ["cp", "simulation.json", "/wsgi/"]

WORKDIR "/wsgi"
CMD [ "bash", "start.sh"]
