def finish_off(handle1, handle2, name1, name2, rating1, rating2, dic1, dic2, lis1, lis2, result):
	
	par1 = 0
	par2 = 0
	result = result + "Handle : " + handle1 + "\n"
	result = result + "Name : " + name1+ "\n"
	result = result + "Current ratings : " + rating1 + '\n'
	result = result + "\n"
	result = result + "Handle : " + handle2 + "\n"
	result = result + "Name : " + name2 + "\n"
	result = result + "Current ratings : " + rating2 + '\n'
	result = result + "\n"

	lis = []

	if(len(lis1) < len(lis2)):
		lis = lis1
	else:
		lis = lis2

	result = result + "Contest\t\t\tRank1\t\t\tRank2\t\t\tWinner\n"

	for i in range(0, len(lis)):
		if(lis[i] in dic1 and lis[i] in dic2):
			result = result + lis[i] + "\t\t\t" + dic1[lis[i]] + "\t\t\t" + dic2[lis[i]]
			if(int(dic1[lis[i]]) < int(dic2[lis[i]])):
				winner = name1
				par1 += 1
			elif(int(dic1[lis[i]]) > int(dic2[lis[i]])):
				winner = name2
				par2 += 1
			else:
				winner = "Tie"

			result = result + "\t\t\t" +  winner + '\n'

	result += "\n" + "Wins: \n"
	result += name1 + " : " + str(par1) + "\t"
	result += name2 + " : " + str(par2) + "\n\n"
	if(par1 == par2):
		result += "Tie" + "\n\n\n"
	else:
		result += "OVERALL WINNER : "
		if(par1 > par2):
			result += name1 + "\n\n\n"
		else:
			result += name2 + "\n\n\n"
	return result
