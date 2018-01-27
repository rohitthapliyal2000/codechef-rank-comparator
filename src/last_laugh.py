def finish_off(handle1, handle2, name1, name2, rating1, rating2, dic1, dic2, lis1, lis2):
	
	print("Handle : " + handle1)
	print("Name : " + name1)
	print("Current ratings : " + rating1 + '\n')

	print("Handle : " + handle2)
	print("Name : " + name2)
	print("Current ratings : " + rating2 + '\n')

	lis = []

	if(len(lis1) < len(lis2)):
		lis = lis1
	else:
		lis = lis2

	print("Contest\t\t\tRank1\t\t\tRank2\t\t\tWinner\n")

	for i in range(0, len(lis)):
		if(lis[i] in dic1 and lis[i] in dic2):
			print(lis[i] + '\t\t\t' + dic1[lis[i]] + '\t\t\t' + dic2[lis[i]], end = '\t\t\t')
			if(int(dic1[lis[i]]) < int(dic2[lis[i]])):
					winner = name1
			elif(int(dic1[lis[i]]) > int(dic2[lis[i]])):
				winner = name2
			else:
				winner = "Tie"

			print(winner + '\n')