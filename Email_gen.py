class Email:
    def __init__(self):
        self.full_name = ''
        self.first_name = ''
        self.email = ''
        self.last_name = ''
    
    def set_full_name(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name+' '+self.last_name

    def set_first_name(self,first_name):
        self.first_name = first_name
    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name.capitalize() if self.first_name != '' else 'Please Enter Your Firstname'
    def get_last_name(self):
        return self.last_name.capitalize() if self.last_name != '' else 'Please Enter Your Lastname'
    def get_full_name(self):
        return self.get_first_name() + " "+ self.get_last_name() if self.first_name != '' and self.last_name != '' else self.get_first_name() if self.first_name == '' and self.last_name != '' else self.get_last_name() if self.last_name == '' and self.first_name != '' else self.get_first_name()+' & Lastname'
    def get_email(self):
        return self.first_name.lower()+'.'+self.last_name.lower()+'@kmitl.ac.th' if self.first_name != '' and self.last_name != '' else self.get_first_name()  if self.first_name == '' and self.last_name != '' else self.get_last_name() if self.last_name == '' and self.first_name != '' else self.get_first_name()+' & Lastname'

n = input('*** Create Email < BY KMITL > ***\nEnter Input : ')
e = Email()

for i in n.split(','):
    if i.startswith('A'):
        e.set_full_name(i.split()[1].lower(),i.split()[2].lower())
    elif i.startswith('E'):
        print("'E' -> Email :",e.get_email())
    elif i.startswith('F'):
        e.set_first_name(i.split()[1].lower())
    elif i.startswith('L'):
        e.set_last_name(i.split()[1].lower())
    elif i.startswith('SA'):
        print("'SA' -> Fullname :", e.get_full_name())
    elif i.startswith('SF'):
        print("'SF' -> Firstname :", e.get_first_name())
    elif i.startswith('SL'):
        print("'SL' -> Lastname :", e.get_last_name())
    elif i.startswith('X'):
        break
    else:
        print(f"'{i}' is Invalid Input !!!")
        break
    