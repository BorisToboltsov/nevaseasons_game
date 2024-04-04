from config.config import Config, load_config
from config.database import load_database
from services.init_database.add_command_name import InitDbSaveCommandName
from services.init_database.add_game import InitDbSaveGame
from services.init_database.add_questions_answers_template import InitDbQuestionsAnswerTemplate

config: Config = load_config()
database_config = load_database()
sm = database_config.get_sessionmaker
session = sm()

init_db_save_game = InitDbSaveGame(session)
init_db_save_game.write_game()

init_db_command_name = InitDbSaveCommandName(session)
init_db_command_name.write_command_name()

init_db_qat = InitDbQuestionsAnswerTemplate(session)
init_db_qat.questions_answer_template()

session.commit()
