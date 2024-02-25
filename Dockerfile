FROM ubuntu:latest


# Copy calculator.py and the test file to the /app directory
COPY calculator_main.py /app/calculator1.py
COPY calculator_test.py /app/test.py


CMD printf "1\n4\n3\n" | python3 calculator1.py
