import time
from time import sleep


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {execution_time:.4f} секунд(с).")
        return result
    return wrapper

class Car:
    positionx: float
    positiony: float
    direction: float

    def __init__(self, x, y, r: float):
        self.positionx = x
        self.positiony = y
        self.direction = r

    def move(self, dx: float, dy: float):
        x = self.positionx
        y = self.positiony
        self.positionx = float(x) + float(dx)
        self.positiony = float(y) + float(dy)

    def turn(self, r: float):
        self.direction += r

    def __str__(self):
        return f"Car(position=[{self.positionx} , {self.positiony}], direction={self.direction})"


class Bus(Car):
    passengers: int = 0
    money: float = 0.0

    def __post_init__(self,x:float,y:float,r:float):
        super().__init__(x,y,r)
        self.passengers = 0
        self.money = 0

    @timer_decorator
    def enter(self):
        sleep(1)
        if self.passengers < 50:
            self.passengers += 1
            print(f"Пассажир {self.passengers} вошел в автобус.")
        else:
            print("Автобус полный.")

    @timer_decorator
    def exit(self):
        sleep(2)
        if self.passengers > 0:
            self.passengers -= 1
            print(f"Пассажир {self.passengers} вышел из автобуса.")
        else:
            print("Автобус пустой.")
    @timer_decorator
    def move(self,dx: float,dy:float):
        sleep(0.5)
        super().move(dx,dy)
        self.money += (dx+dy) * self.passengers * 50

    def __str__(self):
        return f"Bus \n position={self.positionx},{self.positiony} \n direction={self.direction}\n passengers={self.passengers}\n money earned={self.money}"

x=input("x: ")
y=input("y: ")
bus = Bus(x=x, y=y, r=90)

print(bus)
bus.enter()
bus.move(float(input("x: ")),float(input("y: ")))
bus.turn(float(input("r: ")))
bus.exit()
print(bus)