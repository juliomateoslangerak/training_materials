FROM python:3.9
LABEL authors="Julio Mateos Langerak"

WORKDIR /app
COPY requirements.txt requirements.txt
COPY server_conf_light_0.py server_conf_light_0.py
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYRO_SERIALIZER=pickle

EXPOSE 9000

CMD ["python", "-m", "microscope.device_server", "server_conf_light_0.py"]