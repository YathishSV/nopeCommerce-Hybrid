import pytest

from utilities.readProperties import ReadConfigProperty
from pageObjects.LoginPage import Login
from pageObjects.addCustomer import AddNewCustomer
from pageObjects.searchCustomerPage import SearchCustomer
import time

class Test_004_SearchCustomer:
    baseURL = ReadConfigProperty.getapplicationURL()
    username = ReadConfigProperty.getusername()
    password = ReadConfigProperty.getpassword()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.cust = AddNewCustomer(self.driver)
        self.cust.clickOnCustomersMenu()
        self.cust.clickOnCustomersMenuItem()

        self.search = SearchCustomer(self.driver)
        self.search.setEmail("brenda_lindgren@nopCommerce.com")
        self.search.clickSearch()
        time.sleep(3)

        if self.search.searchByEmail("brenda_lindgren@nopCommerce.com") :
            assert True
            print("Email found Successfully")
        else:
            assert False
            print("Email not found")

        self.lp.clickLogout()
        self.driver.close()

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.cust = AddNewCustomer(self.driver)
        self.cust.clickOnCustomersMenu()
        self.cust.clickOnCustomersMenuItem()

        self.search = SearchCustomer(self.driver)
        self.search.setFirstName("James")
        self.search.setLastName("pan")
        self.search.clickSearch()
        time.sleep(3)

        if self.search.searchCustomerByName("James Pan") :
            assert True
            print("Name found Successfully")
        else:
            assert False
            print("Name not found")

        self.lp.clickLogout()
        self.driver.close()






