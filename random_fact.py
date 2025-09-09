from random import choice
from hundred_facts import random_facts
from time import sleep

def fact_generator(random_facts):
	print('\033[1m----------Fact finder activated----------\033[0m')
	sleep(1)
	print('\033[33m*Bzzzt*\033[0m')
	sleep(1)
	print('\033[36mEngaging the Random Fact-o-Matic 3000.\033[0m', end = '\r')
	sleep(1)
	print('\033[36mEngaging the Random Fact-o-Matic 3000..\033[0m', end = '\r')
	sleep(1)
	print('\033[36mEngaging the Random Fact-o-Matic 3000...\033[0m')
	sleep(1)
	fact = choice(random_facts)
	return fact
	
fact_info = (fact_generator(random_facts))

print(f'\033[35m{fact_info}\033[0m')

