import pytest

from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfigProperty as rConf
from utilities.customLLogger import LogGen
from utilities import xcelutils
import time


class Test_002_Login:
    logger = LogGen.loggen()
    path = ".//TestData//LoginData.xlsx"

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login_ddt(self, setup):
        self.driver = setup
        self.driver.get(rConf.getapplicationURL())
        lp = Login(self.driver)

        rowcount = xcelutils.getRowCount(self.path, "Sheet1")
        test_status = []
        for r in range(2, rowcount + 1):
            username = xcelutils.readData(self.path, "Sheet1", r, 1)
            password = xcelutils.readData(self.path, "Sheet1", r, 2)
            exp = xcelutils.readData(self.path, "Sheet1", r, 3)
            lp.setUserName(username)
            lp.setPassword(password)
            lp.clickLogin()
            time.sleep(5)
            act_pageTitle = self.driver.title
            if act_pageTitle == "Dashboard / nopCommerce administration":
                if exp == "Pass":
                    lp.clickLogout()
                    test_status.append("Pass")

                elif exp == "Fail":
                    lp.clickLogout()
                    test_status.append("Fail")

            elif act_pageTitle != "Dashboard / nopCommerce administration":
                if exp == "Pass":
                    test_status.append("Fail")

                elif exp == "Fail":
                    test_status.append("Pass")
        self.driver.close()
        print(test_status)
        if "Pass" in test_status:
            print("Test Passed")
            assert True
        else:
            print("Test Failed")
            assert False
