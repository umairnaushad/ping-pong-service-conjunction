FROM python:rc-alpine3.13

WORKDIR /opt/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5001

ENTRYPOINT [ "python" ]

CMD [ "api.py" ]
