class Zebra:
    def __init__(self,count=0):
        self.count=count
    def which_stripe(self):
        self.count+=1
        if self.count%2==0:
            print('white stripe')
        else:
            print('black stripe')