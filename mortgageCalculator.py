def loanAmount(payment):

    purchasePrice = eval(input("Enter the purchase price of the house : $"))
    downPayment = eval(input("Enter the amount of down payment: $"))
    principal = purchasePrice - downPayment
    print(f"The principal is $ {principal}")


    termLoan = eval(input("Enter the term of loan: "))
    numberPayments = termLoan * 12
    print(f"The number of payments to be made in {termLoan} years is {numberPayments}")

    annualInterestRate = eval(input("Enter the annual interest rate: "))
    monthlyInterestRate = annualInterestRate/100
    print(f"The interest rate is: {monthlyInterestRate}")

    monthlyPayment = ((principal*(monthlyInterestRate/12))/(1-((1+(monthlyInterestRate/12))**(-numberPayments))))
    #print(f"Your monthly payment is {format(payment,',.2f')}")
    return monthlyPayment

def stateRate():
    state = ['New York', 'California', 'Colorado', 'Texas',' FLorida']
    for i in range (len(state)):
        interestRate = eval(input(f"Enter interest rate: "))
        if interestRate > 5:
            print('High Interest Rate!')
        else:
            print('Great interest rate. Buy the house!')


stateRate()
