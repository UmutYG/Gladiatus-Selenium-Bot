from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import pyautogui as p
from python_imagesearch import imagesearch
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
action = ActionChains(browser)  # ACTION CHAINSI BROWSERE GOSTERME

browser.get("https://www.facebook.com/login.php?skip_api_login=1&api_key=552294145208884&kid_directed_site=0&app_id=552294145208884&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv10.0%2Fdialog%2Foauth%3Fclient_id%3D552294145208884%26response_type%3Dcode%26scope%3Demail%2Bpages_show_list%2Bpages_read_engagement%2Bpages_read_user_content%2Bpages_manage_engagement%2Bpages_manage_posts%26redirect_uri%3Dhttps%253A%252F%252Fapi.streamelements.com%252Fauth%252Ffacebook%252Fcallback%26state%3DeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZXR1cm5VcmwiOiJodHRwczovL3N0cmVhbWVsZW1lbnRzLmNvbS9pbXNvdGlsdGFmL3N0b3JlIiwicGxhdGZvcm0iOiJ3ZWIiLCJyZWZlcmVyIjoiaHR0cHM6Ly9zdHJlYW1lbGVtZW50cy5jb20vIiwidXNlckZsb3ciOiJzdHJlYW1lciIsImNzcmYiOiJlMGEwMDA4YmE1N2QzYmU2OWFkMWY1NWEyY2IzYzdhZSIsImlhdCI6MTY1NzU3MDg1NywiZXhwIjoxNjU3NTcxMTU3fQ.z1WOh-9JfIHRnSsY0BkRwz-0CgKEtxtk_G1GrzbMAQE%26auth_type%3Drerequest%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc3909bda-3964-4845-9173-db25f6a3be2f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fapi.streamelements.com%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZXR1cm5VcmwiOiJodHRwczovL3N0cmVhbWVsZW1lbnRzLmNvbS9pbXNvdGlsdGFmL3N0b3JlIiwicGxhdGZvcm0iOiJ3ZWIiLCJyZWZlcmVyIjoiaHR0cHM6Ly9zdHJlYW1lbGVtZW50cy5jb20vIiwidXNlckZsb3ciOiJzdHJlYW1lciIsImNzcmYiOiJlMGEwMDA4YmE1N2QzYmU2OWFkMWY1NWEyY2IzYzdhZSIsImlhdCI6MTY1NzU3MDg1NywiZXhwIjoxNjU3NTcxMTU3fQ.z1WOh-9JfIHRnSsY0BkRwz-0CgKEtxtk_G1GrzbMAQE%23_%3D_&display=page&locale=tr_TR&pl_dbl=0")
time.sleep(2)


username = browser.find_element(By.XPATH, "//*[@id='email']")
password = browser.find_element(By.XPATH, "//*[@id='pass']")

username.send_keys("umut_husam@hotmail.com")
time.sleep(0.5)
password.send_keys("kolaysabul")
time.sleep(0.5)
sign_in = browser.find_element(By.XPATH, "//*[@id='loginbutton']")
time.sleep(0.5)
sign_in.click()









