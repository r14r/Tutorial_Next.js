## bankkonto-klasse
class BankKonto:
    def __init__(self, besitzer, stand=0):
        self.besitzer = besitzer
        self.stand = stand

    def einzahlen(self, betrag):
        self.stand += betrag

    def anzeigen(self):
        print(f"{self.besitzer} hat {self.stand} Euro")

acc = BankKonto("Alice", 100)
acc.einzahlen(50)
acc.anzeigen()
