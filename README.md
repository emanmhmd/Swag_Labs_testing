This is a demo test using Selenium (WIP)  
__________________________________
The test contains the following cases to valid different parts in the website:  
1-Test login with valid coordinates  
2-Test login with invalid coordinates  
3-Test add items to cart then checkout  
_________________________________________
Project structure goes as the following:  
Swag_Labs_testing/
│
├── Tests/
│   ├── test_login.py               # Test cases for user login
│   ├── test_addtocart.py           # Test cases for add items to cart then checkout
│   └── ...
│
├── pages/
│   ├── LoginPage.py             # Page object for the login page
│   ├── Addtocart.py             # Page object for add items , cart page
│   └── ...
└── README.md  
___________________________________________
Enviroment:
________________
Selenium Version: 4.12.0  
System Platform: linux (Ubuntu - 22.04)  
Browser: ChromeDriver  
Version: 116.0.5845.96 
