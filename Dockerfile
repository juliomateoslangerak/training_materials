FROM python:3.9
LABEL authors="Julio Mateos Langerak"

WORKDIR /app
COPY requirements.txt requirements.txt
COPY server_conf_camera_0.py camera_server_conf.py
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["python", "-m", "microscope.device_server", "camera_server_conf.py"]

