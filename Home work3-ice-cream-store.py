## Mohsen Pourdehghan

icelist= ['ice1', 'ice2', 'ice3', 'ice4', 'ice5', 'ice6']
iceprice= [7000, 2000, 5000, 9000, 1000, 10000]

print(icelist)

for index in range(len(icelist)):
    print(f"{icelist[index]} price= {iceprice[index]}")
            

p1= input('\nhi "player 1", please choose your ice cream type: ')
p2= input('hi "player 2", you too, please choose your ice cream type: ')

index1= icelist.index(p1)
index2= icelist.index(p2)

p1_ice= iceprice[index1]
p2_ice= iceprice[index2]

print(f"""
'Player 1', you chose {p1}, your price is: {p1_ice}
'Player 2', you chose {p2}, your price is: {p2_ice}

you have to pay: {p1_ice + p2_ice}

-= Thanks for coming =-
""")

