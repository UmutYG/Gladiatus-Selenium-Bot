from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import pyautogui as p
from python_imagesearch import imagesearch
from TelegramNotify import send_msg
import os
# ************* SİTE AÇILIŞI ************
from selenium.webdriver.remote.webelement import WebElement

kesifTamamlandi = 1
zindanTamamlandi = 1


def kesifSeferiYap(browser):
    global kesifTamamlandi
    kesif_seferi = browser.find_element_by_xpath("//*[@id='cooldown_bar_expedition']/a")
    kesif_seferi.click()

    saldir_1 = browser.find_element_by_xpath("//*[@id='expedition_list']/div[3]/div[2]/button")
    # saldir_3 = browser.find_element_by_xpath("//*[@id='expedition_list']/div[3]/div[2]/button")
    # saldir_2 = browser.find_element_by_xpath("//*[@id='expedition_list']/div[2]/div[2]/button")

    saldir_1.click()
    send_msg(str(kesifTamamlandi) + ". Keşif Tamam.")
    kesifTamamlandi += 1
    time.sleep(2)


def zindanYap(browser):
    global zindanTamamlandi
    zindan = browser.find_element_by_xpath("//*[@id='cooldown_bar_dungeon']/a")
    zindan.click()
    time.sleep(2)
    try:
        yeniZindan = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/form/table/tbody/tr/td[1]/input")
        yeniZindan.click()
        time.sleep(2)
        print("Yeni zindana girildi.")
    except:
        pass

    zindanSaldir = browser.find_element_by_css_selector("img[src='9391/img/combatloc.gif']")
    zindanSaldir.click()
    send_msg(str(zindanTamamlandi) + ". Zindan Tamam.")
    zindanTamamlandi += 1
    time.sleep(2)


a = 0
sayac = 0


def canYenile(browser):
    global envanter, a, sayac
    try:
        canBariElement = browser.find_element_by_xpath("//*[@id='header_values_hp_percent']")
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

        canBariElement = browser.find_element_by_xpath("//*[@id='header_values_hp_percent']")
        canBariText = canBariElement.text
        canBariTextInt = int(canBariText[:len(canBariText) - 1])
        print("Yeni can = ", canBariTextInt)

        send_msg("Yeni can : " + str(canBariTextInt))
        if canBariTextInt < 10:
            browser.close()
    except Exception:
        pass

    time.sleep(1)


def egitimYap(browser):
    try:

        taverna = browser.find_element_by_xpath("//*[@id='submenuhead1']/div[1]/a")
        taverna.click()
        time.sleep(2)
        egitimSayfasi = browser.find_element_by_xpath("//*[@id='submenu1']/a[3]")
        egitimSayfasi.click()
        time.sleep(2)

        egit = browser.find_element_by_xpath("//*[@id='training_box']/div[5]/div[2]/a")
        egit.click()
        time.sleep(2)

    except Exception:
        send_msg("Eğitim hatası yapıldı.")
        time.sleep(2)


def arenaYap(browser):
    arena = browser.find_element_by_xpath("//*[@id='cooldown_bar_arena']/a")
    arena.click()
    time.sleep(2)
    arenaUstRakip = browser.find_element_by_xpath(
        "//*[@id='content']/article/aside[2]/section/table/tbody/tr[2]/td[2]/div")
    arenaUstRakip.click()
    time.sleep(2)


def sirkYap(browser):
    try:
        sirk = browser.find_element_by_xpath("//*[@id='cooldown_bar_ct']/a")
        sirk.click()
        time.sleep(2)
        sirkUstRakip = browser.find_element_by_xpath(
            "//*[@id='own3']/table/tbody/tr[2]/td[4]/div")
        sirkUstRakip.click()
        send_msg("Sirk tamamlandı.")
        time.sleep(2)
    except:
        send_msg("Sirk hatası.")


def levelKontrol(browser):
    try:
        tamam = browser.find_element_by_xpath("//*[@id='linknotification']")
        tamam.click()
    except Exception:
        print()


def muzayedeCheck(browser):
    try:
        hermitBas = browser.find_element_by_xpath("//*[@id='submenuhead2']/div[1]/a")
        hermitBas.click()
        time.sleep(2)
        muzSalonu = browser.find_element_by_xpath("//*[@id='submenu1']/a[15]")
        muzSalonu.click()
        time.sleep(2)
        muzoSure = browser.find_element_by_xpath("//*[@id='content']/article/p[1]/span[2]/b").text
        print(muzoSure)
        send_msg("Kalan müzayede süresi : " + muzoSure + "\n")
        if muzoSure == "çok kısa":
            send_msg("Müzayede bitmek üzere!")
    except:
        send_msg("Müzayede bakımında hata.")


def paraBagisla(browser):
    try:
        ittifak = browser.find_element_by_xpath("//*[@id='mainmenu']/a[3]")
        ittifak.click()
        time.sleep(2)
        banka = browser.find_element_by_xpath("//*[@id='content']/div[1]/a[6]")
        banka.click()
        time.sleep(2)
        bagis = browser.find_element_by_xpath(
            "//*[@id='content']/article/section[2]/form/table/tbody/tr[2]/th[2]/input")
        bagis.send_keys("10000")
        tikla = browser.find_element_by_xpath("//*[@id='content']/article/section[2]/form/table/tbody/tr[3]/th/input")
        tikla.click()
        send_msg("Para bağışı yapıldı : 10000 ")
        time.sleep(2)
    except:
        pass


def basla(kesifAllowed, zindanAllowed):

    browser = webdriver.Chrome()
    action = ActionChains(browser)  # ACTION CHAINSI BROWSERE GOSTERME
    browser.get(
        "https://s47-tr.gladiatus.gameforge.com/game/index.php?mod=overview&sh=69629a882266dbc357b4927e6440b0ab")
    time.sleep(3)
    try:
        cerezKabul = browser.find_element_by_xpath("/html/body/div[3]/div/div/span[2]/button[2]")
        cerezKabul.click()
    except:
        pass
    # ************* İLK GİRİŞ ************
    giris_sayfasi = browser.find_element_by_xpath("//*[@id='loginRegisterTabs']/ul/li[1]/span")
    giris_sayfasi.click()
    time.sleep(3)

    # ************* BİLGİ GİRİŞİ ************

    username = browser.find_element_by_name("email")
    password = browser.find_element_by_name("password")
    username.send_keys("sultangndzz1@gmail.com")
    password.send_keys("Bestplayer1.")
    time.sleep(3)
    giris_yap = browser.find_element_by_xpath("//*[@id='loginForm']/p/button[1]/span")
    giris_yap.click()
    time.sleep(3)

    # ************* BILGILERLE OYNAYA BASIŞ ************
    oyna = browser.find_element_by_xpath("//*[@id='joinGame']/a/button")
    oyna.click()
    time.sleep(2)
    oyna2 = browser.find_element_by_xpath("//*[@id='accountlist']/div/div[1]/div[2]/div[1]/div/div[4]/div")
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
    # arena = browser.find_element_by_xpath("//*[@id='cooldown_bar_arena']/a")
    # zindan = browser.find_element_by_xpath("//*[@id='cooldown_bar_dungeon']/a")
    # egitim = browser.find_element_by_xpath("//*[@id='submenu1']/a[3]")
    altinString = browser.find_element_by_xpath("//*[@id='sstat_gold_val']").text
    altin = float(altinString)
    # ************* CAN BARI TANITIM ************
    canBariElement = browser.find_element_by_xpath("//*[@id='header_values_hp_percent']")
    canBariText = canBariElement.text
    canBariTextInt = int(canBariText[:len(canBariText) - 1])

    # ************** SURUKLEME YEMEK ***********
    yemekDiv = "//*[@id='inv']/div[1]"
    envanter = browser.find_element_by_xpath(yemekDiv)  # ENV ILK YERIkran parla

    karakter = browser.find_element_by_xpath("//*[@id='avatar']/div[2]")
    mouseSurukle = ActionChains(browser).drag_and_drop(envanter, karakter).release()
    KesifSeferi = browser.find_element_by_xpath("//*[@id='expeditionpoints_value_point']").text
    KesifSeferiHakki = int(KesifSeferi)
    i = 1
    while KesifSeferiHakki > 5:

        p.moveTo(1255, 204)
        p.click()
        canBariElement = browser.find_element_by_xpath("//*[@id='header_values_hp_percent']")
        canBariText = canBariElement.text
        canBariTextInt = int(canBariText[:len(canBariText) - 1])
        tecrube = browser.find_element_by_xpath("//*[@id='header_values_xp_percent']").text
        print(tecrube)
        if canBariTextInt < 20:
            canYenile(browser)
        else:
            if kesifAllowed:
                kesifSeferiYap(browser)
                KesifSeferi = browser.find_element_by_xpath("//*[@id='expeditionpoints_value_point']").text
                KesifSeferiHakki = int(KesifSeferi)
                levelKontrol(browser)
                time.sleep(1)

            zindann = browser.find_element_by_xpath("//*[@id='dungeonpoints_value_point']").text
            zindanHakki = int(zindann)
            if zindanHakki > 0 and zindanAllowed:
                try:
                    zindanYap(browser)
                    levelKontrol(browser)

                except Exception as e:
                    print("Zindan hatası")
                    send_msg("Zindan Yapılırken Hata.")
            sirkYap(browser)

            altin = browser.find_element_by_id("sstat_gold_val").text
            print("Altın Miktarı: " + altin)
            print(float(altin))
            if float(altin) > 2.000:
                #print("Altın miktarı fazla, bağış yapılıyor.")
                #paraBagisla(browser)
                send_msg("Paran 20kyı aştı!")
            muzayedeCheck(browser)
            genelDurum = browser.find_element_by_xpath("//*[@id='mainmenu']/a[1]")
            genelDurum.click()

            time.sleep(65)


basla(1, 1)
send_msg("Görevim bitti. Bilgisayar kapatılıyor.")
time.sleep(1)
os.system('shutdown -s')
