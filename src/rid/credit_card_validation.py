import re

def credit_card_validator(c):
   if c.count("-")>0:
        a = c.split("-")
        p = 1
        if len(a)!=4:
            p=None
            a=[]
        for b in a:
            if len(b)!=4:
               p=None
               break
            else:
               p = re.search("[456][0-9]{15}",c)
            c = c.replace("-"," ")
            q = re.search(".*([0-9])\1{3}.*",c)

            if p!=None and q==None:
               return False
            else:
               return True

c = "5423-2578-8632-658"
print(credit_card_validator(c))


