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

# user input 1
handle = input("Enter handle for user 1 : ")
handle1 = handle

# dictionary [contest -> rank] for user1
dic1 = {}

# scraping contests and respective ranks for user1
us.details_for_one(handle, dic1, lis1)

rating1 = ur.ratings(handle)

name1 = un.name(handle)

# user input 2
handle = input("Enter handle for user 2 : ")
handle2 = handle

# dictionary [contest -> rank] for user2
dic2 = {}

# scraping contests and respective ranks for user2
us.details_for_one(handle, dic2, lis2)

rating2 = ur.ratings(handle)

name2 = un.name(handle)

print('\n')

ll.finish_off(handle1, handle2, name1, name2, rating1, rating2, dic1, dic2, lis1, lis2)
