import json
from sqlalchemy import Column, ForeignKey, Integer, Numeric, Table, Text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from app import db

Base = db.Model
metadata = Base.metadata

teachers_to_goals = Table(
    "teachers_to_goals",
    Base.metadata,
    Column("teachers", Integer, ForeignKey("teachers.teacher_id", ondelete="CASCADE")),
    Column("goals", Integer, ForeignKey("goals.goal_id", ondelete="CASCADE")),
)


class Goal(Base):
    __tablename__ = "goals"

    goal_id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)


class Teacher(Base):
    __tablename__ = "teachers"

    teacher_id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    about = Column(Text)
    rating = Column(Text, nullable=False)
    price = Column(Integer, nullable=False)
    picture = Column(Text)
    _free = Column("free", Text, nullable=False)
    goals = relationship("Goal", secondary=teachers_to_goals, backref="teachers")

    @property
    def free(self):
        if not self._free:
            return {}
        return json.loads(self._free)

    @free.setter
    def free(self, value):
        self._free = json.dumps(value)


class Booking(Base):
    __tablename__ = "bookings"

    booking_id = Column(Integer, primary_key=True)
    teacher_id = Column(
        ForeignKey("teachers.teacher_id", ondelete="CASCADE"), nullable=False
    )
    day = Column(Text, nullable=False)
    time = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    phone = Column(Text, nullable=False)

    teacher = relationship("Teacher")


class Request(Base):
    __tablename__ = "requests"

    request_id = Column(Integer, primary_key=True)
    goal_id = Column(ForeignKey("goals.goal_id"), nullable=False)
    time = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    phone = Column(Text, nullable=False)

    goal = relationship("Goal")
