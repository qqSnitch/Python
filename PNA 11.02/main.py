import random


def multiply_vectors(a, b):
    """Умножение векторов"""
    return sum(x * y for x, y in zip(a, b))


def argmax(vector):
    """Поиск индекса максимального элемента"""
    return max(range(len(vector)), key=lambda i: vector[i])


class WTANeuron:
    def __init__(self, n_inputs, learning_rate=0.1):
        # Инициализация весов случайными числами от 0 до 1
        self.weights = [random.random() for _ in range(n_inputs)]
        self.learning_rate = learning_rate

    def forward(self, inputs):
        # Вычисление выходных значений
        outputs = []
        for i in range(len(inputs)):
            output = sum(x * y for x, y in zip(inputs,self.weights))
            outputs.append(output)

        # Поиск победителя
        winner_idx = argmax(outputs)

        # Создание результата с единицей в позиции победителя
        result = [0.0] * len(outputs)
        result[winner_idx] = outputs[winner_idx]
        return result

    def train(self, inputs, targets):
        # Получение текущих выходных значений
        outputs = self.forward(inputs)

        # Обновление весов
        for i in range(len(inputs)):
            error = targets[i] - outputs[i]
            if error != 0:
                for j in range(len(self.weights)):
                    self.weights[j] += self.learning_rate * error * inputs[i][j]


# Пример использования
wtaneuron = WTANeuron(n_inputs=3)

# Тестовые данные
test_inputs = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Исходные веса:", wtaneuron.weights)
print("\nТестовый прогон:")
for inp in test_inputs:
    output = wtaneuron.forward([inp])  # Передаем как список списков
    print(f"Вход: {inp}, Выход: {output}")

# Обучение
test_targets = [10, 20, 30]
wtaneuron.train(test_inputs, test_targets)
print("\nВеса после обучения:", wtaneuron.weights)