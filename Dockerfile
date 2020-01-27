FROM python:3.8.1-alpine3.10

RUN pip3 install --upgrade pip && pip3 install extractCMRRPhysio

ENTRYPOINT ["extractCMRRPhysio"]
