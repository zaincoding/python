

class Bank:
    bank_name = 'Habib'
    @classmethod
    def change_bank_name(cls, name):
            cls.bank_name = name
            return cls
    
    def display(self):
        print(f"Bank Name: {self.bank_name}")


bank = Bank()

print(bank.bank_name)


bank.change_bank_name('Meezain')

bank.display()
