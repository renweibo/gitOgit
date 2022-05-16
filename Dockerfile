FROM python:3.9-slim

COPY requirements_dev.txt .
RUN pip3 install -U -r requirements_dev.txt
RUN pip3 install -U gitOgit
CMD gitOgit