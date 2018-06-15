from random import *
from time import *
from colorama import Fore, Back, Style,init
seed(clock())
init()
i = 0
hp = 100
while 1:
	a = randrange(3)
	if a==1:
		print('Вы видите запустевший склеп')
		q = int(input('1 - обыскать\n 2 - уйти\n3 - Покинуть мир'))
		if q ==1:
			print('Вы нашли ржавый меч')
		elif q==3:
			break
	elif a==2:
		print('Вы видите магическое дерево')
		q = int(input('1 - Поговорить\n 2 - уйти'))
		if q ==1:
			print(Back.RED+Fore.GREEN+'Дерево дало вам силы'+Style.RESET_ALL)
		elif q==3:
			break
	elif a==0:
		print(Fore.GREEN+'Вы видите орка'+Style.RESET_ALL)
		q = int(input('1 - Ударить\n 2 - Сбежать'))
		if q ==1:
			health = health - 10
			print('Орк ударил вас, ваши жизни ',health)
			print('Вы убили орка и получили 10 опыта')
		elif q==3:
			break
	i = i+1
print('Game over')


if d ==3:
	if '' in inventory:
		i = 0
		for x in inventory:
			if x=='':
				inventory[i]='меч'
				break
			i+=1
	else:
		print('Нет места в инвентаре')

i=0
for x in inventory:
	print(i,' '+x)
a = int(input('Какой предмет хотите использовать'))
if inventory[a] =='зелье силы':
	power +=10


