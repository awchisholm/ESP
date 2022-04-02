import pandas as pd
import datetime
import matplotlib.pyplot as plt

def profit_loss_menu():
    flag = True
    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show profit/loss for specific products")
        print("2. Show profit/loss for all products")
        print("###############################################")

        profit_loss_choice = input("Please enter the number of your choice (1-2): ")

	      # This code tries to convert the input into an int
	      # if it fails, the except: path is executed, otherwise the else path
        try:  
            int(profit_loss_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(profit_loss_choice) < 1 or int(profit_loss_choice) > 2:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(profit_loss_choice) 

def get_product_choice():
    flag = True
    while flag:
        print("######################################################")
        print("Please choose a product from the list:")
        print("Please enter the number of the product (1-16)")
        print("1.  Potatoes")
        print("2.  Carrots")
        print("3.  Peas")
        print("4.  Lettuce")
        print("5.  Onions")
        print("6.  Apples")
        print("7.  Oranges")
        print("8.  Pears")
        print("9.  Lemons")
        print("10. Limes")
        print("11. Melons")
        print("12. Cabbages")
        print("13. Asparagus")
        print("14. Broccoli")
        print("15. Cauliflower")
        print("16. Celery")
        print("######################################################")

        product_list = ["Potatoes", "Carrots", "Peas", "Lettuce", "Onions", 
"Apples", "Oranges", "Pears", "Lemons", "Limes","Melons", "Cabbages", 
"Asparagus", "Broccoli", "Cauliflower", "Celery"]

        product_choice = input("Please enter the number of your choice (1-16): ")
	      # This checks the input is an integer
        try:
            int(product_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(product_choice) < 1 or int(product_choice) > 16:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                product_name = product_list[int(product_choice)-1]
                return product_name

def get_start_date():
    flag = True
    while flag:
        start_date = input('Please enter start date for your time range (DD/MM/YYYY) ')
        # This checks the start date is a valid date
        try:
           pd.to_datetime(start_date, dayfirst=True)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            start_date_return = pd.to_datetime(start_date, dayfirst=True)
            if (pd.isnull(start_date_return) == True):
                print("Sorry, you did not enter a valid date")
                flag = True
            else:
                return start_date_return

def get_end_date():
    flag = True
    while flag:
        end_date = input('Please enter end date for your time range (DD/MM/YYYY) ')
        # This checks the end date is a valid date
        try:
           pd.to_datetime(end_date, dayfirst=True)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            end_date_return = pd.to_datetime(end_date, dayfirst=True)
            if (pd.isnull(end_date_return) == True):
                print("Sorry, you did not enter a valid date")
                flag = True
            else:
                return end_date_return

def do_plotting(dataframe):
    summary = dataframe.groupby(['Supplier', 'Date'])[['Profit subtotal', 'KGs Sold']].sum().reset_index()
    suppliers = summary.groupby('Supplier')
    fig, ax = plt.subplots()
    for name, supplier in suppliers:
        ax.plot(supplier['Date'], supplier['Profit subtotal'], label=name)
    ax.legend()
    plt.xticks(rotation=90)
    plt.show()

def get_date_range_all():
    # df1 is a pandas data frame being created from a csv file
    df1 = pd.read_csv("Task4a_data.csv") 
    print(df1.columns)

    df1["Date"] = pd.to_datetime(df1["Date"], dayfirst=True) # convert Date column to be a datetime object

    # This selects all the rows between the dates and removes the Supplier column completely
    # results is another data frame
    results = df1.loc[(df1["Date"] >= start_date) & (df1["Date"] <= end_date)].copy()
    
    # Calculate some new columns from existing columns
    results["Cost Subtotal"] = results["KGs Purchased"] * results["Purchase Price"]
    results["Sales subtotal"] = results["KGs Sold"] * results["Selling Price"]
    results["Profit subtotal"] = results["Sales subtotal"] - results["Cost Subtotal"]
    
    total = round(results["Profit subtotal"].sum(),2)
    # This sorts the date in order
    results.sort_values('Date', inplace=True)

    # The to_string function just makes the Pandas data frame look nice
    # without the index (index = False)
    results_print = results.to_string(index=False)
    print(results_print)

    # The format function is just a convenient way to make a string to print out
    # Anything between the {} is replaced with the value of the variables that are passed to the string
    print("The overall profit/loss for the selected time frame was £{}".format(total))

    do_plotting(results)

def get_date_range_product():
    product_name = get_product_choice()
    # df2 is a pandas data frame from the complete csv file
    df2 = pd.read_csv("Task4a_data.csv") 

    df2["Date"] = pd.to_datetime(df2["Date"], dayfirst=True) # convert Date column to be a datetime object

    # This selects all the rows in the data frame between the dates and for the chosen product 
    # and makes a new data frame called product_results
    product_results = df2.loc[(df2["Date"] >= start_date) & (df2["Date"] <= end_date) & (df2["Product"] == product_name)].copy()

    # Calculate some new columns from existing columns
    product_results["Cost Subtotal"] = product_results["KGs Purchased"] * product_results["Purchase Price"]
    product_results["Sales subtotal"] = product_results["KGs Sold"] * product_results["Selling Price"]
    product_results["Profit subtotal"] = product_results["Sales subtotal"] - product_results["Cost Subtotal"]
    
    total = round(product_results["Profit subtotal"].sum(),2)
    # The to_string function just makes the Pandas data frame look nice
    results_print = product_results.to_string(index=False)
    
    print(results_print)
    # The format function is just a convenient way to make a string to print out 
    # Anything between the {} is replaced with the value of the variables that are passed to the string
    print("The profit/loss for the {} for the selected time frame was £{}".format(product_name, total))

    do_plotting(product_results)


def process_menu_choice():
    if profit_choice == 1:
        get_date_range_product()
    else:
        get_date_range_all()


start_date = get_start_date()
end_date = get_end_date()
profit_choice = profit_loss_menu()
pres = process_menu_choice()