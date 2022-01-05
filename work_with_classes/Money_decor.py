class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, value):
        if isinstance(value, int) and value > 0:
            self.total_cents = value * 100 + self.total_cents % 100
        else:
            print('Wrong input')

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, value):
        if isinstance(value, int) and value < 100:
            self.total_cents = self.total_cents - self.total_cents % 100 + value
        else:
            print('Wrong input')

    def __str__(self):
        return f'Ваше состояние составляет {self.total_cents // 100} долларов {self.total_cents % 100} центов.'

    def __repr__(self):
        return f'Object class money'