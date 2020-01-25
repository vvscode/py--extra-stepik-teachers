import json
import pathlib

from app import db
from data import models


def get_goals():
    return models.Goal.query.all()


def get_teachers(goal=None):
    query = models.Teacher.query

    if goal:
        query = query.filter(goal in model.Teacher.goals)

    return query.all()


def save_teachers(teachers):
    with open(f'{data_dir}/teachers.json', 'w') as file:
        file.write(json.dumps(teachers))


def get_teacher(id):
    return models.Teacher.get(id)


def save_lesson_request(data):
    print('data', data)
    try:
        with open(f'{data_dir}/requests.json') as file:
            list = json.loads(file.read())
    except OSError:
        list = []
    except json.decoder.JSONDecodeError:
        list = []

    list.append(data)

    with open(f'{data_dir}/requests.json', 'w') as file:
        file.write(json.dumps(list))


def save_lesson_booking(booking_request):
    save_lesson_request(booking_request)

    teachers = get_teachers()
    for teacher in teachers:
        if teacher['id'] == booking_request['teacher_id']:
            teacher['free'][booking_request['day']
                            ][booking_request['time']] = False

    save_teachers(teachers)
