def bonAppetit(bill, k, b):
    bill.remove(bill [k])
    cuenta = sum(bill)//2
    cuenta = b - cuenta

    if cuenta == 0:
        print("bon appetit")
    else:
        print(cuenta)
    
bonAppetit([3,10,9,2],1,7)