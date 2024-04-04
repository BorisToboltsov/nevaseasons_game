# db_template = DbTemplate()
# templates = (db_template.get_task_list_by_template())


async def get_task(**kwargs):
    dialog_manager = kwargs.get('dialog_manager')
    participant = dialog_manager.start_data.get('participant')
    # print(kwargs)
    return {'text': participant.telegram_id}
