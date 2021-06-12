FROM python:rc-alpine3.13

WORKDIR /opt/app

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "api.py" ]