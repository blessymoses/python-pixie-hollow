class InsufficientAmount(Exception):
    pass


class Account(object):
    """
    A Bank Account
    """

    def __init__(self, name: str, balance: int = 0) -> None:
        """
        Returns an account object with customer name and account balance
        """
        self.name = name
        self.balance = balance

    def withdraw(self, amount) -> int:
        """
        Returns the account balance after withdrawing the amount
        """
        if self.balance < amount:
            raise InsufficientAmount(f"Not enough balance to withdraw {amount}")
        self.balance -= amount
        return self.balance

    def deposit(self, amount) -> int:
        """
        Returns the account balance after depositing the amount
        """
        self.balance += amount
        return self.balance
