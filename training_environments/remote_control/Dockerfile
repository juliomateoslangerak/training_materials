FROM jupyter/scipy-notebook:python-3.9
LABEL authors="Julio Mateos Langerak"

COPY requirements.txt requirements.txt
COPY ./notebooks notebooks
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYRO_SERIALIZER=pickle
