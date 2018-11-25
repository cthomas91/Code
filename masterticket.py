SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100



def calculate_price(number_of_tickets):

    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    user_name = input("Enter Name")
    num_tickets = input("How many tickets would you like to purchase, {}? ".format(user_name))
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Not a Vaild Input. Please try again".format(err))
    else:
        amount_due = calculate_price(num_tickets)
        print("The total due is ${}".format(amount_due))
        proceed = input("Would you like to confirm your purchase?  Y/N  ")
        if proceed.lower() == "y":
            #TODO: Gather credit card info and process it
            print("SOLD!")
            tickets_remaining -= num_tickets
        else :
            print("Thank you, {}! ".format(user_name))
print("Sorry the tickets are all sold out!!!")
