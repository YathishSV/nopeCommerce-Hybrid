

class SearchCustomer:
    txt_searchEmail_xpath = "//input[@id='SearchEmail']"
    txt_searchFirstName_xpath = "//input[@id='SearchFirstName']"
    txt_searchLastName_xpath="//input[@id='SearchLastName']"
    txt_searchCompany_xpath = "//input[@id='SearchCompany']"
    txt_searchIpAddress_xpath="//input[@id='SearchIpAddress']"
    btn_search_xpath = "//button[@id='search-customers']"

    tbl_results_xpath = "//table[@id='customers-grid']"
    tbl_resultsRow_xpath = "//table[@id='customers-grid']//tbody//tr"
    tbl_resultsColoumn_xpath = "//table[@id='customers-grid']//tbody//tr//td"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txt_searchEmail_xpath).clear()
        self.driver.find_element_by_xpath(self.txt_searchEmail_xpath).send_keys(email)

    def setFirstName(self,firstname):
        self.driver.find_element_by_xpath(self.txt_searchFirstName_xpath).clear()
        self.driver.find_element_by_xpath(self.txt_searchFirstName_xpath).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element_by_xpath(self.txt_searchLastName_xpath).clear()
        self.driver.find_element_by_xpath(self.txt_searchLastName_xpath).send_keys(lastname)

    def clickSearch(self):
        self.driver.find_element_by_xpath(self.btn_search_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tbl_resultsRow_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tbl_resultsColoumn_xpath))

    def searchByEmail(self,email):
        flag = False
        for i in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.tbl_results_xpath)
            emailid = table.find_element_by_xpath("//table[@id='customers-grid']//tbody//tr["+str(i)+"]//td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self,name):
        flag = False
        for i in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.tbl_results_xpath)
            fullname = table.find_element_by_xpath("//table[@id='customers-grid']//tbody//tr["+str(i)+"]//td[3]").text
            if fullname == name:
                flag = True
                break
        return flag

