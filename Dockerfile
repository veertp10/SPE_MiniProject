FROM ubuntu:latest


# Copy calculator1.py and the test.py file to the /app directory
COPY calculator1.py /app/calculator1.py
COPY test.py /app/test.py


CMD printf "1\n4\n3\n" | python3 calculator1.py
