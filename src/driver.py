import user_ranks as us
import user_ratings as ur
import name_of_user as un
import last_laugh as ll

rating1 = ""
rating2 = ""
name1 = ""
name2 = ""
handle1 = ""
handle2 = ""
lis1 = []
lis2 = []

# For better UX
print('\nMaximise the terminal\n')

# user input 1
handle1 = input("Enter handle for user 1 : ")

# user input 2
handle2 = input("Enter handle for user 2 : ")

# dictionary [contest -> rank] for user1
dic1 = {}

# scraping contests and respective ranks for user1
us.details_for_one(handle1, dic1, lis1)

rating1 = ur.ratings(handle1)

name1 = un.name(handle1)



# dictionary [contest -> rank] for user2
dic2 = {}

# scraping contests and respective ranks for user2
us.details_for_one(handle2, dic2, lis2)

rating2 = ur.ratings(handle2)

name2 = un.name(handle2)

print('\n')
ll.finish_off(handle1, handle2, name1, name2, rating1, rating2, dic1, dic2, lis1, lis2)
