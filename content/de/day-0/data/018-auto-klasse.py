## auto-klasse
class Auto:
    def __init__(self, marke, benzin=100):
        self.marke = marke
        self.benzin = benzin

    def fahren(self):
        if self.benzin > 0:
            self.benzin -= 10
            print(f"{self.marke} fährt!")
        else:
            print("Kein Benzin!")

    def tanken(self):
        self.benzin = 100
        print(f"{self.marke} vollgetankt.")
