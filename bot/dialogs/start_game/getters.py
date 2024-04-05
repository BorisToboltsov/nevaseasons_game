# db_template = DbTemplate()
# templates = (db_template.get_task_list_by_template())
from database.task.crud.answers import DbAnswer


async def get_task(**kwargs):
    dialog_manager = kwargs.get('dialog_manager')
    participant = dialog_manager.start_data.get('participant')
    # 724746757
    # print(dialog_manager.start_data)
    templates = dialog_manager.start_data.get('templates')
    template = templates.pop(0)
    session = dialog_manager.middleware_data.get('session')
    db_answer = DbAnswer()
    answers_list = db_answer.get_answer_list_by_question(template.question_id, session=session)
    print(template.question.text)
    return {'number_question': template.serial_number_question,
            'question_text': template.question.text,
            'answers_list': answers_list}
