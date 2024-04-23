from dataclasses import dataclass
from typing import Type

from database.task.models.answers import Answer
from database.task.models.template import Template


@dataclass
class Task:
    template: Template
    answers_list: list[Type[Answer]]
