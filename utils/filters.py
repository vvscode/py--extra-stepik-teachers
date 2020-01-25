from app import app
from data import provider


@app.template_filter()
def ru_goal(goal):
    return goal if type(goal) == str else goal.name


@app.template_filter()
def ru_week_day(day):
    week = {
        "mon": "Понедельник",
        "tue": "Вторник",
        "wed": "Среда",
        "thu": "Четверг",
        "fri": "Пятница",
        "sat": "Суббота",
        "sun": "Воскресение",
    }
    return week.get(day, "Unknown day")
