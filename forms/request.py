from flask_wtf import FlaskForm
from wtforms import StringField, RadioField
from wtforms.validators import InputRequired, Regexp, ValidationError

from data import provider


class RequestForm(FlaskForm):
    goals = provider.get_goals()
    choices = list(map(lambda goal: (goal.goal_id, goal.name), goals))
    goal = RadioField(
        "Какая цель занятий?",
        validators=[InputRequired()],
        choices=choices,
        coerce=int,
        default=goals[-1].goal_id,
    )

    time = RadioField(
        "Сколько времени есть?",
        validators=[InputRequired()],
        choices=[
            ("1-2", "1-2 часа в&nbsp;неделю"),
            ("3-5", "3-5 часов в&nbsp;неделю"),
            ("5-7", "5-7 часов в&nbsp;неделю"),
            ("7-10", "7-10 часов в&nbsp;неделю"),
        ],
        default="3-5",
    )
    name = StringField("Вас зовут", validators=[InputRequired()])

    phone = StringField(
        "Ваш телефон",
        validators=[
            InputRequired(),
            Regexp("\+(\d|\s){5,}$", message="Используйте формат +372..."),
        ],
    )

    def validate_name(form, field):
        if len(field.data) < 5:
            raise ValidationError("Имя должно быть не короче 5 символов")
