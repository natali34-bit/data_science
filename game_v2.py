import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла, если угадали
    return count

# Пример использования функции
if __name__ == "__main__":
    # Загадать число от 1 до 100
    secret_number = np.random.randint(1, 101)  # Компьютер загадывает число
    print(f'Загаданное число: {secret_number}')  # Для проверки, можно убрать в финальной версии
    attempts = random_predict(secret_number)
    print(f'Количество попыток: {attempts}')