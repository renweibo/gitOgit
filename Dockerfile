FROM python:3.9-slim

COPY requirements.txt .
RUN pip3 install -U -r requirements.txt
RUN pip3 install -U gitOgit
CMD gitOgit