"""
Code Challenge
  Name: 
    Supermarket
  Filename: 
    supermarket.py
  Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User  
  Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
  Input:
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30
  Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20

"""

from collections import OrderedDict

# take items from user as input
user_input = input("Enter items with values : ")

# make items list from splitting user_input with "\n"
items_list = user_input.split("\n")

# make Object of OrderDict
od = OrderedDict()

for each_item in items_list:
    
    # use split function to get item's price value
    data = each_item.split(" ")
    price = data[-1]
    
    # join rest string which is item name
    item = " ".join(data[:-1])
    
    # Adding and updating price of the item using orderdict function 
    od[item] = od.get(item,0) + int(price)

for k,v in od.items():
    print (k,v)