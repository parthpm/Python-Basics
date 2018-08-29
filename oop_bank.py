import datetime
class Account(object):
    '''Simple account balance class '''


    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return utc_time


    def __init__(self,name,balance):
        self._name=name
        self.__balance=balance
        self._transaction_list=[(Account._current_time(), balance)]
        print("Account created for " + self._name)
        self.show_transactions()

    def deposit(self,amount):
        if(amount>0):
            self.__balance+=amount
            self.showbalance()
            self._transaction_list.append((Account._current_time(), amount))
    def withdraw(self,amount):
        if(amount>0 and amount<self.__balance):
            self.__balance-=amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("Amount >0 and less than balance")
        self.showbalance()

    def showbalance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):

        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} ".format(amount, tran_type,date))

if __name__=='__main__':
    print(Account._current_time())


    maheshwari=Account('Maheshwari',200)
    maheshwari.showbalance()
    maheshwari.deposit(300)
    maheshwari.withdraw(400)
    maheshwari.show_transactions()
    print('\n\n')

    parth=Account('Parth',0)
    print(parth.__dict__) #adding _ before  Account__balance so we cant change it but we canchange it by
                            # _Account__balance=something
    parth.showbalance()
    parth.deposit(10000)
    parth.withdraw(900)
    parth.__balance=9900 # we are able to change the balance
    parth.withdraw(10000)
    parth.show_transactions()

