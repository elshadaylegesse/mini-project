
# full_ice_menu = []
# with open('../data/products.txt', 'r') as f:
#     for flavour in f.readlines():
#         full_ice_menu.append(flavour.rstrip())
#     print(full_ice_menu)

# with open('../Mini Projects/couriers.txt', 'r'):
#     pass


from os import name


main_page = ['0) Save your changes to the text files and EXIT the app',  '1) Product page', '2) Courier page']
#user_input = input('Insert the number your choice here  ')
product_page = ['1. See full gelato menu ', '2. Add a new flavour ', '3. Update an existing product ', '4. Delete a product', '5. EXIT APP']
courier_page= ['0) Return to main menu, 1) See couriers list, 2) Add a new courier to the list, 3) Replace a courier, 4) Delete a courier from the list']
#product_input = input('Select one of the options listed ')
full_ice_menu = ['Chilli Chocolate', 'Mango', 'Hazlenut', 'Lemon and Poppy Seeds', 'Jam-Packed', 'Dark Chocolate', 'Triple Chocolate', 'Vanilla', 'Strawberry', 'Oreo', 'Pecan Caramel', 'Peanut Crunch', 'Sea Salt Caramel']



def main_menu():  
    print(main_page)
    user_input = input('Insert the number your choice here  ')  
    if user_input == '0':  
        save_p_c() 
    elif user_input == '1':
        product_menu()    
    elif user_input == '2':
        courier_menu()      


def save_p_c():
    with open('products.txt', 'w') as product_file:
        
        for flavour in full_ice_menu:
                product_file.write(flavour, '\t')

    with open('couriers.txt', 'w') as courier_file:
        for name in courier_list:
                courier_file.write(name, '\t')

        
###PRODCUTS MENU  

def product_menu():
    print(product_page)
    product_input = input('Select one of the options listed ')

            
    if product_input == '0':
        main_menu()
        
    elif product_input == '1':
        print(full_ice_menu)
        product_menu()
            
    elif product_input == '2':
        create_flavour = str(input('Insert name of new flavour   '))
        full_ice_menu.append(create_flavour)
        print(full_ice_menu[-1])
        product_menu()
            
    elif product_input == '3':
        for (i, flavour) in enumerate(full_ice_menu, start=0):
            print(i, flavour)
        old_flavour = input('Type in number to be replaced')
        full_ice_menu[old_flavour] = int(input('What is your update?'))
        print(full_ice_menu)

    elif product_input == '4':
        print('Delete a flavour from the list below.')
        for (i, flavour) in enumerate(full_ice_menu, start=0): 
            print(i, flavour) 
        delete_flavour = int(input('Type in number to be deleted'))
        del full_ice_menu[delete_flavour]  

    

####couriers menu
def courier_menu():
    print(courier_page)
    courier_input = input('Select one of the options listed ')
    
    if courier_input == 0:
        main_menu()
        
    elif courier_input == '1':
        print(courier_list)
        courier_menu()
            
    elif courier_input == '2':
        new_name = str(input('Insert name of new courier  '))
        courier_list.append(new_name)
        print(courier_list[-1])
        courier_menu()
            
    elif courier_input == '3':
        for (i, name) in enumerate(courier_list, start=0):
            print(i, name)
        old_name = input('Type in number to be replaced')
        courier_list[old_name] = int(input('What is your update?'))
        print(courier_list)

    elif courier_input == '4':
        print('Delete a name from the list below.')
        for (i, name) in enumerate(courier_list, start=0): 
            print(i, name) 
        delete_name = int(input('Type in number to be deleted'))
        del courier_list[delete_name]  



main_menu() 
    
    
    
    