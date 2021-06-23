# selenium-py/002-seleniump-python-alapok-1
# 006 006 Feladat: Selenium weboldal menyitás gyakorlása

# Készíts egy Python alkalmazást ami selenium-ot használ. Nyisson meg egy Chrome böngészöt és töltsön be egy tetszőleges weblapot az Internetről.
# A megoldást egy start.py nevű fileban kell beadnod.

from selenium import webdriver

PATH = "C:\\Windows\\webdriversForSelenium\\chromedriver.exe"
URL = "https://e-learning.training360.com/courses/take/szoftverteszteles-selenium-webdriverrel/texts/24442049-feladat-python-for-ciklus-gyakorlasa"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

time.sleep(2)
browser.quit()