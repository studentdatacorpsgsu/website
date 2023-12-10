FROM python:3.11
ENV PYTHONUNBUFFERED=1
WORKDIR /sdcweb
COPY requirements.txt requirements.txt
COPY . /sdcweb/
RUN pip3 install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
