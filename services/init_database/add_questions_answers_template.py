from sqlalchemy.orm import Session

from database.game.crud.game import DbGame
from database.task.models.answers import Answer
from database.task.models.questions import Question
from database.task.models.template import Template
from services.init_database.print_message_decorator import print_message


class InitDbQuestionsAnswerTemplate:
    def __init__(self, session: Session):
        self.session = session
        self.questions_list = [
            {'id': 1, 'text': """В начале мая 1703 года Пётр и его команда причалили к небольшому острову и решили закрепиться здесь! Остров назывался на финский манер “Янисаари”, что переводится как “Заячий остров”. Перед крепостью сидит зайчик, который спасается на деревянных сваях от очередного наводнения.
Вам поручено назвать нашего зайца. Подберите из предложенных вариантов имя, которое созвучнее всего иностранному названию острова Янисаари.
В ответ укажите номер правильного ответа.""",
             'path_image': '',
             'requires_verification': False,
             'type_response': 1},
            {'id': 2, 'text': """Верно! Мы назвали зайца. По легенде, заяц, спасшийся от наводнения, прыгнул на сапог Петру I, который в этот момент выходил из лодки на остров. Царь и его единомышленники начнут на этом острове  строительство крепости, а закончит возведение укреплений другая правительница. Крепость даст нам подсказку, в каком году завершилось строительство каменных укреплений.
В ответ укажите этот год и подойдите к месту с подсказкой.""",
             'path_image': '',
             'requires_verification': False,
             'type_response': 2},
            {'id': 3, 'text': """Толщина крепостных стен - 20 метров. Внешняя стена - 6 метров, внутренняя - 2 метра, а между этими стенами свободное пространство - каземат - 12 метров, где находится продовольствие, техника и работают солдаты.
Мы совсем заработались. Пора подкрепиться. Попробуем одно из любимых блюд императора!
Блюдо это зашифровано, но вы без труда его отгадаете. Для разгадки шифра воспользуйтесь азбукой заключённых тюрьмы Трубецкого бастиона Петропавловской крепости.
Как известно, у арестантов была азбука перестукиваний. Сначала стучали номер строки, затем - столбца.
Послушайте аудио-сообщение и разгадайте шифр, тогда вы и получите название лакомства. Это блюдо варила на миндальном молоке сама императрица Екатерина I!
В ответ укажите название блюда.""",
             'path_image': '1.png',
             'requires_verification': True,
             'type_response': 2},
            {'id': 4, 'text': """Вы нашли нужное здание! Перед нами дом для зажиточных - среднего класса. Мы поселим сюда инженеров и устроим склады. Инженерный дом появился здесь в царствование Елизаветы Петровны - в середине XVIII века.
Есть в крепости и более молодые достопримечательности. Идите прямо вдоль инженерного дома, пока не встретите необычный памятник, осмотрите его. На памятнике будет надпись с указанием трёх государств, которые связаны с этой скульптурой.
Перечислите эти государства в ответе с заглавных букв и без запятых.""",
             'path_image': '',
             'requires_verification': True,
             'type_response': 2},
            {'id': 5, 'text': """Флаг в крепости часто путают с флагом Великобритании, где на синем фоне расположены красно-белые кресты. Гюйс в нашей крепости представляет собой синий крест Андрея Первозванного - покровителя моряков, и белый крест Георгия Победоносца - символа военной мощи, на алом фоне. Здесь соединяются  море и военное дело.
Традицию поднимать такой флаг на носу военных кораблей и над морскими крепостями установил Петр I, вдохновленный европейским опытом. Флаг стал символом центрального бастиона крепости - Нарышкина, названного в честь руководителя строительством Кирилла Нарышкина.
На Нарышкине бастионе с 1731 года развевается гюйс, а со времён Александра II в полдень стреляет пушка.
Рядом с бастионом располагается дом важного человека. Около дома вы найдёте 12 стульев и распространённый измерительный прибор. У главного входа в это здание есть табличка с указанием должности человека, который жил в доме.
В ответ пришлите фото таблички и напишите, кто жил в этом доме.""",
             'path_image': '1.png',
             'requires_verification': True,
             'type_response': 3},
        ]
        self.answers_list = [
            {'text': 'Евгений',
             'is_correct': False,
             'question_id': 1},
            {'text': 'Арсений',
             'is_correct': True,
             'question_id': 1},
            {'text': 'Семён',
             'is_correct': False,
             'question_id': 1},
            {'text': 'Христиан',
             'is_correct': False,
             'question_id': 1},
            {'text': '1740',
             'is_correct': True,
             'question_id': 2},
            {'text': 'перловка',
             'is_correct': False,
             'question_id': 3},
            {'text': 'Америка Италия Россия',
             'is_correct': True,
             'question_id': 4},
            {'text': 'Комендант',
             'is_correct': True,
             'question_id': 5},
        ]
        self.template_list = [
            {'name': 'ППК команда',
             'team_number': 1,
             'serial_number_question': 1,
             'game_id': 1,
             'question_id': 1},
            {'name': 'ППК команда',
             'team_number': 1,
             'serial_number_question': 2,
             'game_id': 1,
             'question_id': 2},
            {'name': 'ППК команда',
             'team_number': 1,
             'serial_number_question': 3,
             'game_id': 1,
             'question_id': 3},
            {'name': 'ППК команда',
             'team_number': 1,
             'serial_number_question': 4,
             'game_id': 1,
             'question_id': 4},
            {'name': 'ППК команда',
             'team_number': 1,
             'serial_number_question': 5,
             'game_id': 1,
             'question_id': 5},
        ]

    @print_message("Start add QuestionsAnswerTemplate", "Complete add QuestionsAnswerTemplate\n")
    def questions_answer_template(self):
        game_db = DbGame()
        game = game_db.get_game_by_name(self.session, 'ППК')
        for question in self.questions_list:
            # Создаем новую запись.
            question_data = Question(
                text=question['text'],
                path_image=question['path_image'],
                requires_verification=question['requires_verification'],
                type_response=question['type_response'],
            )
            self.session.add(question_data)
            self.session.flush()
            for answer in self.answers_list:
                if answer.get('question_id') == question.get('id'):
                    answer_data = Answer(answer_text=answer.get('text'),
                                         is_correct=answer.get('is_correct'),
                                         question_id=question_data.id)
                    self.session.add(answer_data)
            for template in self.template_list:
                if template.get('question_id') == question.get('id'):
                    template_data = Template(name=template.get('name'),
                                             team_number=template.get('team_number'),
                                             serial_number_question=template.get('serial_number_question'),
                                             game_id=game.id,
                                             question_id=question_data.id,
                                             )
                    self.session.add(template_data)
        return self.session
