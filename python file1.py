
name_1=input("what is your name:")
name_2=input("what is your name:")
name_3=input("what is your name:")

slices_in_the_pizza=input(" how many slices in the pizza:")
Price_of_the_pizza=input(" what is the price of the pizza:")

pecentage_ate_by_person_1=input(name_1+" what percentage of pizza you ate:")
pecentage_ate_by_person_2=input(name_2+" what percentage of pizza you ate:")
pecentage_ate_by_person_3=input(name_3+" what percentage of pizza you ate:")

number_of_slices_ate_by_person_1=float(pecentage_ate_by_person_1)*float(slices_in_the_pizza)
number_of_slices_ate_by_person_2=float(pecentage_ate_by_person_2)*float(slices_in_the_pizza)
number_of_slices_ate_by_person_3=float(pecentage_ate_by_person_3)*float(slices_in_the_pizza)

price_paide_by_name_1=float(pecentage_ate_by_person_1)*float(Price_of_the_pizza)
price_paide_by_name_2=float(pecentage_ate_by_person_2)*float(Price_of_the_pizza)
price_paide_by_name_3=float(pecentage_ate_by_person_3)*float(Price_of_the_pizza)

print(name_1+" have paide "+str(number_of_slices_ate_by_person_1)+" slices and payed "+str(price_paide_by_name_1)+" $ for his meal ")
print(name_2+" have paide "+str(number_of_slices_ate_by_person_2)+" slices and payed "+str(price_paide_by_name_2)+" $ for his meal ")
print(name_3+" have paide "+str(number_of_slices_ate_by_person_3)+" slices and payed "+str(price_paide_by_name_3)+" $ for his meal ")
