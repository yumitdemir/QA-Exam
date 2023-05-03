import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())



def hover_on_profile(driver, index):
    profilepic = driver.find_element(By.XPATH, "(//img[@alt='User Avatar'])[{0}]".format(index))
    
    action_chains = ActionChains(driver)
    action_chains.move_to_element(profilepic).perform()
    driver.save_screenshot("screenshot{0}.png".format(index))
    try:
        link = driver.find_element(By.XPATH, "(//a[contains(text(),'View profile')])[{0}]".format(index))
        username = driver.find_element(By.XPATH, "//h5[normalize-space()='name: user{0}']".format(index))
    
    except NoSuchElementException:
        link = None;
        username = None;
        
    link = driver.find_element(By.XPATH, "(//a[contains(text(),'View profile')])[{0}]".format(index))
    username = driver.find_element(By.XPATH, "//h5[normalize-space()='name: user{0}']".format(index))
    return [link, username]
    
def unhover(driver):
    randomplace = driver.find_element(By.XPATH, "(//div[@id='flash-messages'])[1]")
    action_chains = ActionChains(driver)
    action_chains.move_to_element(randomplace).perform()    
    




class ChromeSearch(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = driver
      

    def test_if_right_page(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/hovers")
        driver.save_screenshot("screenshot.png")
        assert "https://the-internet.herokuapp.com/hovers" == driver.current_url
        assert len(driver.find_elements(By.CSS_SELECTOR, ".figure")) == 3

       
    def test_if_hover_shows_informations(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/hovers")
        time.sleep(2)
        for i in range(1, 4):
            link_username = hover_on_profile(driver,i)  
            self.assertIsNotNone(link_username[0])
            self.assertIsNotNone(link_username[1])

    def test_if_viewprofile_link_works(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/hovers")
        
        time.sleep(2)
       
        profiles = len(driver.find_elements(By.CSS_SELECTOR, ".figure"))                    
        for i in range(1, profiles):
            driver.get("https://the-internet.herokuapp.com/hovers")
            time.sleep(1)
            link_username = hover_on_profile(driver,i)
            link_username[0].click() 
            time.sleep(1)
            driver.save_screenshot("screenshot2.png")
            assert "https://the-internet.herokuapp.com/hovers" != driver.current_url
            assert "https://the-internet.herokuapp.com/users/{0}".format(i) == driver.current_url
        
   
           

        
        
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

