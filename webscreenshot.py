from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="C:/Users/Pooja Devi/Downloads/chromedriver_win32 (1)/chromedriver.exe")
driver.get("https://unsplash.com/s/photos/dog")
driver.save_screenshot("C:/Users/Pooja Devi/Desktop/screenshot/image.png")

sleep(1)


driver.quit()
print("end...")