
from enum import Enum


class Priority(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class TaskStatus(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


class AnswerOption(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
