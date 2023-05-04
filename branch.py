import collections
import person as p
import card.generators as gen
import secrets

class BankBranch:
    
    def __init__(self,branchName,address):
        self.g = gen.Generators()
        self.branchName = branchName
        self.address = address
        self.sortCode = self.g.generateSortCode(self.branchName, self.address['Post Code'])
        self.issueNum = self.g.generateIssueNumber(self.branchName, self.address['Post Code'], self.sortCode)
        self.customers = collections.defaultdict(dict)
        
    def createPerson(self):
        while True:
            title = input('Enter Title: ').upper()
            firstName = input('Enter First Name: ').capitalize()
            middleName = input('Enter Middle Name (or Press Enter to continue): ').capitalize()
            lastName = input('Enter Last Name: ').capitalize()
            
            print()
            print("DATE OF BIRTH (DD/MM/YYYY)")
            dob = [0]*3
            for i,pos in enumerate(['DD','MM','YYYY']):
                while True:
                    try:
                        dob[i] = int(input(f"{pos}: "))
                    except ValueError:
                        continue
                    break
            print()
                
            
            while True:
                try:
                    number = int(input("Enter Contact Number: "))
                except ValueError:
                    continue
                break
            
            print()
            print("ADDRESS")
            house = input('House Number/ Flat Number: ')
            road = input("Road: ")
            town = input("Town: ")
            postcode = input("Postcode: ")
            print()
            
            print()
            print('DETAILS')
            print(f"Name: {title} {firstName} {middleName} {lastName}")
            print(f"DOB: {dob[0]}/{dob[1]}/{dob[2]}")
            print(f"Address: {house} {road}, {town}, {postcode}")
            print()
            
            ans = None
            
            while ans not in {'y','n'}:
                ans = input('Are these details correct? (y/n): ')
            
            if ans.lower() == 'y': break
        
        address = {'house': house, 'road':road, 'town':town, 'postcode':postcode}
        dateOfBirth = self.g.generateDate(dob[0],dob[1],dob[2])
        
        while True:
            cusNum = int(f'{secrets.randbelow(99999999):10d}')
            if cusNum not in self.customers: break
        
        self.customers[cusNum] = p.Person(cusNum, title, firstName, middleName, lastName, address, number, dateOfBirth)
        
    def createCard(self,customerNumber):
        if customerNumber not in self.customers:
            print('ERROR - Customer Not Found')
            return False
        
        accountType = input('Enter Account Type')
        
        overdraftChoice = None
        while overdraftChoice not in {'y','n'}:
            overdraftChoice = input('Are these details correct? (y/n): ')
        
        hasOverdraft = True if overdraftChoice == 'y' else False
        overdraft = 0
        
        if hasOverdraft:
            while True:
                try:
                    overdraft = int(input("Enter Overdraft: "))
                except ValueError:
                    continue
                break
        
        while True:
            try:
                initalBalance = int(input("Enter Inital Balance: "))
            except ValueError:
                continue
            break
        
        self.customers[customerNumber].addAccount(self.sortCode,self.issueNum,accountType,hasOverdraft,initalBalance,overdraft)
        
    def printCustomers(self):
        print("Customers at this Branch:")
        print()
        for customer in self.customers.keys():
            print(f'{customer}: {self.customers[customer].title} {self.customers[customer].firstName} {self.customers[customer].middleName} {self.customers[customer].lastName}')
        