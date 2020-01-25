"""initial seed

Revision ID: 00000000002
Revises:
Create Date: 2020-01-25 15:00:45.144060

"""
import json
import os

from app import db
from models import Teacher, Goal

# revision identifiers, used by Alembic.
revision = "00000000002"
down_revision = "00000000001"
branch_labels = None
depends_on = None

basedir = os.path.abspath(os.path.dirname(__file__))

with open(
    os.path.join(basedir, "00000000002_initial_state_seed__teachers.json")
) as file:
    teachers = json.loads(file.read())


with open(os.path.join(basedir, "00000000002_initial_state_seed__goals.json")) as file:
    goals = json.loads(file.read())


def upgrade():
    # Goals
    goals_map = {}
    for goal_slug in goals.keys():
        goal = Goal(name=goals[goal_slug])
        db.session.add(goal)
        goals_map[goal_slug] = goal

    db.session.commit()

    # Teachers
    for teacher_item in teachers:
        teacher = Teacher(
            name=teacher_item["name"],
            about=teacher_item["about"],
            rating=teacher_item["rating"],
            price=teacher_item["price"],
            picture=teacher_item["picture"],
            free=json.dumps(teacher_item["free"]),
        )

        db.session.add(teacher)

        for teacher_goal in teacher_item["goals"]:
            teacher.goals.append(goals_map[teacher_goal])

    db.session.commit()


def downgrade():
    print(f"Migration #{revision} has no downgrade option")
    print("But you can add here removing data from columns")
