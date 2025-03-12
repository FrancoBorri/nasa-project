FROM python:3.12-bookworm
ENV PYTHONUNBUFFERED=1
RUN mkdir /workspace
WORKDIR /workspace
COPY requirements.txt /workspace/
RUN python -m pip install -r requirements.txt
COPY . /workspace/