import sys
import user_ranks as us
import user_ratings as ur
import name_of_user as un
import last_laugh as ll

def driver_function(handle1, handle2):
	rating1 = ""
	rating2 = ""
	name1 = ""
	name2 = ""
	lis1 = []
	lis2 = []
	result = ""

	# dictionary [contest -> rank] for user1
	dic1 = {}

	print("Calling name_of_user for " + handle1)
	name1 = un.name(handle1, result)
	if(len(name1) > 0):
		print("Calling name_of_user for " + handle2)
		name2 = un.name(handle2, result)

		if(len(name2) > 0):
			# scraping contests and respective ranks for user1
			print("Calling user_ranks for " + handle1)
			us.details_for_one(handle1, dic1, lis1, result)
			
			print("Calling user_ratings for " + handle1)
			rating1 = ur.ratings(handle1, result)
			
			# dictionary [contest -> rank] for user2
			dic2 = {}

			# scraping contests and respective ranks for user2
			print("Calling user_ranks for " + handle2)
			us.details_for_one(handle2, dic2, lis2, result)

			print("Calling user_ratings for " + handle2)
			rating2 = ur.ratings(handle2, result)

			print("Calling finishing function")
			return ll.finish_off(handle1, handle2, name1, name2, rating1, rating2, dic1, dic2, lis1, lis2, result)
		else:
			print("Handle2 is wrong")
			result += "Handle: " + handle2 + " is not a valid handle."
			return result
	else:
		print("Handle1 is wrong")
		result += "Handle: " + handle1 + " is not a valid handle."
		return result
