#Diego Espinola
#03.25.2020
#assignment 8
from stackandqueue import Stack
from stackandqueue import Queue

x = input("Welcome,this program will help you to report  your profits and losses at the end of the year.Click "
          "enter to continue \n>")

total_stock_qty= 0
total_profit= 0.0
total_bought = 0.0
total_sold = 0.0
portfolio = []
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

    while choice != 6 :
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
                portfolio.append(name)
                stock_qty.push(qty)
                stock_price.push(price)
                stock_value = qty * price
                total_bought += stock_value
                total_stock_qty += qty
                print(f'Your stocks have been added to your portfolio')

            elif choice == 2:
                name = input("What company stock do you want to sell?/ \n >")
                qty_needed = int(input("How many shares are you trying to sell? \n >"))
                if qty_needed > total_stock_qty :
                    print(f"You do not have enough stocks to sell")
                else:
                    total_popped = 0
                    total_sale = 0.0

                    qty_popped = stock_qty.pop()
                    total_stock_qty -= qty_popped
                    price = stock_price.pop()
                    total_sale += (qty_popped * price)
                    total_popped += qty_popped
                    while total_popped < qty_needed:
                        qty_popped = stock_qty.pop()
                        total_stock_qty-= qty_popped
                        price = stock_price.pop()
                        total_sale += (qty_popped *price)
                        total_popped += qty_popped
                    if total_popped > qty_needed:
                        overage = total_popped - qty_needed
                        stock_qty.push(overage)
                        stock_price.push(price)
                        total_stock_qty += overage
                        total_sale -=(overage * price)

                        total_sold += total_sale
                        profit_loss = total_bought - total_sold
                        total_profit = profit_loss
            elif choice == 3 :
                print(f"The total stock quantity is {total_stock_qty}")

            elif choice == 4 :
                print(f"Your profits or losses are {total_profit}")
            elif choice == 5:
                exit (f"Program closed")










