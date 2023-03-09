FROM python:3.7

ENV PYTHONUNBUFFERED 1


COPY requirements.txt /code/requirements.txt
WORKDIR /code
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . .
# CMD ["celery", "-A", "innovation", "worker", "--beat", "--scheduler", "django", "--loglevel=info"]