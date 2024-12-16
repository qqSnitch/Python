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

class Client:
    Cod: float
    Name: str
    Date: float
    Size: float
    Percent: float

    def __init__(self, c, n, d, s, p):
        self.Cod = c
        self.Name = n
        self.Date = d
        self.Size = s
        self.Percent = p

    def __str__(self):
        return f"Клиент {self.Name}, код: {self.Cod}, дата: {self.Date}, вклад: {self.Size}, процент: {self.Percent}"


class Bank(Client):
    def __init__(self):
        self.client_base = []

    def add_client(self, Client):
        self.client_base.append(Client)

    def show_by_money(self, money):
        filtered_clients = [
            str(client)
            for client in self.client_base
            if client.Size > money
        ]
        return "\n".join(filtered_clients)

    def show_by_code(self, code):
        for client in self.client_base:
            if client.Cod == code:
                return str(client)
        return "Клиент с данным кодом не найден"
    @timer_decorator
    def show_by_proc(self, proc):
        filtered_clients = [
            str(client)
            for client in self.client_base
            if client.Percent > proc
        ]
        sleep(0.5)
        return "\n".join(filtered_clients)

    # Создание клиентов


client1 = Client("C001", "Иван Иванов", "2023-01-01", 10000, 5)
client2 = Client("C002", "Мария Петрова", "2023-02-15", 20000, 7)
client3 = Client("C003", "Алексей Сидоров", "2023-03-20", 15000, 6)

# Создание банка и добавление клиентов
bank = Bank()
bank.add_client(client1)
bank.add_client(client2)
bank.add_client(client3)


# Использование декоратора для метода add_client
def add_client(client):
    bank.client_base.append(client)


# Тестирование методов банка
print(bank.show_by_money(10000))
print()
print(bank.show_by_code("C002"))
print()
print(bank.show_by_proc(5))