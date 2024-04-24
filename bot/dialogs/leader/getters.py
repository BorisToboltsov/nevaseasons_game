from aiogram.enums import ContentType
from aiogram_dialog.api.entities import MediaAttachment, MediaId


async def get_text(**kwargs):
    dialog_manager = kwargs.get("dialog_manager")
    correct_answer = dialog_manager.start_data.get("correct_answer")
    participant_answer = dialog_manager.start_data.get("participant_answer")
    command_name = dialog_manager.start_data.get("command_name")
    task = dialog_manager.start_data.get("task")

    if task.template.question.type_response == 3:
        photo_id = dialog_manager.start_data.get("photo_id")
        photo = MediaAttachment(ContentType.PHOTO, file_id=MediaId(photo_id))
    else:
        photo = None

    return {
        "correct_answer": correct_answer,
        "participant_answer": participant_answer,
        "command_name": command_name,
        "photo": photo,
    }
