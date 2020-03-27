#Diego Espinola
#03.25.2020
#assignment 8
from stackandqueue import Stack
from stackandqueue import Queue

x = input("Welcome,this program will help you to report  your profits and losses at the end of the year.Click "
          "enter to continue \n>")

total_inventory_qty = 0
total_inventory_price = 0
price = 0
total_profit_or_losses = 0.0


choice = 0
method = 0
while method != 3:
    print("Did you use a 1)LIFO or 2)FIFO method?")
    method = int(input("1) or 2) >"))

    if method == 1:

        stock_qty= Stack()
        stock_price = Stack()

    else:
        stock_qty = Queue()
        stock_price = Queue()


    while choice != 5:
            print("Please select an option from the menu below:")
            print("1. Buy stocks")
            print("2. Sell stocks")
            print("3. View portafolio")
            print("4. See portfolio")
            print("5. Exit Program")
            choice = int(input(">"))



            if choice == 1:
                name = input("What company would you like to buy? \n >")
                qty = int(input("How many shares would you like to buy? \n >"))
                price = float(input("What's the price for each stock? \n "))
                stock_qty.push(qty)
                stock_price.push(price)
                print("Added to inventory. \n\n")

        # Keep the running total
                total_inventory_qty += qty

            elif choice == 2:
                qty_needed = int(input("How many are you looking to sell?\n>"))
                price_sold = float(input("At what price are you selling each stock?\n>"))
                if qty_needed > total_inventory_qty:
                    print("You do not have that many available for sale.\n\n")
            # This statement makes the loop start back at the menu
                    continue
                else:
                    total_popped = 0
                    total_price_popped = 0.0

            # These next 5 lines are the key to keeping track of where you are
                    qty_popped = stock_qty.pop()
                    total_inventory_qty -= qty_popped
                    price_popped = stock_price.pop()
                    total_inventory_price -= price_popped
                    total_popped += qty_popped
                    total_price_popped += price_popped
            # Keep popping until we have enough
                    while total_popped < qty_needed:
                        qty_popped = stock_qty.pop()
                        total_inventory_qty -= qty_popped
                        price_popped = stock_price.pop()
                        total_inventory_price -= price_popped
                        total_popped += qty_popped
                        total_price_popped += price_popped

            # We should have popped enough, but did we pop too many?  Push the extra back on.
                    if total_popped > qty_needed:
                        overage = total_popped - qty_needed
                        stock_qty.push(overage)
                        total_inventory_qty += overage


            # Let's calculate the profit on what we are selling and keep track of it
                    total_profit_or_losses += (total_popped * total_price_popped)
                print(f"You have successfully filled the order for {qty_needed}\n")

            elif choice == 3:
                 print(f"The total current inventory quantity is {total_inventory_qty}\n")

            elif choice == 4:
                print(f"The total profit from sales is currently ${total_profit_or_losses}\n")

