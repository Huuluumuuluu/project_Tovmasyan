"""
Практическая работа №16
Вариант 30 — Блок 1
Класс "Банк"
"""


class Bank:
    """Класс банковского счета."""

    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    def calculate_interest(self):
        """Вычисление процентных начислений."""
        interest = self.balance * self.interest_rate / 100
        return interest

    def withdraw_money(self, amount):
        """Снятие денег со счета."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Снято: {amount} руб.")
        else:
            print("Недостаточно средств на счете.")

    def show_balance(self):
        """Вывод текущего баланса."""
        print(f"Текущий баланс: {self.balance} руб.")


# Тестовый запуск
bank_account = Bank(10000, 5)

bank_account.show_balance()

interest = bank_account.calculate_interest()
print(f"Процентные начисления: {interest} руб.")

bank_account.withdraw_money(2500)
bank_account.show_balance()
