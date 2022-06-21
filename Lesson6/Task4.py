class Car:

    is_police = False

    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed
        print(f'New Car: {self.name} (Color {self.color})')

    def go(self, speed=30):
        self.speed = speed
        print(f'{self.name}: Car is going')

    def stop(self):
        self.speed = 0
        print(f'{self.name}: Car is stop')

    def turn(self, direction):
        print(f'{self.name}: Car turned: {"left" if direction==0 else "right"}')

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}.'

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f'Over speed {self.name}: Car speed: {self.speed}.'
        else:
            return f'{self.name}: Car speed: {self.speed}.'

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Over speed {self.name}: Car speed: {self.speed}.'
        else:
            return f'{self.name}: Car speed: {self.speed}.'

class SportCar(Car):
    pass

class PoliceCar(Car):
    is_police = True

sport_car = SportCar("Sport car", "Red", 120)
sport_car.go()
sport_car.turn(1)
print(sport_car.show_speed())
sport_car.stop()
