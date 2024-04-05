

async def get_task_choice(**kwargs):
    dialog_manager = kwargs.get('dialog_manager')
    task = dialog_manager.dialog_data.get('current_task')
    send_answer = dialog_manager.dialog_data.get('send_answer')
    return {'number_question': task.template.serial_number_question,
            'question_text': task.template.question.text,
            'answers_list': task.answers_list,
            'send_answer': send_answer,
            'not_send_answer': not send_answer}


async def get_task_input(**kwargs):
    dialog_manager = kwargs.get('dialog_manager')
    task = dialog_manager.dialog_data.get('current_task')
    return {'number_question': task.template.serial_number_question,
            'question_text': task.template.question.text}
