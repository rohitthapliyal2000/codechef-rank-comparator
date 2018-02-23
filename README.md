# codechef-rank-comparator
Web scraping in python using lxml package (XML Path Language)

### Input :

*Two codechef usernames which are to be compared*

### Operations :

*Checks if the entered username is valid or not*
	
*Scraps the name of the user*
	
*Scraps the current codechef ratings of the user*
	
*Outputs the list of mutually participated contests of the users and the winner*
	

### Packages/tools used :

*lxml library to use html element API*
	
*requests library to send HTTP request to the webpage*
	
*sys library to exit the system in case of errors*

*Flask web framework*

*HTML and Javascript to create web template*
	

### Running the source code locally :

*Clone/Download the repo*
	
*Compile/Run the application file i.e. app.py by running the following command:*
	
	$ python app.py

*Enter the following URL in address bar of your browser*
	
	localhost:5000

### Requirements to run the source :

*Python 3*
	
*pip(Python Package Index) :*
	
	$ sudo apt-get install python3-pip
		
*requests package :*
	
	$ pip3 install requests
		
*lxml package :*
	
	$ sudo apt-get install libxml2-dev libxslt1-dev python-dev

	$ pip install lxml

*Flask package :*
	
	$ pip install flask

### Description :

The script works by sending request at URL : 'codechef.com/users/handle'. This part is handled by Python. XML Path Language is used for crawling. Separate files are specified for the information being scraped. A dictionary [contest -> rank] is created for both the users. The mutual contests becomes the part of the result. The information is stored in a string 'result'.

Flask web framework is used for creating a Web API to link the HTML file with the python script.

The UI is created in HTML. The application is then deployed on Heroku cloud platform.

The application can be run using the terminal through local host or directly through the [Heroku platform](http://codechefcomparator.herokuapp.com/)

This Project is a joint contribution of :

[Rohit Thapliyal](https://www.linkedin.com/in/rohit-thapliyal-515b5913a/) and [Neeraj Negi](https://www.linkedin.com/in/iamneerajnegi/)

