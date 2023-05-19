from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import pyautogui as p
i = 1
a = 0
def kesifSeferiYap(browser):
    kesif_seferi = browser.find_element_by_xpath("//*[@id='cooldown_bar_expedition']/a")
    kesif_seferi.click()
    time.sleep(3)


    saldir_1 = browser.find_element_by_xpath("//*[@id='expedition_list']/div[2]/div[2]/button")
    # saldir_3 = browser.find_element_by_xpath("//*[@id='expedition_list']/div[3]/div[2]/button")
    # saldir_2 = browser.find_element_by_xpath("//*[@id='expedition_list']/div[2]/div[2]/button")
    #saldir_1.click()


    time.sleep(2)
def muzayedeCheck(browser):
    hermitBas = browser.find_element_by_xpath("//*[@id='submenuhead2']/div[1]/a")
    hermitBas.click()
    time.sleep(2)
    muzSalonu = browser.find_element_by_xpath("//*[@id='submenu1']/a[8]")
    muzSalonu.click()
    time.sleep(2)
    muzoSure = browser.find_element_by_xpath("//*[@id='content']/article/p[1]/span[2]/b").text
    print(muzoSure)

def basla():
    browser = webdriver.Chrome()
    action = ActionChains(browser)
    browser.get(
        "https://s47-tr.gladiatus.gameforge.com/game/index.php?mod=overview&sh=69629a882266dbc357b4927e6440b0ab")
    time.sleep(2)
    cookie = browser.find_element_by_xpath("/html/body/div[3]/div/div/span[2]/button[2]")
    cookie.click()
    time.sleep(2)
    giris_sayfasi = browser.find_element_by_xpath("//*[@id='loginRegisterTabs']/ul/li[1]/span")
    giris_sayfasi.click()
    time.sleep(2)
    username = browser.find_element_by_name("email")
    password = browser.find_element_by_name("password")
    username.send_keys("umutgndz13@gmail.com")
    password.send_keys("Umut07umut07")
    time.sleep(2)
    giris_yap = browser.find_element_by_xpath("//*[@id='loginForm']/p/button[1]/span")
    giris_yap.click()
    time.sleep(3)
    oyna = browser.find_element_by_xpath("//*[@id='joinGame']/a/button")
    oyna.click()
    time.sleep(2)
    oyna2 = browser.find_element_by_xpath("//*[@id='accountlist']/div/div[1]/div[2]/div[1]/div/div[4]/div")
    time.sleep(2)
    window_before = browser.window_handles[0]
    action.double_click(oyna2).perform()
    time.sleep(2)
    window_after = browser.window_handles[1]
    time.sleep(2)
    browser.switch_to.window(window_after)
    time.sleep(2)

    p.moveTo(1255, 204)
    p.click()

    KesifSeferiHakki = browser.find_element_by_xpath("//*[@id='expeditionpoints_value_point']").text
    print("Kalan Keşif Hakkı:", int(KesifSeferiHakki))
    kesifSeferiYap(browser)

    muzayedeCheck(browser)

basla()