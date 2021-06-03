# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
def paragraph():
    """
    Разделяет текст на параграфы
    :return:
    """
    print('-' * 100)


class Stationery:
    def __init__(cls, title):
        cls.title = title
        print(f'{title} project')

    @staticmethod
    def draw(obj, tool):
        print('Start rendering')
        print(f'{tool} has drawn {obj}')


class Pen(Stationery):
    tool = 'Pen'

    def __init__(cls, title):
        super().__init__(title)

    def use_tool(self, obj, tool=tool):
        super().draw(obj, tool)


class Pencil(Stationery):
    tool = 'Pencil'

    def __init__(cls, title):
        super().__init__(title)

    def use_tool(self, obj, tool=tool):
        super().draw(obj, tool)


class Handle(Stationery):
    tool = 'Handle'

    def __init__(cls, title):
        super().__init__(title)

    def use_tool(self, obj, tool=tool):
        super().draw(obj, tool)


paragraph()

pen = Pen('Face')
pen.use_tool('circle')

paragraph()

pen = Pen('Eyes')
pen.use_tool('circle')
pen.use_tool('circle')

paragraph()

pencil = Pencil('Nose')
pencil.use_tool('triangle')

paragraph()

handle = Handle('Mouth')
handle.use_tool('arc')
# Нарисовали лицо:)
