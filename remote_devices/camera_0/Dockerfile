FROM python:3.9
LABEL authors="Julio Mateos Langerak"

WORKDIR /app
COPY requirements.txt requirements.txt
COPY server_conf_camera_0.py server_conf_camera_0.py
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYRO_SERIALIZER=pickle

EXPOSE 8000

CMD ["python", "-m", "microscope.device_server", "server_conf_camera_0.py"]

#FROM balenalib/%%BALENA_MACHINE_NAME%%-python:3-stretch-run
#
## enable container init system.
#ENV INITSYSTEM on
#
## use `install_packages` if you need to install dependencies,
## for instance if you need git, just uncomment the line below.
## RUN install_packages git
#RUN pip install --upgrade pip
#RUN pip install Pyro4 dill
#
#ENV PYRO_SERIALIZERS_ACCEPTED=serpent,json,marshal,pickle,dill
#ENV PYTHONUNBUFFERED=0
#
#ENTRYPOINT ["pyro4-ns"]
#
#EXPOSE 9090