class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f"{sum(self._income.values())}"


worker_1 = Position("Toktar", "Aubakirov", "Austronaut", 129999, 34998)
print(worker_1.get_full_name())
print(worker_1.position)
print(worker_1.get_full_profit())
