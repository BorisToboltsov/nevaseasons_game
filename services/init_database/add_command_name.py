from sqlalchemy.orm import Session

from config.database import load_database
from database.participant.models.participant import CommandName
from services.init_database.print_message_decorator import print_message


class InitDbSaveCommandName:
    def __init__(self, session: Session):
        self.name_list = [
            "Чумовые ящерицы",
            "Безбашенные кролики",
            "Забивные крокодилы",
            "Безумные ежи",
            "Изворотливые бегемоты",
            "Бдительные бородавочники",
            "Седые ёжики",
            "Бодрые барсуки",
            "Сметливые селезни",
            "Торопливые тритоны",
            "Отважные олени",
            "Геройские гиббоны",
            "Цепкие цапли",
            "Калёные козероги",
            "Задорные зайцелопы",
            "Кармические коалы",
            "Рассветные рыси",
            "Инакомыслящие сурикаты",
            "Нарядные нарвалы",
            "Мечтательные оцелоты",
            "Педантичные панголины",
            "Квантовые кетцали",
            "Нетерпеливые какомицили",
            "Дерзкие саламандры",
            "Надёжные тары",
            "Утопические единороги",
            "Яркие верветки",
            "Гостеприимные белки",
            "Болтливые яки",
            "Пикантные полутушканчики",
            "Ловкие трубкозубы",
            "Бионические бобры",
            "Космические каракатицы",
            "Дискотечные динго",
            "Рассветные горностаи",
            "Сосредоточенные фоссы",
            "Крутые гориллы",
            "Косматые гиппопотамы",
            "Озорные индри",
            "Везучие медузы",
            "Кинетические куду",
            "Лунные омары",
            "Мантические минотавры",
            "Благородные намбаты",
        ]
        self.session = session

    @print_message("Start add command name", "Complete add command name\n")
    def write_command_name(self):
        database_config = load_database()
        sm = database_config.get_sessionmaker
        for name in self.name_list:
            # Создаем новую запись.
            data = CommandName(
                name=name,
            )
            self.session.add(data)
        return self.session
