import collections
import card.bankCard as card
import secrets

class Person:
    
    def __init__(self,customerNumber,title,firstName,middleName,lastName,address,number,dateOfBirth):
        self.customerNumber = customerNumber
        self.title = title.upper()
        self.firstName = firstName.upper()
        self.middleName = middleName.upper()
        self.lastName = lastName.upper()
        self.accounts = collections.defaultdict(dict)
        self.phoneNumber = number
        self.address = address
        self.dateOfBirth = dateOfBirth
        
    
    def addAccount(self,sortCode,issueNum,accountType,hasOverdraft=False,initalBalance=0,overdraft=0):
        while True:
            accountNum = int(f'{secrets.randbelow(99999999):8d}')
            if accountNum not in self.accounts: break
        self.accounts[accountNum] = {
                            'sortCode': sortCode,
                            'accountNumber': accountNum,
                            'accountType': accountType,
                            'card': card(f'{self.title} {self.firstName[0]} {self.middleName[0] if self.middleName else ""} {self.lastName}'.upper(),
                                         issueNum,
                                         hasOverdraft,
                                         initalBalance,
                                         overdraft)
                              }
    def showAccounts(self):
        for i,account in enumerate(self.accounts.keys()):
            print(i)
            print(account['accountType'])
            print(account['sortCode'],account['accountNumber'])
            print(f"£{account['card'].balance}")
            print()
            