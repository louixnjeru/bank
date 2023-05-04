import hashlib
from datetime import date

class Validators:
    
    def __init__(self):
        pass
    
    def printErrorMessage(self,message='',attempts=False):
        if attempts:
            print('ERROR - Too Many Attempts')
        else:
            print(f'ERROR - Incorrect {message.upper()} Entered')
    
    def validatePin(self,pin):           
        for i in range(3):
            try:
                pinEntry = int(input('Enter your PIN: '))
            except ValueError:
                self.printErrorMessage(message='pin')
                continue
            validationAttempt = hashlib.sha256((str(pinEntry)+pin[0]).encode()).hexdigest()
            if validationAttempt == pin[1]: return True
            self.printErrorMessage(message='pin')
        
        self.printErrorMessage(attempts=True)
        return False
    
    def validateCVV(self,cvvHash,expYear,expMonth,primaryAccountNum,serviceCode=201):
        for i in range(3):
            try:
                cvvEntry = int(input('Enter your CVV: '))
            except ValueError:
                self.printErrorMessage(message='cvv')
                continue
            if cvvEntry == cvvHash[1]: return True
            self.printErrorMessage(message='cvv')
        
        self.printErrorMessage(attempts=True)
        return False
    
    def validateExpiryDate(self,expiryDate):
        return date.today() <= expiryDate

