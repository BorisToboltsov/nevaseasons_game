import os

from aiogram.enums import ContentType
from aiogram_dialog.api.entities import MediaAttachment


async def get_task_choice(**kwargs):
    dialog_manager = kwargs.get("dialog_manager")
    task = dialog_manager.dialog_data.get("current_task")
    send_answer = dialog_manager.dialog_data.get("send_answer")
    path_to_image = task.template.question.path_image
    if path_to_image:
        try:
            image = MediaAttachment(ContentType.PHOTO, path=f'{os.getenv("PATH_TO_IMAGE")}{path_to_image}')
            test_file = open(f'{os.getenv("PATH_TO_IMAGE")}{path_to_image}', "r")
            test_file.close()
        except FileNotFoundError:
            image = None
            path_to_image = None
    else:
        image = None
    return {
        "number_question": task.template.serial_number_question,
        "question_text": task.template.question.text,
        "answers_list": task.answers_list,
        "send_answer": send_answer,
        "path_to_image": path_to_image,
        "image": image
        # "not_send_answer": not send_answer,
    }


async def get_task_input(**kwargs):
    dialog_manager = kwargs.get("dialog_manager")
    task = dialog_manager.dialog_data.get("current_task")
    path_to_image = task.template.question.path_image
    if path_to_image:
        try:
            image = MediaAttachment(ContentType.PHOTO, path=f'{os.getenv("PATH_TO_IMAGE")}{path_to_image}')
            test_file = open(f'{os.getenv("PATH_TO_IMAGE")}{path_to_image}', "r")
            test_file.close()
        except FileNotFoundError:
            image = None
            path_to_image = None
    else:
        image = None
    return {
        "number_question": task.template.serial_number_question,
        "question_text": task.template.question.text,
        "path_to_image": path_to_image,
        "image": image
    }


async def get_start_message(**kwargs):
    dialog_manager = kwargs.get("dialog_manager")
    current_task = dialog_manager.dialog_data.get("current_task")
    if current_task is None:
        text = {
            "text": 'Нажми старт',
            "button": 'Старт',
        }
    else:
        text = {
            "text": 'Для следующего вопроса нажми вперед',
            "button": 'Вперед',
        }
    return text
