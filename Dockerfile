FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD gunicorn --bind=0.0.0.0:${PORT} --workers=${SERVER_WORKER_NUMBER} 'server:create_app()' --access-logfile=access.log --error-logfile=error.log --capture-output