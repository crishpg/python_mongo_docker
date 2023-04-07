FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 27017
COPY . .
COPY daemon.py /usr/src/app
CMD [ "python", "./daemon.py" ]


 
