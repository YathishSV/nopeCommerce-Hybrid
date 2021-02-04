import pytest

from utilities.readProperties import ReadConfigProperty
from pageObjects.addCustomer import AddNewCustomer
from pageObjects.LoginPage import Login
import uuid


class Test_003_AddCustomer:
    baseURL = ReadConfigProperty.getapplicationURL()
    username = ReadConfigProperty.getusername()
    password = ReadConfigProperty.getpassword()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.addCust = AddNewCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()

        self.addCust.clickOnAddNew()
        self.email = str(uuid.uuid4()) + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        self.addCust.setFirstName("Shady")
        self.addCust.setLastName("Mathers")
        self.addCust.setGender("male")
        self.addCust.setDob("1/28/2021")
        self.addCust.setCompanyName("AutoQA")
        self.addCust.setCustomerRole("guests")
        self.addCust.setVendorManager("Vendor 1")
        self.addCust.clickOnSave()

        self.msg = self.driver.find_element_by_tag_name("body").text

        if "new customer has been added successfully" in self.msg:
            assert True
            print("Test case passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addNewCustomer.png")
            assert False

        self.driver.close()
        print("Test done")
