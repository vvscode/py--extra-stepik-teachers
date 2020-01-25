import json
import pathlib

from app import db
from data import models


def get_goals():
    return models.Goal.query.all()


def get_goal(id):
    return models.Goal.query.get(id)


def get_teachers(goal=None):
    query = models.Teacher.query

    if goal:
        query = query.filter(models.Teacher.goals.any(models.Goal.goal_id == goal))

    return query.all()


def save_teachers(teachers):
    with open(f"{data_dir}/teachers.json", "w") as file:
        file.write(json.dumps(teachers))


def get_teacher(id):
    return models.Teacher.query.get(id)


def save_lesson_request(data):
    request = models.Request()

    request.goal_id = data["goal"]
    request.time = data["time"]
    request.name = data["name"]
    request.phone = data["phone"]
    db.session.add(request)
    db.session.commit()


def save_lesson_booking(booking_request):
    teacher = get_teacher(booking_request["teacher_id"])

    booking = models.Booking(teacher=teacher)
    booking.time = booking_request["time"]
    booking.day = booking_request["day"]
    booking.name = booking_request["name"]
    booking.phone = booking_request["phone"]
    db.session.add(booking)

    # trick with setters
    free = teacher.free
    free[booking_request["day"]][booking_request["time"]] = False
    teacher.free = free

    # https://stackoverflow.com/questions/4201455/sqlalchemy-whats-the-difference-between-flush-and-commit
    db.session.flush()
    db.session.commit()
