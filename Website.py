from selenium import webdriver
import datetime
import unittest
from selenium.webdriver.common.keys import Keys

class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):

        desired_capabilities = webdriver.DesiredCapabilities.CHROME
        desired_capabilities['version'] = ''
        desired_capabilities['platform'] = 'Windows 8'
        desired_capabilities['name'] = 'Website Testing'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://jhayes:b89520c0-92db-45f5-8305-e86a68fed481@ondemand.saucelabs.com:80/wd/hub"
        )
        self.driver.implicitly_wait(30)

    def test_social_media(self):
        self.driver.get('http://qa-gift-give.herokuapp.com')
        self.driver.implicitly_wait(10)

        assert "Fundraising" in self.driver.title

        #Start of Social media test

        facebook = self.driver.find_element_by_link_text('Facebook')
        self.assertEqual("http://www.facebook.com/GiftGiveLLC",facebook.get_attribute("href"))

        twitter = self.driver.find_element_by_link_text('Twitter')
        self.assertEqual("http://twitter.com/giftgive1", twitter.get_attribute("href"))

        gplus = self.driver.find_element_by_link_text('Google+')
        self.assertEqual("http://plus.google.com/100777158497033145395?prsrc=3", gplus.get_attribute("href"))

        youtube = self.driver.find_element_by_link_text('YouTube')
        self.assertEqual("http://www.youtube.com/ggivesoftware",youtube.get_attribute("href"))

        pint = self.driver.find_element_by_link_text('Pinterest')
        self.assertEqual("http://pinterest.com/giftgive/", pint.get_attribute("href"))

        link = self.driver.find_element_by_link_text('LinkedIn')
        self.assertEqual("http://www.linkedin.com/company/gift-give-inc-", link.get_attribute("href"))

        rss = self.driver.find_element_by_link_text('Blog')
        self.assertEqual("http://www.gift-give.com/content", rss.get_attribute("href"))

    #End

    def test_header_links(self):
        #checks all the links on the homepage
        self.driver.get('http://qa-gift-give.herokuapp.com')
        self.driver.implicitly_wait(2)

        np = self.driver.find_element_by_link_text('Nonprofits')
        np.click()
        self.driver.implicitly_wait(2)
        self.assertEqual ("What Is GiFTgive? | GiFTgive", self.driver.title)

        self.driver.get('http://qa-gift-give.herokuapp.com')
        self.driver.implicitly_wait(5)

        donors = self.driver.find_element_by_link_text('Donors')
        donors.click()
        self.assertEqual ("Browse | GiFTgive" , self.driver.title)

        self.driver.get('http://qa-gift-give.herokuapp.com')
        self.driver.implicitly_wait(5)

        price = self.driver.find_element_by_link_text('Pricing')
        price.click()
        self.assertEqual("Pricing | GiFTgive" ,self.driver.title)

        self.driver.get('http://qa-gift-give.herokuapp.com')
        self.driver.implicitly_wait(5)

        faq = self.driver.find_element_by_link_text('FAQ')
        faq.click()
        self.driver.implicitly_wait(5)
        self.assertEqual("FAQ | GiFTgive", self.driver.title)

        self.driver.get('http://qa-gift-give.herokuapp.com')
        self.driver.implicitly_wait(5)

        contact = self.driver.find_element_by_link_text('Contact')
        contact.click()
        self.driver.implicitly_wait(5)
        self.assertEqual("Help | GiFTgive", self.driver.title)


    def test_blog(self):

        self.driver.get('http://qa-gift-give.herokuapp.com')
        self.driver.implicitly_wait(5)

        blog = self.driver.find_element_by_link_text('Blog')
        blog.click()
        self.driver.implicitly_wait(15)
        self.assertEqual("Blog | GiFTgive", self.driver.title)

    def test_login(self):

        self.driver.get("http://www.gift-give.com")
        signin = self.driver.find_element_by_id('login')
        signin.click()

        
        username = self.driver.find_element_by_id('user_email')
        password = self.driver.find_element_by_id('user_password')

        #Invalid Test Case -- Both wrong
        username.sendKeys('joe@mail.com')
        password.sendKeys('strange')
        password..sendKeys(Keys.RETURN)
        
        
                
        

        

        
        

    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()












