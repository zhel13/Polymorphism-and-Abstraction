from typing import List


class Account:
    def __init__(self, owner: str, amount=0):
        self.owner = owner
        self.amount = amount
        self._transaction: List = []
        
    @property
    def balance(self):
        return self.amount + sum(self._transaction)


    def handle_transaction(self, transaction_amount):
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")
        self._transaction.append(transaction_amount)
        return f'New balance: {self.balance}'

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        return self.handle_transaction(amount)

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'

    def __len__(self):
        return len(self._transaction)

    def __getitem__(self, index):
        return self._transaction[index]

    def __reversed__(self):
        return reversed(self._transaction)

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __add__(self, other):
        new_account = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
        new_account._transactions = self._transaction + other._transactions
        return new_account
    

