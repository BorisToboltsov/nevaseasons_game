

async def get_text(**kwargs):
    dialog_manager = kwargs.get('dialog_manager')
    correct_answer = dialog_manager.start_data.get('correct_answer')
    participant_answer = dialog_manager.start_data.get('participant_answer')
    command_name = dialog_manager.start_data.get('command_name')
    return {'correct_answer': correct_answer,
            'participant_answer': participant_answer,
            'command_name': command_name}
