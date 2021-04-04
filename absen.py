from link_matkul import matkul
import json

ket, matkul_sekarang = matkul()
if matkul_sekarang == 0:
    print(ket)
else:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time
    PATH = "C:\Drivers\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    LOGIN_URL = "http://elearning.bsi.ac.id/login"
    driver.get(LOGIN_URL)
    data = json.load(open('akun.json'))
    username_mhs = data['username']
    password_mhs = data['password']

    username = driver.find_element_by_id("username")
    username.send_keys(username_mhs)

    password = driver.find_element_by_id("password")
    password.send_keys(password_mhs)
    password.send_keys(Keys.ENTER)

    driver.get(matkul_sekarang)

    time.sleep(3)
    absen = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[5]/div/form/center/button")
    absen.click()

    komen = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[5]/div/form/center/textarea")
    komen.send_keys("Sudah Absen Hari ini")
    kirim = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[5]/div/form/center/button")
    kirim.click()