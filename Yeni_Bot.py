from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import pyautogui as p
from python_imagesearch import imagesearch
from selenium.webdriver.common.by import By

from TelegramNotify import send_msg
import os
# ************* SİTE AÇILIŞI ************
from selenium.webdriver.remote.webelement import WebElement

kesifTamamlandi = 1
zindanTamamlandi = 1


def kesifSeferiYap(browser):
    global kesifTamamlandi
    kesif_seferi = browser.find_element(By.XPATH,"//*[@id='cooldown_bar_expedition']/a")
    kesif_seferi.click()

    #saldir_1 = browser.find_element(By.XPATH,"//*[@id='expedition_list']/div[3]/div[2]/button")
    # saldir_3 = browser.find_element(By.XPATH,"//*[@id='expedition_list']/div[3]/div[2]/button")
    saldir_2 = browser.find_element(By.XPATH,"//*[@id='expedition_list']/div[1]/div[2]/button")

    saldir_2.click()
    send_msg(str(kesifTamamlandi) + ". Keşif Tamam.")
    kesifTamamlandi += 1
    time.sleep(2)


def zindanYap(browser):
    global zindanTamamlandi
    zindan = browser.find_element(By.XPATH,"//*[@id='cooldown_bar_dungeon']/a")
    zindan.click()
    time.sleep(2)
    try:
        yeniZindan = browser.find_element(By.XPATH,"//*[@id='content']/div[2]/div/form/table/tbody/tr/td[1]/input")
        yeniZindan.click()
        time.sleep(2)
        print("Yeni zindana girildi.")
    except:
        pass

    zindanSaldir = browser.find_element(By.CSS_SELECTOR,"img[src='9407/img/combatloc.gif']")
    zindanSaldir.click()
    send_msg(str(zindanTamamlandi) + ". Zindan Tamam.")
    zindanTamamlandi += 1
    time.sleep(2)


a = 0
sayac = 0


def canYenile(browser):
    global envanter, a, sayac
    try:
        canBariElement = browser.find_element(By.XPATH,"//*[@id='header_values_hp_percent']")
        canBariText = canBariElement.text
        canBariTextInt = int(canBariText[:len(canBariText) - 1])
        print("İlk can = ", canBariTextInt)
        send_msg("Can azaldı : " + str(canBariTextInt))
        p.moveTo(755 + a, 1000)
        p.mouseDown()
        time.sleep(0.2)
        p.moveTo(580, 778)
        time.sleep(0.4)
        p.mouseUp()
        time.sleep(2)
        a += 40
        sayac += 1

        canBariElement = browser.find_element(By.XPATH,"//*[@id='header_values_hp_percent']")
        canBariText = canBariElement.text
        canBariTextInt = int(canBariText[:len(canBariText) - 1])
        print("Yeni can = ", canBariTextInt)

        send_msg("Yeni can : " + str(canBariTextInt))
        if canBariTextInt < 10:
            browser.close()
    except Exception:
        pass

    time.sleep(1)


def arenaYap(browser):
    arena = browser.find_element(By.XPATH,"//*[@id='cooldown_bar_arena']/a")
    arena.click()
    time.sleep(2)
    arenaUstRakip = browser.find_element(By.CLASS_NAME,
        "attack")


    arenaUstRakip.click()
    time.sleep(2)


def sirkYap(browser):
    try:
        sirk = browser.find_element(By.XPATH,"//*[@id='cooldown_bar_ct']/a")
        sirk.click()
        time.sleep(2)
        sirkUstRakip = browser.find_element(By.XPATH,
            "//*[@id='own3']/table/tbody/tr[2]/td[4]/div")
        sirkUstRakip.click()
        send_msg("Sirk tamamlandı.")
        time.sleep(2)
    except:
        send_msg("Sirk hatası.")


def levelKontrol(browser):
    try:
        tamam = browser.find_element(By.XPATH, "//*[@id='linknotification']")
        tamam.click()
    except Exception:
        print()





def basla(kesifAllowed, zindanAllowed):

    browser = webdriver.Chrome()
    action = ActionChains(browser)  # ACTION CHAINSI BROWSERE GOSTERME
    browser.get(
        "https://s47-tr.gladiatus.gameforge.com/game/index.php?mod=overview&sh=69629a882266dbc357b4927e6440b0ab")
    time.sleep(3)
    try:
        cerezKabul = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/span[2]/button[2]")
        cerezKabul.click()

    except:
        pass
    # ************* İLK GİRİŞ ************
    giris_sayfasi = browser.find_element(By.XPATH,"//*[@id='loginRegisterTabs']/ul/li[1]/span")
    giris_sayfasi.click()
    time.sleep(3)

    # ************* BİLGİ GİRİŞİ ************

    username = browser.find_element(By.NAME,"email")
    password = browser.find_element(By.NAME,"password")
    username.send_keys("<yourusername>")
    password.send_keys("<yourpassword>")
    time.sleep(3)
    giris_yap = browser.find_element(By.XPATH,"//*[@id='loginForm']/p/button[1]/span")
    giris_yap.click()
    time.sleep(3)

    # ************* BILGILERLE OYNAYA BASIŞ ************
    oyna = browser.find_element(By.XPATH,"//*[@id='joinGame']/a/button")
    oyna.click()
    time.sleep(2)
    oyna2 = browser.find_element(By.XPATH,"//*[@id='accountlist']/div/div[1]/div[2]/div[1]/div/div[4]/div")
    time.sleep(3)

    # ************* YENI SEKME KONTROLU VE ÇİFT TIKLA OYUNA GİRME ************
    window_before = browser.window_handles[0]
    action.double_click(oyna2).perform()
    time.sleep(3)
    window_after = browser.window_handles[1]
    time.sleep(2)
    browser.switch_to.window(window_after)
    time.sleep(2)

    try:
        p.moveTo(1255, 204)
        p.click()
        time.sleep(2)
    except:
        pass

    # ************* BOT KESIF SEFERI - ARENA DEGISKENLERI ************
    arena = browser.find_element(By.XPATH,"//*[@id='cooldown_bar_arena']/a")
    zindan = browser.find_element(By.XPATH,"//*[@id='cooldown_bar_dungeon']/a")
    # ************* CAN BARI TANITIM ************
    canBariElement = browser.find_element(By.XPATH, "//*[@id='header_values_hp_percent']")
    canBariText = canBariElement.text
    canBariTextInt = int(canBariText[:len(canBariText) - 1])

    # ************** SURUKLEME YEMEK ***********

    yemekDiv = "//*[@id='inv']/div[1]"
    envanter = browser.find_element(By.XPATH, yemekDiv)  # ENV ILK YERIkran parla

    karakter = browser.find_element(By.XPATH,"//*[@id='avatar']/div[2]")
    KesifSeferi = browser.find_element(By.XPATH,"//*[@id='expeditionpoints_value_point']").text
    KesifSeferiHakki = int(KesifSeferi)
    i = 1
    while KesifSeferiHakki > 5:
        p.moveTo(1255, 204)
        p.click()
        canBariElement = browser.find_element(By.XPATH,"//*[@id='header_values_hp_percent']")
        canBariText = canBariElement.text
        canBariTextInt = int(canBariText[:len(canBariText) - 1])
        tecrube = browser.find_element(By.XPATH, "//*[@id='header_values_xp_percent']").text
        print(tecrube)
        if canBariTextInt < 20:
            canYenile(browser)
        else:
            if kesifAllowed:
                kesifSeferiYap(browser)
                KesifSeferi = browser.find_element(By.XPATH,"//*[@id='expeditionpoints_value_point']").text
                KesifSeferiHakki = int(KesifSeferi)
                levelKontrol(browser)
                time.sleep(1)

            zindann = browser.find_element(By.XPATH,"//*[@id='dungeonpoints_value_point']").text
            zindanHakki = int(zindann)
            if zindanHakki > 10 and zindanAllowed:
                try:
                    zindanYap(browser)
                    levelKontrol(browser)
                    sirkYap(browser)
                    #arenaYap(browser)
                except Exception as e:
                    print("Zindan hatası")
                    send_msg("Zindan Yapılırken Hata.")


            genelDurum = browser.find_element(By.XPATH,"//*[@id='mainmenu']/a[1]")
            genelDurum.click()

            time.sleep(55)


basla(1, 1)
