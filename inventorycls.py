class Remote:
    #Initializing a model num - (str), description - (str), remote list - (list)
    def __init__(self, model_num, des, rem=None):
        self.model_num = model_num
        self.des = des
        if rem is None:
            self.rem = []
        else:
            self.rem = rem
    
    def add_model(self):
        if self.model_num not in self.rem:
            self.rem.append(self.model_num)
            return self.rem



remote_1 = Remote("#0","Remote for Monti")
remote_2 = Remote("#01", "Remote for Tower")
print(remote_1.add_model())
print(remote_2.add_model())       