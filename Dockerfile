FROM python:3
RUN mkdir -p /app
WORKDIR /app
COPY main.py requirements.txt start.sh /app
RUN python -m pip install -r requirements.txt
CMD [ "sh", "start.sh" ]
