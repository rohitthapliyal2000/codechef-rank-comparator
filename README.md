# codechef-rank-comparator
Web scraping in python using lxml package (XML Path Language).

Input :
	Two codechef usernames which are to be compared

Operations :
	Checks if the entered username is valid or not
	Scraps the name of the user
	Scraps the current codechef ratings of the user
	Outputs the list of mutually participated contests of the users and the winner

Packages used :
	lxml library to use html element API
	requests library to send HTTP request to the webpage
	sys library to exit the system in case of errors

Running the source code locally :
	Clone/Download the repo
	Compile/Run the driver file i.e. driver.py by running the following command:
		$ python driver.py
	Note : Keep the files saved in src in the same directory

Requirements to run the source :
	Python 3 should be installed
	Install pip(Python Package Index) :
		sudo apt-get install python3-pip
	Install requests :
		pip3 install requests
	Install lxml :
		sudo apt-get install libxml2-dev libxslt1-dev python-dev
		pip install lxml
