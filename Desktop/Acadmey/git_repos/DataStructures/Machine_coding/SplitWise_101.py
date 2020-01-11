from collections import defaultdict
from abc import ABC, abstractmethod

#define user class for users
class User:
    
    def __init__(self, user_id, name, phone_no = None, address=None,_amount = 0):
        if len(user_id) >0 :
            self.user_id = user_id
        else:
            raise Exception("user_id is mandatory field")
        
        if len(name)>0:
            self.name = name
        else:
            raise Exception("name is mandatory field")
        
        self.phone_no = phone_no
        self.address = address
        self._amount = _amount
        print("user added successfully")


class Transaction:
    
    def __init__(self,debitors=None, creditor=None, total_amount=None):
        self.debitors = debitors
        self.creditor = creditor
        self.total_amount = total_amount


class Expense(ABC):
    
    
    def __init__(self,name,transaction,date = None,image = None,notes = None, location = None):
        self.name = name
        self.date = date
        self.image = image 
        self.notes= notes
        self.location = location
        self.transaction = transaction
    
    @abstractmethod
    def divideExpense(self,transaction):
        pass

class EqualExpense(Expense):
    
    def divideExpense(self, transaction):
        #write code to divide amount equal
        
        each_contribution = int(transaction.total_amount)//(len(transaction.debitors)+1)
        for debitor in transaction.debitors:
            debtorObject = Driver.dic_user[debitor]
            debtorObject._amount -= each_contribution
        Driver.dic_user[transaction.creditor]._amount += each_contribution*len(transaction.debitors)
        return 
        
class ExactExpense(Expense):
    
    def divideExpense(self,total_amount,transaction):
        #write code to divide amount equal
        pass
    
class Driver:
    
    dic_user = defaultdict(list)
    dic_exp = defaultdict(list)
    def dashboard(self):
        while(1):
            print("press 1: To add User")
            print("press 2: To add Expenses")
            print("press 3: To Show Balance")
            print("press 4: To Exist")
            choice = input()
            
            
            if int(choice) == 1:
                print("user_id:")
                user_id = input()
                print("name:")
                name = input()
                print("phone_no:")
                phone_no = input()
                print("Address:")
                Address = input()
                user_object = User(user_id,name,phone_no,Address)
                self.dic_user[user_object.user_id] = user_object
            
            elif int(choice) == 2:
                transactionObject = Transaction()
                print("Enter name of expense")
                expense_name = input()
                print("Enter payee user_id:")
                transactionObject.creditor = input()
                print("Enter people in group ")
                transactionObject.debitors = list(input().lstrip().rstrip().split())
                print("enter amount")
                transactionObject.total_amount = input()
                
                EqualExpObj = EqualExpense(name = expense_name,transaction = transactionObject)
                EqualExpObj.divideExpense(transactionObject)
                self.dic_exp[EqualExpObj.name] = EqualExpObj
                print("transaction successfull")
                
            elif int(choice) == 3:
                self.showBalance()
                print("\n")
                
            elif int(choice) == 4:
                
                break

            
    def showBalance(self):
        
        if len(self.dic_user) == 0:
            print("no user exist")
            return
        
        for user in self.dic_user:
            print("user_id:"+str(self.dic_user[user].user_id)+" Amount:"+str(self.dic_user[user]._amount))
        
        
o_bject = Driver()
o_bject.dashboard()
#o_bject.showBalance()

        
     
    