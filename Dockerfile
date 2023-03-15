FROM python:3.8-slim-buster
WORKDIR /src

COPY src/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD python3 -m pytest -v --junit-xml /src/test_results.xml test_api_main.py