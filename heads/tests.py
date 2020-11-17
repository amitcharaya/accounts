from django.test import TestCase
from selenium import webdriver

class FunctionalTestCase(TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()


    def test_login(self):
        self.browser.get("http://localhost:8000")
        text=self.browser.find_element_by_id('inputEmail')
        text.send_keys('charayaamit@gmail.com')
        self.browser.find_element_by_name('Sign in').click()
        self.assertIn("Please sign in",self.browser.page_source)


    def test_home_page(self):
        self.browser.get("http://localhost:8000")
        self.assertIn('Please sign in',self.browser.page_source)


    def test_homepage_template(self):
        response=self.client.get("/")
        self.assertTemplateUsed(response,"heads/index.html")
