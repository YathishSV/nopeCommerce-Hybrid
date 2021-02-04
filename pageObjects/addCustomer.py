import time

from selenium.webdriver.support.select import Select


class AddNewCustomer:
    customers_sidemenu_xpath = "//a[@href='#']//span[text()='Customers']"
    customers_sidemenu_item_xpath = "//a[@class='menu-item-link']//span[text()='Customers']"
    btn_AddNew_xpath = "//a[@class = 'btn bg-blue']"
    txtEmail_xpath = "//input[@id = 'Email']"
    txtPassword_xpath = "//input[@id = 'Password']"
    txtFirstName_xpath = "//input[@id = 'FirstName']"
    txtLastName_xpath = "//input[@id = 'LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtCompany_xpath = "//input[@id = 'Company']"
    chkbx_TaxExempt_xpath = "//input[@id = 'Company']"
    txt_AdminCmnt_xpath = "//textarea[@id = 'AdminComment']"
    txtcustomerRoles_xpath = "//ul[@id='SelectedCustomerRoleIds_taglist']//parent::div"
    lstitem_Administrators_xpath = "//li[text()='Administrators']"
    lstitem_ForumModerators_xpath = "//li[text()='Forum Moderators']"
    lstitem_Guests_xpath = "//li[text()='Guests']"
    lstitem_Registered_xpath = "//li[text()='Registered']"
    lstitem_Vendors_xpath = "//li[text()='Vendors']"
    drpmgrofVendors_xpath = "//*[@id='VendorId']"
    txt_Dob_xpath = "//input[@id = 'DateOfBirth']"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.customers_sidemenu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.customers_sidemenu_item_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btn_AddNew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, firstname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lastname)

    def setCustomerRole(self, role):
        self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
        time.sleep(3)

        if role.lower() == "administrators":
            self.lstitem = self.driver.find_element_by_xpath(self.lstitem_Administrators_xpath)

        elif role.lower() == "forummoderators":
            self.lstitem = self.driver.find_element_by_xpath(self.lstitem_ForumModerators_xpath)

        elif role.lower() == "vendors":
            self.lstitem = self.driver.find_element_by_xpath(self.lstitem_Vendors_xpath)

        else :
            time.sleep(3)
            self.lstitem = self.driver.find_element_by_xpath(self.lstitem_Guests_xpath)
            self.driver.find_element_by_xpath(self.lstitem_Registered_xpath).click()

        self.driver.execute_script("arguments[0].click()",self.lstitem)


    def setVendorManager(self,vendor):
        drp = Select(self.driver.find_element_by_xpath(self.drpmgrofVendors_xpath))
        drp.select_by_visible_text(vendor)

    def setGender(self,gender):
        if gender.lower() == "male":
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender.lower() == "female" :
            self.driver.find_element_by_id(self.rdFemaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setDob(self,dob):
        self.driver.find_element_by_xpath(self.txt_Dob_xpath).send_keys(dob)

    def setAdminContent(self,content):
        self.driver.find_element_by_xpath(self.txt_AdminCmnt_xpath).send_keys(content)

    def setCompanyName(self,company):
        self.driver.find_element_by_xpath(self.txtCompany_xpath).send_keys(company)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()



