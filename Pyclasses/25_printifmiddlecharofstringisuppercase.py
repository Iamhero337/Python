a = input(" Give input: ")

if len(a)%2 ==1:
	if 'A'<= a[len(a)//2] <= 'Z':
		print(a[len(a)//2])
	else:
		print("The middle char is not uppercase.")
else:
	print('This does not have middle char.')
