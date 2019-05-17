#OOPR-Assgn-3
#Start writing your code here
class Customer:
    def __init__(self,name,total_amount):
        self.customer_name=name
        self.bill_amount=total_amount
    def purchases(self):
        pays_bill(amount)
    def pays_bill(self,amount):
        amount=amount-amount*0.05
        self.bill_amount=self.bill-amount
        print("{0} pays bill amount of Rs. {1}".format(self.customer_name,amount))
