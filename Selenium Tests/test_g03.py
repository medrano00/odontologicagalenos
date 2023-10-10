# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestG03():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_g03(self):
    self.driver.get("http://127.0.0.1:8000/index/")
    self.driver.set_window_size(974, 1080)
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(4) > .nav-link").click()
    self.driver.find_element(By.ID, "id_username").click()
    self.driver.find_element(By.ID, "id_username").send_keys("fespinoza")
    self.driver.find_element(By.ID, "id_password").send_keys("1234")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    self.driver.find_element(By.CSS_SELECTOR, "li").click()
    self.driver.find_element(By.CSS_SELECTOR, "li").click()
  
