
def main():
    print('This program converts between pounds and dollars')
    print('')
    
  
    print('To convert dollars to pounds press "D"')
    print('To convert pounds to dollars press "P":')
    
    
    
    # Create a nested function that converts Pounds to dollars
    def Pounds():
        amount = int(input('Enter Amount: '))
        converted = amount * 1.22
        print(f'{amount} pounds : {converted} dollars')
        
        
    # Create a nested function that converts dollars to Pounds
    def Dollars():
        amount = int(input('Enter Amount: '))
        converted = amount * 0.82
        print(f'{amount} Dollars : {converted} Pounds')
        
    # Create a continous loop 
    while True:
        choice = input('P or D?: ')
        if choice.upper() ==  'P':
            Pounds()
            
        elif choice.upper() ==  'D':
            Dollars()
            
        else:
            print('Invalid answer try again')
            break
    
    

# Call the function 
main()