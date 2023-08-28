# noodles
noodles1 = ['egg noodles', 'instant noodles']
noodles2 = ['ramen', 'vermicelli',]
noodles3 = ['udon', 'soba']
noodles_list = noodles1 + noodles2 + noodles3

# soup
soup1 = ['miso']
soup2 = ['spicy','sour & spicy','sweet sour & spicy']
soup3 = ['tomato']
soup4 = ['fish']
soup5 = ['curry', 'beef']
soup_list = soup1 + soup2 + soup3 + soup4 + soup5

# ingredients
ingredients1 = ['lettuce', 'pak choi', 'cabbage']
ingredients2 = ['ham','mushrooms']
ingredients3 = ['shitake mushrooms','chicken breast', 'pork', 'duck breast']
ingredients4 = ['beef', 'tofu', 'fish tofu']
ingredients5 = ['prawns', 'squid']
ingredients_list = ingredients1 + ingredients2 + ingredients3 + ingredients4 + ingredients5

# naming variables
noodles_price = 0
soup_price = 0
ingredients1_price = 0
ingredients2_price = 0
ingredients3_price = 0
price = 0

order_list = []
price_list = []

# ordering
print('-----------------------------------------')
print('--  Hello, welcome to My Noodle Shop!  --')
print('-----------------------------------------')
print()

# noodles
try:
    print('1. Please choose your noodle: ')
    print(noodles_list)
    noodles_preference = input().lower()
    if noodles_preference in noodles_list:
        if noodles_preference in noodles1:
            noodles_price = 4
        elif noodles_preference in noodles2:
            noodles_price = 5
        elif noodles_preference in noodles3:
            noodles_price = 6
        price_list.append(noodles_price)
        
        print()
        print('2. Please choose your soup:')
        print(soup_list)
        soup_preference = input().lower()
        if soup_preference in soup_list:
            if soup_preference in soup1:
                soup_price = 0
            elif soup_preference in soup2:
                soup_price = 0.5
            elif soup_preference in soup3:
                soup_price = 0.8
            elif soup_preference in soup4:
                soup_price = 1
            elif soup_preference in soup5:
                soup_price = 1.2
            price_list.append(soup_price)
            
            print()
            print('3. Please choose your first ingredient:')
            print(ingredients_list)
            ingredients1_preference = input().lower()
            if ingredients1_preference in ingredients_list:
                if ingredients1_preference in ingredients1:
                    ingredients1_price = 0.5
                elif ingredients1_preference in ingredients2:
                    ingredients1_price = 0.8
                elif ingredients1_preference in ingredients3:
                    ingredients1_price = 1
                elif ingredients1_preference in ingredients4:
                    ingredients1_price = 1.2
                elif ingredients1_preference in ingredients5:
                    ingredients1_price = 1.5
                order_list.append(ingredients1_preference)
                price_list.append(ingredients1_price)

                print()
                print('4. Do you want additional ingredients? (y/n)')
                ingredients2_choice = input().lower()
                if ingredients2_choice == 'y':
                    print()
                    print('5. Please choose your second ingredient:')
                    print(ingredients_list)
                    ingredients2_preference = input().lower()
                    if ingredients2_preference in ingredients_list:
                        if ingredients2_preference in ingredients1:
                            ingredients2_price = 0.5
                        elif ingredients2_preference in ingredients2:
                            ingredients2_price = 0.8
                        elif ingredients2_preference in ingredients3:
                            ingredients2_price = 1
                        elif ingredients2_preference in ingredients4:
                            ingredients2_price = 1.2
                        elif ingredients2_preference in ingredients5:
                            ingredients2_price = 1.5
                        order_list.append(ingredients2_preference)
                        price_list.append(ingredients2_price)
                                        
                        print()
                        print('6. Do you want additional ingredients? (y/n)')
                        ingredients3_choice = input().lower()
                        if ingredients3_choice == 'y':
                            print()
                            print('7. Please choose your third ingredient:')
                            print(ingredients_list)
                            ingredients3_preference = input()
                            if ingredients3_preference in ingredients_list:
                                if ingredients3_preference in ingredients1:
                                    ingredients3_price = 0.5
                                elif ingredients3_preference in ingredients2:
                                    ingredients3_price = 0.8
                                elif ingredients3_preference in ingredients3:
                                    ingredients3_price = 1
                                elif ingredients3_preference in ingredients4:
                                    ingredients3_price = 1.2
                                elif ingredients3_preference in ingredients5:
                                    ingredients3_price = 1.5
                                order_list.append(ingredients3_preference)
                                price_list.append(ingredients3_price)
                            else:
                                raise Exception
                        elif ingredients3_choice == 'n':
                            ingredients3_price = 0
                            price_list.append(ingredients3_price)
                        else:
                            raise Exception
                    else:
                        raise Exception
                elif ingredients2_choice == 'n':
                        ingredients2_price = 0
                        price_list.append(ingredients2_price)
                else:
                    raise Exception
            else:
                raise Exception
        else:
            raise Exception
    else:
        raise Exception
    price = round(sum(price_list),2)
    print()
    print ('----------------------RECEIPT----------------------')
    ingredients = ', '.join(order_list)
    order = (soup_preference + ' ' + noodles_preference + ' with' + ' ' + ingredients)
    print ('Order: ', order.title())
    print ('Price: £', price)   
except:
    print ()
    print ('An error occured. Please order again.')

finally:
    print ('---------------------------------------------------')
    print ('Thank you for using our food ordering system!')
    print ('---------------------------------------------------')

