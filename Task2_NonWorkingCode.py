from datetime import datetime

# Add two products to start with
products = [['Desktop', 799.00, 5], ['Laptop A', 1200.00, 6]]  
sales = []

def stock_check():
    print("[Type, Cost, stock]")
    for product in products: 
        if product[2] == 0:
            products.remove(product)
    for product in products: 
        print(product)

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

    check_1 = False  
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

def additional_sale():
    s_check = False
    q_check = False
    remove_zero_product = False
    data1 = []
    while not s_check:
        stock_type = input("Enter the Stock Type which you want to buy: ")

        for product in products:
            if stock_type.lower() == product[0].lower():  
                s_check = True

                while not q_check:
                    s_quantity = int(input("Enter the quantity for %s which you want to buy: " % stock_type))
                    if s_quantity > product[2]:
                        print("Max available stock is: %s" % str(product[2]))
                    else:
                        product[2] = product[2] - s_quantity
                        q_check = True
                        break
        if s_check == False:
            print("Entered stock does not exist")
        if (s_check == True and q_check == True):
            data1.append(stock_type)
            data1.append(s_quantity)
            break

    return data1

def price(value):
    for product in products:
        if value[0].lower() == product[0].lower():
            cost = value[1] * product[1]  
            break
    return cost

def record_sale():
    data = []
    c_name = input("Enter Customer Name: ")
    comp_name = input("Enter Company Name: ")
    data.append(c_name)
    data.append(comp_name)
    now = datetime.now()  
    date_time = now.strftime("%d\%m\%Y")  
    data.append(date_time)
    print("Stock products are shown below")
    stock_check()
    data.append(additional_sale())
    while True:
        opt = input("Add more products? press y or n: ")
        if opt.lower() == "y":
            data.append(additional_sale())
        elif opt.lower() == "n":
            break
        else:
            print("invalid option")
    sum = 0
    sub_total = 0
    product_details = ""  # this holds details that we build it up in a loop so we can print it later
    for item in data:     # The data object is a list but it contains 1 or more other lists
        if isinstance(item, list):   # this code finds the lists inside the main list
            sum = sum + int(item[1]) # item[0] is the name of a product and item[1] is a quantity
            sub_total = sub_total + price(item)
            product_details = product_details + item[0] + " / " + str(item[1]) + " / £" + str(round(price(item),2)) + "\n"
    data.append(sub_total)
    discount = 0
    if sum >= 5:
        discount = sub_total * 5 / 100
    final_total = sub_total - discount
    data.append(final_total)

    sales.append(data)

    print(f"Customer Receipt\n\nCustomer Name:{c_name}\nCompany name: {comp_name}\nPurchase date: {date_time}\n\n")
    print(f"Products (Type/Number/Price) :\n {product_details}\n\nSubtotal: £{round(sub_total,2)}  \nDiscount: £{round(discount,2)} \n\n")
    print(f"Final Total: £{round(final_total,2)}\n")

while True:
    option = int(input("Enter 1 for Stock Check \nEnter 2 for Add Stock\nEnter 3 for Record Sale\nEnter 4 to Exit\n"))
    if option == 1:
        stock_check()
    elif option == 2:
        add_stock()
    elif option == 3:
        record_sale()
    elif option == 4:   
        break
    else:
        print("Invalid option, Select between 1 and 4")
