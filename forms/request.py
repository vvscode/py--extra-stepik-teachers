from flask_wtf import FlaskForm
from wtforms import StringField, RadioField
from wtforms.validators import InputRequired, Regexp, ValidationError, length

from data import provider


class RequestForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.init_goal()

    def init_goal(self):
        goals = provider.get_goals()
        choices = list(map(lambda goal: (goal.goal_id, goal.name), goals))
        self.goal.choices = choices

    goal = RadioField("Какая цель занятий?", validators=[
                      InputRequired()], coerce=int)

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
    name = StringField("Вас зовут", validators=[
                       InputRequired(), length(min=5, message="Должно быть не короче 5 символов")])

    phone = StringField(
        "Ваш телефон",
        validators=[
            InputRequired(),
            Regexp("\+(\d|\s){5,}$", message="Используйте формат +372..."),
        ],
    )
