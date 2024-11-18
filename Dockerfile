FROM python:3.12.5

WORKDIR /insurance_api

COPY /requirements.txt /insurance_api/requirements.txt

RUN pip install --upgrade -r /insurance_api/requirements.txt

COPY /models.py  server/
COPY /main.py  server/

CMD ["fastapi","run","server/main.py","--port","8000"]
