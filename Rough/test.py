from os.path import dirname
from selenium.webdriver.support.select import Select

from selenium import webdriver
from pathlib import Path
class TestMethod:


    sel = Select (webdriver.Chrome.find_element_by_id("abc"))
    sel.select_by_visible_text()
    def test_method(self):
        print(self.test_method.__name__)


abc = TestMethod()
abc.test_method()
#print(str(Path.home()))
print((dirname(dirname(__file__))))