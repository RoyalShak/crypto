FROM ubuntu:20.04
WORKDIR C:/Users/henle/PycharmProjects/Crypto
RUN python --version
COPY req.txt .
COPY crypto.py C:/Users/henle/PycharmProjects/Crypto/crypto.py
RUN pip3 install --upgrade pip && pip3 install -r req.txt
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt install python-is-python3
RUN apt-get install vim -y
CMD ["python", "-u", "crypto.py"]





