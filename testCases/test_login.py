import pytest

from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfigProperty as rConf
from utilities.customLLogger import LogGen


class Test_001_Login:
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homepagetitle(self, setup):
        self.logger.info(" **************** started Test_001_Login ****************")
        self.driver = setup
        self.logger.info(" **************** Testing Home Page Title ****************")
        self.driver.get(rConf.getapplicationURL())
        act_pageTitle = self.driver.title
        self.driver.close()
        if act_pageTitle == "Your store. Login":
            self.logger.info(" **************** Home Page title test passed ****************")
            assert True
        else:
            self.logger.info(" **************** Home Page title test failed **************** ")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self, setup):
        self.driver = setup
        self.driver.get(rConf.getapplicationURL())
        lp = Login(self.driver)
        lp.setUserName(rConf.getusername())
        lp.setPassword(rConf.getpassword())
        lp.clickLogin()
        act_pageTitle = self.driver.title
        lp.clickLogout()
        self.driver.close()
        if act_pageTitle == "Dashboard / nopCommerce administration":
            self.logger.info(" **************** Login test passed **************** ")
            assert True
        else:
            self.logger.info("**************** Login test failed ****************")
            assert False

    @pytest.mark.regression
    def test_invalid_login(self, setup):
        self.driver = setup
        self.driver.get(rConf.getapplicationURL())
        lp = Login(self.driver)
        lp.setUserName(rConf.getusername())
        lp.setPassword("abcde")
        lp.clickLogin()
        act_pageTitle = self.driver.title
        if act_pageTitle != "Dashboard / nopCommerce administration":
            self.driver.save_screenshot(".\\Screenshots\\" + "test_invalid_login.png")
            self.logger.info("**************** Invalid Login test passed ****************")
            assert True
        else:
            self.logger.error("**************** Invalid Login test failed ****************")
            assert False
        self.driver.close()

