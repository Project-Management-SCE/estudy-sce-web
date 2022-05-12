FROM python:3.7-alpine
WORKDIR /Estudy_Project
ADD . /Estudy_Project
RUN pip install -r requirements.txt
CMD ["python", "manage.py","makemigrations"]
CMD ["python", "manage.py","migrate"]
CMD ["python", "manage.py","runserver"]
EXPOSE 8000
