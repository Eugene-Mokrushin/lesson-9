# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.

import time


class TrafficLight:
    _colour = 'Red', 'Yellow', 'Green'
    _timer = 7, 2, 5
    condition = 0

    def running(self):
        while True:
            print(self._colour[self.condition])
            time.sleep(self._timer[self.condition])
            if self.condition == 2:
                self.condition = 0
            elif self.condition not in (0, 1, 2):
                print('TrafficLight does not work')
                break
            else:
                self.condition += 1


traffic_lights = TrafficLight()
traffic_lights.running()
