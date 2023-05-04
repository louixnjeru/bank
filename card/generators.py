import uuid
import hashlib
import secrets
from datetime import date
import calendar
from numpy import random

class Generators:
    
    def generatePin(self):
        newPin = random.randint(15000,99999)//10
        print('New PIN:',newPin)
        salt = str(uuid.uuid4())
        pinHash = hashlib.sha256((str(newPin)+salt).encode()).hexdigest()
        return [salt,pinHash]
    
    def generateCardNumber(self,issueNum):
        prelimCardNum = f'{issueNum}{secrets.randbelow(999999999):9d}'
        prelimCardNum += str(self.generateCheckDigit(prelimCardNum))
        print(prelimCardNum)
        return int(prelimCardNum)
        
    def generateCheckDigit(self,cardNum):
        sumDigits = 0
        for i in reversed(range(len(cardNum))):
            currNum = int(cardNum[i])
            if i % 2 == 0:
                tmp = currNum*2
                sumDigits += (tmp - 9) if tmp > 9 else tmp
            else:
                sumDigits += currNum
        return 10 - (sumDigits%10)
    
    def generateCVV(self,expYear,expMonth,primaryAccountNum,serviceCode=201):
        salt = str(uuid.uuid4())
        date = f'{expYear}'[-2:]+f'{expMonth:02d}'
        combined = f'{primaryAccountNum}{date}{serviceCode}{salt}'
        cvvHash = hashlib.sha256(combined.encode()).hexdigest()
        cvv = int(cvvHash,16)%900+100
        print(f'CVV2 number for card {primaryAccountNum}: ',cvv)
        return [salt,cvvHash]
    
    def generateIssueDate(self):
        return date.today()
    
    def generateExpiryDate(self,today):
        expiryMonth = calendar.monthrange(today.year+5, today.month)
        expiryDay = date(today.year+5,today.month,expiryMonth[1])
        return expiryDay
    
    def generateSortCode(self,name,postCode):
        sortCode = ""
        for i in range(3):
            for j in range(1,3):
                combined = f'{uuid.uuid4()}{j}{name}{postCode}'
                codeHash = hashlib.sha256(combined.encode()).hexdigest()
                sortCode += f'{int(codeHash,16)%10}'
            sortCode += '-'
        return sortCode[:-1]
    
    def generateIssueNumber(self,name,postCode,sortCode):
        issueNum = "4"
        for i in range(1,6):
            combined = f'{uuid.uuid4()}{i}{name}{postCode}{sortCode}'
            issueHash = hashlib.sha256(combined.encode()).hexdigest()
            issueNum += f'{int(issueHash,16)%10}'
        return issueNum
    
    def generateDate(self,day,month,year):
        return date(year,month,day)
            
        
                
                
