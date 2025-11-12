def add(a: float, b: float) -> float:
    """Возвращает сумму двух чисел"""
    return a + b


def subtract(a: float, b: float) -> float:
    """Возвращает разность a - b"""
    return a - b


def multiply(a: float, b: float) -> float:
    """Возвращает произведение"""
    return a * b


def divide(a: float, b: float) -> float:
    """Возвращает результат деления a / b, если b ≠ 0"""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b


def main():
    print("Добро пожаловать в калькулятор!")
    print("Доступные операции: +, -, *, /")
    
    while True:
        try:
            # Получаем ввод от пользователя
            num1 = float(input("Введите первое число: "))
            operation = input("Введите операцию (+, -, *, /): ").strip()
            num2 = float(input("Введите второе число: "))
            
            # Выполняем операцию
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            else:
                print("Ошибка: Неверная операция. Пожалуйста, используйте +, -, *, или /")
                continue
            
            print(f"Результат: {num1} {operation} {num2} = {result}")
            
            # Спрашиваем, хочет ли пользователь продолжить
            again = input("\nХотите выполнить ещё одну операцию? (да/нет): ").strip().lower()
            if again not in ('да', 'yes', 'y'):
                print("Спасибо за использование калькулятора!")
                break
                
        except ValueError as e:
            if "could not convert" in str(e):
                print("Ошибка: Пожалуйста, введите корректное число.")
            else:
                print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")


if __name__ == "__main__":
    main()
