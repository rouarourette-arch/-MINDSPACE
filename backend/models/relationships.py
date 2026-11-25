
from sqlalchemy.orm import relationship

from backend.models.user_model import User
from backend.models.category_model import Category
from backend.models.task_model import Task
from backend.models.planner_event_model import PlannerEvent
from backend.models.focus_session_model import FocusSession
from backend.models.quiz_model import Quiz
from backend.models.question_model import Question
from backend.models.quiz_result_model import QuizResult


# User relationships
User.categories = relationship(
    Category, back_populates="user"
)
User.tasks = relationship(
    Task, back_populates="user"
)
User.planner_events = relationship(
    PlannerEvent, back_populates="user"
)
User.focus_sessions = relationship(
    FocusSession, back_populates="user"
)
User.quiz_results = relationship(
    QuizResult, back_populates="user"
)


# Category relationships
Category.user = relationship(
    User, back_populates="categories"
)
Category.tasks = relationship(
    Task, back_populates="category"
)


# Task relationships
Task.user = relationship(
    User, back_populates="tasks"
)
Task.category = relationship(
    Category, back_populates="tasks"
)
Task.planner_events = relationship(
    PlannerEvent, back_populates="task"
)
Task.focus_sessions = relationship(
    FocusSession, back_populates="task"
)


# PlannerEvent relationships
PlannerEvent.user = relationship(
    User, back_populates="planner_events"
)
PlannerEvent.task = relationship(
    Task, back_populates="planner_events"
)


# FocusSession relationships
FocusSession.user = relationship(
    User, back_populates="focus_sessions"
)
FocusSession.task = relationship(
    Task, back_populates="focus_sessions"
)


# Quiz relationships
Quiz.questions = relationship(
    Question, back_populates="quiz"
)
Quiz.results = relationship(
    QuizResult, back_populates="quiz"
)


# Question relationships
Question.quiz = relationship(
    Quiz, back_populates="questions"
)


# QuizResult relationships
QuizResult.user = relationship(
    User, back_populates="quiz_results"
)
QuizResult.quiz = relationship(
    Quiz, back_populates="results"
)
