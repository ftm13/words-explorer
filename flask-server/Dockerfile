FROM python:3.6

EXPOSE 5000

WORKDIR /temp/

COPY requirements.txt /temp/requirements.txt
RUN pip install -r requirements.txt

COPY . /temp

CMD python src/hello.py