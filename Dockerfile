FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*


# Copy calculator1.py and the test.py file to the /app directory
COPY calculator1.py /app/calculator1.py
COPY test.py /app/test.py


CMD printf "1\n4\n3\n" | python3 calculator1.py
#yess
