from flask_wtf import FlaskForm
from wtforms import StringField, RadioField
from wtforms.validators import InputRequired, Regexp, ValidationError


class BookingForm(FlaskForm):
    day = StringField()
    time = StringField()

    name = StringField("Вас зовут", validators=[InputRequired()])
    phone = StringField(
        "Ваш телефон",
        validators=[
            InputRequired(),
            Regexp("\+(\d|\s){5,}$", message="Используйте формат +372..."),
        ],
    )

    def validate_name(form, field):
        if len(field.data) < 3:
            raise ValidationError("Имя должно быть не короче 3 символов")
