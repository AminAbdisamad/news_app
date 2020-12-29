FROM python:3.9.1-alpine3.12
WORKDIR "/app"
COPY Pipfile .
RUN pip3 install pipenv
RUN pipenv install
COPY . .
# CMD ["pipenv","run","python","app.py"]
RUN pipenv shell
CMD ["gunicorn", "-w" ,"2" ,"-b", "0.0.0.0:8080", "run:app"]

