import requests
from lxml import html
import sys
import lxml.etree
import lxml._elementpath


def ratings(handle, result):

	str = ""

	#valid username url
	url = 'https://www.codechef.com/users/' + handle

	page = requests.get(url)

	tree = html.fromstring(page.content)

	data = tree.xpath("//div/section/div/div/div/a/text()")

	if len(data) == 0:
		result = result + "Handle: " + handle + " is invalid."
		print("Wrong Handle: user_ratings_py")
		sys.exit()

	else:
		for i in range(0, len(data[0])-2):
			str += data[0][i]

	return str
