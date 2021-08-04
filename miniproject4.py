import csv
import pprint

product_fieldnames = ['Flavour', 'Price']
order_fieldnames = ['customer name', 'customer address', 'customer phone', 'courier', 'order status']
courier_fieldnames = ['Name', 'Phone number']
    
full_ice_menu = []
def import_products_csv():
    with open('products.csv', 'r', newline = '') as p:
        csv_p = csv.DictReader(p, delimiter=',')
        for row in csv_p:
            full_ice_menu.append(row)
        pprint.pp(full_ice_menu, sort_dicts=False)
        #print(full_ice_menu)


couriers_list=[]
def import_couriers_csv():
    global couriers_list
    with open('couriers.csv', 'r', newline = '') as c:
        csv_c = csv.DictReader(c, delimiter=',')
        for row in csv_c:
            couriers_list.append(row)
        pprint.pp(couriers_list, sort_dicts=False)
        #print(couriers_list)
        
        
orders = []
def import_orders_csv(): 
    global orders
    with open('orders2.csv', 'r', newline = '') as o:
        csv_o = csv.DictReader(o, delimiter =',')
        for row in csv_o:
            orders.append(row)  
        pprint.pp(orders, sort_dicts=False) 




#My Pages
print("Welcome to the Soho Gelateria")
main_page = ['0) Save your changes to the text files and EXIT the app', '1) Product page', '2) Courier page', '3) Orders Dictionary']
product_page = ['0) Return main menu', '1. See full gelato menu', '2. Add a new flavour ', '3. Update an existing product ', '4. Delete a product  ', '5. EXIT APP']
courier_page= ['0) Return to main menu', '1) See couriers list', '2) Add a new courier to the list', '3) Replace a courier ', '4) Delete a courier from the list']
order_page = ['0) Return to main menu', '1) See orders dictionary ', '2) Insert new customer order details ', '3)Update an existing status ', '4) Update an exisitng order ', '5)\Delete a courier ']
order_status = ['pending', 'posted']


def main_menu():  
    print(main_page)
    user_input = input('Insert the number your choice here  ')  
    if user_input == '0':  
        save_p_c() 
    elif user_input == '1':
        product_menu()    
    elif user_input == '2':
        courier_menu()     
    elif user_input == '3':
        orders_menu()   
    else:
        print('Only one of the options given may be selected')  

## writing items to relevant files




def save_product_csv():
    with open('products.csv', 'a+') as product_file:
        writer = csv.Dictreader(product_file, fieldname = product_fieldnames)
        writer.writeheader()
        for flavour, price in product_file:
            writer.writerow(flavour, price)
        return import_products_csv()
        #for flavour in full_ice_menu:
                #product_file.write(flavour, '\t')


def save_courier_csv():
    with open('couriers.csv', 'a+') as courier_file:
        writer = csv.Dictreader(courier_file, fieldname = courier_fieldnames)
        writer.writeheader()
        for name ,number in courier_file:
            writer.writerow(name, number)
        return import_couriers_csv()    
        #for name in couriers_list:
            # courier_file.write(name, '\t')


def save_new_order(file_name, orders, fieldnames):
    with open('orders.csv', 'a+', newline='') as myfile: 
        writer = csv.DictWriter(myfile, fieldnames= order_fieldnames)
        for flavour, price in orders:
            writer.writerow(flavour, price)
        return import_orders_csv() 
        
        
###check this function
def save_p_c():
    with open('products.csv', 'a+') as product_file:
        for flavour in full_ice_menu:
                product_file.write(flavour, '\t')
                
    with open('couriers.txt', 'a+') as courier_file:
        for name in couriers_list:
                courier_file.write(name, '\t')
                
    
    
        
#PRODucTS MENU  

def product_menu():
    print(product_page)
    product_input = input('Select one of the options listed ')
                        
    if product_input == '0':
        main_menu()
        
    elif product_input == '1':
        for row in full_ice_menu:
            print(row[0], row[1])
        product_menu()
        #print(f"{i['name']}: £{i['price']}")    
        
    elif product_input == '2':
        create_flavour = str(input(f'Insert name of new flavour:   '))
        flavour_price = input('What is the cost of this flavour:')
        orders["Flavour"] = create_flavour
        orders["price"] = flavour_price
        a_new_order = save_new_order()
        for flavour, price in a_new_order:
            flavour = create_flavour
            price = flavour_price
            return save_new_order()
        product_menu()
        
# def add_new_order(file_name, new_flavour_price, fieldnames):
#     with open('orders.csv', 'a+', newline='') as myfile: 
#         writer = csv.DictWriter(myfile, fieldnames= order_fieldnames)
#         for flavour, price in full_ice_menu:
#             writer.writerow(new_flavour_price)
#         import_orders_csv()    

        # for flavour, price in full_ice_menu: 
        #     new_flavour = [create_flavour, flavour_price]
        #     full_ice_menu.append("")
        #     full_ice_menu
        #     print(full_ice_menu[-1])
        # product_menu()
        
    
        #for flavour in full_ice_menu: 
            # create_flavour = str(input(f'Insert name of new flavour:   '))
            # full_ice_menu.append(create_flavour)
            # print(full_ice_menu[-1])
            # product_menu()
            
    elif product_input == '3':
        for (i, flavour) in enumerate(full_ice_menu, start=0):
            print(i, flavour)
        old_flavour = int(input('Type in number to be replaced'))
        
        if old_flavour <= len(full_ice_menu):
            full_ice_menu[old_flavour] = input('What is your update?')
            print(full_ice_menu[old_flavour])
        else:
            print('Invalid number- Please select a flavour from the menu.')
            product_menu()
        

    elif product_input == '4':
        print('Delete a flavour from the list below.')
        for (i, flavour) in enumerate(full_ice_menu, start=0): 
            print(i, flavour) 
        delete_flavour = int(input('Type in number to be deleted'))
        del full_ice_menu[delete_flavour]  
        product_menu()


####couriers menu
def courier_menu():
    print(courier_page)
    courier_input = input('Select one of the options listed ')
    
    if courier_input == '0':
        main_menu()
        
    elif courier_input == '1':
        print(couriers_list)
        courier_menu()
            
    elif courier_input == '2':
        new_name = str(input('Insert name of new courier  '))
        couriers_list.append(new_name)
        print(couriers_list[-1])
        courier_menu()

    elif courier_input == '3':
        for (i, name) in enumerate(couriers_list, start = 0):
            print(i, name)
        old_name = int(input('Type in courier ID to be replaced'))
        
        if old_name <= len(couriers_list):
            couriers_list[old_name] = str(input('What is your update?'))
            print(couriers_list[old_name])
        else:
            print('Invalid ID- Please select a courier ID from the menu.')
            return old_name
        
        courier_menu()

    elif courier_input == '4':
        print('Delete a name from the list below.')
        for (i, name) in enumerate(couriers_list, start=0): 
            print(i, name) 
        delete_name = int(input('Type in ID number of courier to be deleted'))
        del couriers_list[delete_name]  
        courier_menu()



####Order menu
def new_order(): 
    new_customer = {}
    new_customer["Customer Name"] = str(input('Please enter the customer name: ')) 
    for new_address in new_customer:
        new_address = {}
        new_address["house number"] = input('Insert house number:   '),
        new_address["street name "] = str(input('Give street name:   '))
        new_address["City"] = str(input('City:   ')),
        new_address["Postcode"] = str(input('Postcode:   '))
        new_address["Country"] = str(input('Country:   '))
    new_customer["Customer Address"] = new_address
    new_customer["Customer Phone"] = input('Please type in your phone number: ')
    print(couriers_list)
    courier_id = input('Choose your courier from the list above: ')
    new_customer["Courier"] = courier_id
    new_customer["Status"] = 'Pending'
    
    print(new_customer)
    ##look here
    #for orders in import_orders_csv():
    with open ('orders.csv', 'w') as ordersf:
        nc = csv.DictWriter(ordersf, order_fieldnames)
        #nc = csv.DictWriter(ordersf, new_customer.keys())
        nc.writeheader()
        nc.writerow(new_customer)
        #orders.append(new_customer)
        #for new_customer in orders:
            #ordersf.write(f'{new_customer}\n')
    orders_menu()

def update_order():
    orders = import_orders_csv()
    
    for (i, order) in enumerate(orders):
        print(i, order)
    
    for customer_id in orders:
        customer_id = int(input('Please input the customer id of the order you would like to update:  '))
    
        if customer_id > len(orders):
            print('This user_id is invalid')
            return customer_id
        else:    #####unsure about  below
            change_order = True
            print(orders[customer_id], start=0)
            
            while change_order:

                change_field = int(input('\nWhich field would you like to update?\n'
                                            '1) customer name\n'
                                            '2) customer address\n'
                                            '3) Phone number\n'
                                            '4) Courier\n'
                                            '5) Order status\n'
                                            '6) Return to Main menu\n'))
                
                if change_field == 1:
                    new_update = input('Update with new name:')
                    orders["customer name"] = new_update
                    print('Customer name ' + orders[customer_id]["customer name"] + f'has been updated to {new_update}')
                    orders_menu()
                    
                elif change_field == 2:
                    print(orders[customer_id]["customer address"])
                    new_update = input('Insert the number of the address field you\'d like to update: ''\n'
                                        '1) house number''\n'
                                        '2) street name ''\n'
                                        '3) City ''\n'
                                        '4) Postcode'' \n'
                                        '5) Country''\n' )
                    
                    while new_update<=5 and  new_update>=1:
                        if new_update == 1:
                            new_house_number = input('New house number: ')
                            #orders["customer address"["house number"]] = new_house_number
                            orders["customer address"].update({"house number" : new_house_number}) 
                            update_order()
                            
                        elif new_update == 2:
                            new_street_name = str(input('Enter new street name: '))
                            #orders["customer address"["street name"]] = new_street_name
                            orders["customer address"].update({"street name" : new_street_name}) 
                            update_order()
                            
                        elif new_update == 3:
                            new_city = str(input('Enter your new city: '))
                            #orders["customer address"["City"]] = new_city
                            orders["customer address"].update({"City" : new_city}) 
                            update_order()
                        
                        elif new_update == 4:
                            new_postcode = str(input('Enter new postcode: '))
                            #orders["customer address"["Postcode"]] = new_postcode
                            orders["customer address"].update({"Postcode" : new_postcode}) 
                            update_order()
                        
                        elif new_update == 5:
                            new_country = str(input('Enter new country: '))
                            #orders["customer address"["Country"]] = new_country
                            orders["customer address"].update({"Country" : new_country}) 
                            update_order()
                            
                        else:
                            pass
                                                    
                    print(orders[-1])    
                    print('The customer address for ' + orders[customer_id]["customer name"] + f'has been updated to {orders["customer address"]}')
                    
                
                elif change_field == 3:
                    new_update = input('Update with new number:')
                    orders["Phone number"] = new_update
                    print('The customer phone number for ' + orders[customer_id]["customer name"] + f'has been updated to {new_update}')
                
                
                elif change_field == 4:
                    print(couriers_list)
                    new_update = str(input('Update with new courier from list above:'))
                    orders["Courier"] = new_update
                    print('The courier for ' + orders[customer_id]["customer name"] + f'has been updated to {new_update}')
                
                
                elif change_field == 5:
                    new_update = str(input('Update order status: '))
                    orders["Order status"] = new_update
                    print(f'Order status has been updated to {new_update}')
                
                
                elif change_field == 6:
                    return main_menu()
                
                else:
                    print('Invalid Selection, try again')
                    return update_order()

    
#update existing order status
def update_status():
    
    customer_id = int(input('Please input the customer id of the order you would like to update:  '))
    print(orders[customer_id])
    for status in orders[customer_id]:
        new_update = input('Update order status: ')
        orders["Order status"] = new_update
    print(f'Order status has been updated to {new_update}')
    orders_menu()

def del_courier():
    orders = import_orders_csv()
    customer_id = input('Please input the customer id of the order you would like to update:  ')
    del orders[customer_id]["Couriers"]
    print(orders[customer_id])
    orders_menu()
        
    
def orders_menu():
        
    print(order_page)
    order_input = input('Select one of the options listed ')
    
    if order_input == '0':
        return main_menu()

    elif order_input == '1':
        print('Your Orders are listed below')
        import_orders_csv()
    
    elif order_input == '2':
        return new_order()
    
    elif order_input == '3':
        return update_status()
    
    elif order_input == '4':
        return update_order()
    
    elif order_input == '5':
        return del_courier()   
    
    else: 
        return IndexError


import_couriers_csv()
import_orders_csv()
import_products_csv()
main_menu()


    
    
    
    

    
    
    





































