# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.
def paragraph():
    print('-' * 100)


class Car:
    def __init__(cls, speed, colour, name, is_police=False):
        cls.speed = speed
        cls.colour = colour
        cls.name = name
        cls.is_police = is_police

    def go(self):
        print(f'{self.name} rides')

    def stop(self):
        print(f'{self.name} stopped')

    def turn(self, direction):
        print(f'{self.name} turned {direction}')

    def show_speed(self):
        print(f'Current speed {self.speed}')

    def params(self):
        param = f'Car brand: {self.name}, Car colour: {self.colour}'
        if self.is_police:
            param = f"{param}. It's a sound of da police!"
        print(param)

    def change_speed(cls, new_speed):
        cls.speed = new_speed


class TownCar(Car):
    def __init__(cls, speed, colour, name):
        super().__init__(speed, colour, name)
        if speed > 60:
            print('\nSpeed exceeded!\n')


class SportCar(Car):
    def __init__(cls, speed, colour, name):
        super().__init__(speed, colour, name)


class WorkCar(Car):
    def __init__(cls, speed, colour, name):
        super().__init__(speed, colour, name)
        if speed > 40:
            print('\nSpeed exceeded!\n')


class PoliceCar(Car):
    def __init__(cls, speed, colour, name, is_police=True):
        super().__init__(speed, colour, name, is_police)


paragraph()

person_car = TownCar(70, 'Red', 'Toyota')
person_car.go()
person_car.turn('left')
person_car.show_speed()
person_car.change_speed(50)
person_car.go()
person_car.turn('right')
person_car.show_speed()
person_car.stop()
person_car.params()

paragraph()

worker_car = WorkCar(50, 'Black', 'Ford')
worker_car.go()
worker_car.turn('left')
worker_car.stop()
worker_car.params()

paragraph()

police_car = PoliceCar(90, 'Blue-White', 'Mustang')
police_car.go()
police_car.turn('drift')
police_car.stop()
police_car.params()

paragraph()

sport_car = SportCar(120, 'Red', 'Ferrari')
sport_car.go()
sport_car.turn('right drift')
sport_car.stop()
sport_car.params()

# Вот резултаты, Александр. Чтобы не пришлось самому запускать)
# Speed exceeded!
#
# Toyota rides
# Toyota turned left
# Current speed 70
# Toyota rides
# Toyota turned right
# Current speed 50
# Toyota stopped
# Car brand: Toyota, Car colour: Red
# ----------------------------------------------------------------------------------------------------
#
# Speed exceeded!
#
# Ford rides
# Ford turned left
# Ford stopped
# Car brand: Ford, Car colour: Black
# ----------------------------------------------------------------------------------------------------
# Mustang rides
# Mustang turned drift
# Mustang stopped
# Car brand: Mustang, Car colour: Blue-White. It's a sound of da police!
# ----------------------------------------------------------------------------------------------------
# Ferrari rides
# Ferrari turned right drift
# Ferrari stopped
# Car brand: Ferrari, Car colour: Red
