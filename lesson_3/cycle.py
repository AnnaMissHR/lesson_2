my_list = ['chair', 'table', 'wardrobe', 'sofa', 'bed']
for furniture in my_list:
	print(furniture)

print('############################')
	
for furniture in my_list:
	if furniture != 'sofa':
		print(furniture)

my_list = my_list + ['door', 'mirror']
print(my_list)



	
for furniture in my_list:
	if furniture == 'table':
		print('im wtiting here')
	elif furniture == 'chair':
		print('im sitting here')