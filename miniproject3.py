import json 
import csv


full_ice_menu = []
with open('products.txt', 'r') as f:
    for flavour in f.readlines():
        full_ice_menu.append(flavour.rstrip())
    #print(full_ice_menu)

couriers_list=[]
with open('couriers.txt', 'r') as c:
    for name in c.readlines():
        couriers_list.append(name.rstrip())
    #print(couriers_list)
    
#My Pages
print("Welcome to the Soho Gelateria")
main_page = ['0) Save your changes to the text files and EXIT the app\n', '1) Product page\n', '2) Courier page', '3) Orders Dictionary']
product_page = ['0) Return main menu', '1. See full gelato menu', '2. Add a new flavour ', '3. Update an existing product ', '4. Delete a product  ', '5. EXIT APP']
courier_page= ['0) Return to main menu', '1) See couriers list', '2) Add a new courier to the list', '3) Replace a courier ', '4) Delete a courier from the list']
order_page = ['0) Return to main menu', '1) See orders dictionary ', '2) Insert new customer order details ', '3)Update an existing status ', '4) Update an exisitng order ', '5)\Delete a courier ']
order_status = ['pending']

print('\n')

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
def save_p_c():
    
    with open('products.txt', 'w') as product_file:
        for flavour in full_ice_menu:
                product_file.write(flavour, '\t')

    with open('couriers.txt', 'w') as courier_file:
        for name in couriers_list:
                courier_file.write(name, '\t')

        
#PRODucTS MENU  

def product_menu():
    print(product_page)
    product_input = input('Select one of the options listed ')

            
    if product_input == '0':
        main_menu()
        
    elif product_input == '1':
        print(full_ice_menu)
        return product_menu()
            
    elif product_input == '2':
        #for flavour in full_ice_menu: 
            create_flavour = str(input(f'Insert name of new flavour:   '))
            full_ice_menu.append(create_flavour)
            print(full_ice_menu[-1])
            return product_menu()
            
    elif product_input == '3':
        for (i, flavour) in enumerate(full_ice_menu, start=0):
            print(i, flavour)
        old_flavour = int(input('Type in number to be replaced'))
        
        if old_flavour <= len(full_ice_menu):
            full_ice_menu[old_flavour] = input('What is your update?')
            print(full_ice_menu[old_flavour])
        else:
            print('Invalid number- Please select a flavour from the menu.')
                
        return product_menu()
        

    elif product_input == '4':
        print('Delete a flavour from the list below.')
        for (i, flavour) in enumerate(full_ice_menu, start=0): 
            print(i, flavour) 
        delete_flavour = int(input('Type in number to be deleted'))
        del full_ice_menu[delete_flavour]  
        
        return product_menu()

    

####couriers menu
def courier_menu():
    print(courier_page)
    courier_input = input('Select one of the options listed ')
    
    if courier_input == '0':
        main_menu()
        
    elif courier_input == '1':
        print(couriers_list)
        return courier_menu()
            
    elif courier_input == '2':
        new_name = str(input('Insert name of new courier  '))
        couriers_list.append(new_name)
        print(couriers_list[-1])
        return courier_menu()

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
        
        return courier_menu()

    elif courier_input == '4':
        print('Delete a name from the list below.')
        for (i, name) in enumerate(couriers_list, start=0): 
            print(i, name) 
        delete_name = int(input('Type in ID number of courier to be deleted'))
        del couriers_list[delete_name]  
        return courier_menu()



####Order menu

def read_orders_json(): 
    orders = []
    global orders
    with open ("orders.json") as ordersf:
        #current_orders = ordersf.read()
        #print(current_orders)
        current_orders = json.load(ordersf)
        #order.close()
        orders.append(current_orders)      
        print(orders)

    
    
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
    for orders in read_orders_json():
        if new_customer.copy() == True:
            orders.append(new_customer)
            with open ('Mini Projects\orders.json', 'w') as ordersf:
                for new_customer in orders:
                    ordersf.write(f'{new_customer}\n')


def update_order():
    orders = read_orders_json()
    
    for orders in read_orders_json():
        for (i, order) in enumerate(orders):
            print(i, order)
        
        for customer_id in orders:
            customer_id = int(input('Please input the customer id of the order you would like to update:  '))
        
            if customer_id > len(orders):
                print('This user_id is invalid')
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
                            elif new_update == 2:
                                new_street_name = str(input('Enter new street name: '))
                                #orders["customer address"["street name"]] = new_street_name
                                orders["customer address"].update({"street name" : new_street_name}) 
                            
                            elif new_update == 3:
                                new_city = str(input('Enter your new city: '))
                                #orders["customer address"["City"]] = new_city
                                orders["customer address"].update({"City" : new_city}) 
                            
                            elif new_update == 4:
                                new_postcode = str(input('Enter new postcode: '))
                                #orders["customer address"["Postcode"]] = new_postcode
                                orders["customer address"].update({"Postcode" : new_postcode}) 
                            
                            elif new_update == 5:
                                new_country = str(input('Enter new country: '))
                                #orders["customer address"["Country"]] = new_country
                                orders["customer address"].update({"Country" : new_country}) 
                            
                            else:
                                pass
                                                        
                            
                        print('The customer address for ' + orders[customer_id]["customer name"] + f'has been updated to {orders["customer address"]}')
            
                    
                    elif change_field == 3:
                        new_update = input('Update with new number:')
                        orders["Phone number"] = new_update
                        print('The customer phone number for ' + orders[customer_id]["customer name"] + f'has been updated to {new_update}')
                    
                    
                    elif change_field == 4:
                        print(couriers_list)
                        new_update = input('Update with new courier from list above:')
                        orders["Courier"] = new_update
                        print('The courier for ' + orders[customer_id]["customer name"] + f'has been updated to {new_update}')
                    
                    
                    elif change_field == 5:
                        new_update = input('Update order status: ')
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


def del_courier():
    orders = read_orders_json()
    customer_id = input('Please input the customer id of the order you would like to update:  ')
    del orders[customer_id]["Couriers"]
    print(orders[customer_id])
    
        
    
def orders_menu():
        
    print(order_page)
    order_input = input('Select one of the options listed ')
    
    if order_input == '0':
        return main_menu()

    elif order_input == '1':
        print('Your Orders are listed below')
        read_orders_json()
    
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
    
main_menu()























































orders = [{
"order_details":       
{"customer name" : "Vinnie",
"customer address" : {
    "house number" : 22,
    "street name " : "Kings Road",
    "City" : "Woodford",
    "Postcode" : "IG8 4JH",
    "Country" : "United Kingdom"},
"customer phone" : "07931538222",
"courier" : 'gtsrgrt',
"order status" : "Preparing"
},

"customer name" : "Frannie",
"customer address" : {
    "house number" : 62,
    "street name " : "Mullens Road",
    "City" : "Brixton",
    "Postcode" : "SW16 5BV",
    "Country" : "United Kingdom"},
"customer phone" : "07991726388",
"courier" : 'gdjhcfgbdjs',
"order status" : "Preparing"
},

{
"customer name" : "Jemima",
"customer address" : {
    "house number" : 313,
    "street name " : "Yoxley Avenue",
    "City" : "Ilford",
    "Postcode" : "IG8 2BF",
    "Country" : "United Kingdom"},
"customer phone" : "07911927110",
"courier" : 'null',
"order status" : "Preparing"
},
{
"customer name" : "Telisha",
"customer address" : {
    "house number" : 5,
    "street name " : "Evering Road",
    "City" : "Clapton",
    "Postcode" : "E6 9TV",
    "Country" : "United Kingdom"},
"customer phone" : "07727910508",
"courier" : 'null',
"order status" : "Preparing"
},
{
"customer name" : "Jonathon",
"customer address" : {
    "house number" : 19,
    "street name " : "Church Avenue",
    "City" : "Chelsea",
    "Postcode" : "SW8 2FS",
    "Country" : "United Kingdom"},
"customer phone" : "07822012890",
"courier" : 'null',
"order status" : "Preparing"
}]

