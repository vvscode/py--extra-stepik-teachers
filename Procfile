release: FLASK_APP=main.py flask db migrate -m "Initial structure"

web: gunicorn main:app