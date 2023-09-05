# Swag Labs Testing Demo   

This is a demo project for automated testing of the Swag Labs e-commerce website using Selenium. The project includes test cases to validate various parts of the website.  

## Test Cases  

The test cases included in this project are:  

1. **Test Login with Valid Credentials**: Validates the login functionality using valid credentials.  
2. **Test Login with Invalid Credentials**: Validates the login functionality using invalid credentials.  
3. **Test Add Items to Cart and Checkout**: Adds items to the cart and completes the checkout process.  

## Demo  
  
You can watch a sample demo of the tests in action here .  

https://github.com/emanmhmd/Swag_Labs_testing/assets/63087099/ccf77a6c-8bf9-405c-a581-cee543bd827d




## Project Structure  

The project is organized as follows:  

Swag_Labs_testing/  
│  
├── Tests/  
│ ├── test_login.py  
│ ├── test_addtocart.py  
│ └── ...  
│  
├── Pages/  
│ ├── LoginPage.py  
│ ├── Addtocart.py  
│ └── ...  
│  
├── Fixtures/  
│ ├── Data.json  
│  
└── README.md   


- **Tests**: Contains test scripts for different parts of the Swag Labs website.  
- **Pages**: Includes Python classes representing various pages of the website to encapsulate page elements and interactions.  
- **Fixtures**: Stores fixtures and test data, such as login credentials, in JSON format.  

## Getting Started  

To run the tests, follow these steps:  

1. Clone this repository to your local machine.  
2. Navigate to the project directory.  
3. Install the necessary dependencies using `pip install selenium`.  
4. Run the tests using the testing framework of your choice. For example, you can run `pytest Tests` to execute all test scripts in the `Tests` directory.  

## Environment  

- **Selenium Version**: 4.12.0  
- **System Platform**: Linux (Ubuntu 22.04)  
- **Browser**: ChromeDriver 116.0.5845.96  

## Contributors  

- [Eman Mahmoud](https://github.com/emanmhmd)  


