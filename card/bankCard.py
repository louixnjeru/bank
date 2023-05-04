import generators as gen
import validators as val

class BankCard:
    
    def __init__(self,cardholder,issueNum,hasOverdraft=False,initalBalance=0,overdraft=0):
        self.generator = gen.Generators()
        self.validator = val.Validators()
        self.cardholder = cardholder
        self.hasOverdraft = hasOverdraft
        self.balance = initalBalance
        self.overdraft = overdraft
        self.pin = self.generator.generatePin()
        self.issueDate = self.generator.generateIssueDate()
        self.expiryDate = self.generator.generateExpiryDate(self.issueDate)
        self.cardNumber = self.generator.generateCardNumber(issueNum)
        self.cvvHash = self.generator.generateCVV(self.expiryDate.year, self.expiryDate.month, self.cardNumber)
        
    def getBalance(self):
        return self.balance
    
    def withdraw(self,amount):
        if self.validator.validateExpiryDate(self.expiryDate) and self.validator.validatePin(self.pin) and amount >= self.balance+self.overdraft:
            self.balance -= amount
        
    def deposit(self,amount):
        if self.validator.validateExpiryDate(self.expiryDate):
            self.balance += amount
        
    def updateOverDraft(self,amount=0):
        if amount == 0: self.hasOverdraft = False
        self.overdraft = amount
    
    def resetPin(self):
        self.pin = self.generator.generatePin()
        
    def makeOnlinePayment(self,amount):
        if self.validator.validateExpiryDate(self.expiryDate) and self.validator.validateCVV(self.cvvHash) and amount >= self.balance+self.overdraft:
            self.balance -= amount
    
    
    
    
    
    