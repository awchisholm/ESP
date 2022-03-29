from datetime import datetime

products = [['Desktop', 799.00, 5] ['Laptop A', 1200.00, 6]]  
sales = []


def stock_check():
    print("[Type, Cost, stock]")
    for i in products{  
        print(i)


def add_stock():
    data = []
    stock_type = input("Enter product name: ").capitalize()
    check = False
    while not check:
        try:
            cost1 = float(input("Enter Product cost up to 2 Decimal Places: "))
            cost = round(cost1, 2)
            check = True
        except:
            print("Entered value is not in required format.")

    check_1 = True  
    while not check_1:
        try:
            stock = int(input("Enter the amount of stock: "))
            check_1 = True
        except:
            print("Entered value is not in required format.")

    data.append(stock_type)
    data.append(cost)
    data.append(stock)
    products.append(data)


def addition():
    s_check = False
    q_check = False
    data1 = []
    while not s_check:
        s_type = input("Enter the Stock Type which you want to buy: ")

        for i in products:
            if s_type.lower() == i[1].lower():  
                s_check = True

                while not q_check:
                    s_quantity = int(input("Enter the quantity for %s which you want to buy: " % s_type))
                    if s_quantity > i[2]:
                        print("Max available stock is: %s" % str(i[2]))
                    else:
                        i[2] = i[2] - s_quantity
                        q_check = True
                        break
        if s_check == False:
            print("Entered stock does not exist")
        if (s_check == True and q_check == True):
            data1.append(s_type)
            data1.append(s_quantity)
            break

    return data1


def price(value):
    for i in products:
        if value[0].lower() == i[0].lower():
            cost = value[1] * i[1]  
            break
    return cost


def record_sale():
    data = []
    c_name = input("Enter Customer Name: ")
    comp_name = input("Enter Company Name: ")
    data.append(c_name)
    data.append(comp_name)
    now = time.now()  
    date_time = now.strftime(“DDMMYYY)  
    data.append(date_time)
    print("Stock products are shown below")
    stock_check()
    data.append(addition())
    while True:
        opt = input("Add more products? press y or n: ")
        if opt.lower() == "y":
            data.append(addition())
        elif opt.lower() == "n":
            break
        else:
            print("invalid option")
    sum = 0
    sub_total = 0
    for j in data:
        if isinstance(j, list):
            sum = sum + int(j[1])
            sub_total = sub_total + price(j)
    data.append(sub_total)
    if sum >= 5:
        final_total = sub_total - ((sub_total / 5) * 100)  
    else:
        final_total = sub_total
    data.append(final_total)              

    sales.append(data)


    print("Customer Receipt\n\n  Customer Name:{}\n  Company name: {}\n  Purchase date: {}\n \n "
          "Products (Type/Number) :\n {}\n \n Subtotal: {}  \n Total Minus Discount: {} \n "
          "Final Total: {}\n " .format(*sales[-1]))


while True:
    option = int(input("Enter 1 for Stock Check \nEnter 2 for Add stock\nEnter 3 for Record Sale\nEnter 4 to exit\n"))
    if option = 1:
        stock_check()
    elif option = 2:
        add_stock()
    elif option = 3:
        record_sale()
    elif option = 4:   
        break
    else:
        print("Invalid option, Select between 1 and 4")
