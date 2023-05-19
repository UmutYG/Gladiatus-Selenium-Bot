from Gladiatus_Bot import basla
print("dsasf")
import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QLabel, QPushButton, QComboBox
from PyQt5.QtGui import QPixmap, QFont

app = QApplication(sys.argv)

pencere = QWidget()

pencere.setWindowTitle("Gladiatus Bot v1.0")

pencere.setGeometry(100, 100, 1050, 550)
pencere.setStyleSheet("background : #2E2E2E")

bilgi = QLabel(pencere)
bilgi.setPixmap(QPixmap('Resim//hepsi2.PNG'))

bilgi.move(10, 120)

bilgi2 = QLabel(pencere)

bilgi2.setPixmap(QPixmap("Resim//ust.PNG"))
bilgi2.move(300, 5)

botuBaslatButon = QPushButton(pencere)
botuBaslatButon.setStyleSheet("background-color : #6C6B56; color:white")
botuBaslatButon.setFont(QFont('Times', 10))
botuBaslatButon.setText("Botu Başlat")
botuBaslatButon.setGeometry(5, 10, 290, 45)
print("dsasf")
botuBaslatButon.clicked.connect(lambda: basla(kesifTik, zindanTik))
kesifTik = 0
zindanTik = 0

def tikliMi():
    global kesifTik
    kesifTik = 1

def tikliMi2():
    global zindanTik
    zindanTik = 1


botuDurdurButon = QPushButton(pencere)
botuDurdurButon.setStyleSheet("background-color : #6C6B56; color:white")
botuDurdurButon.setFont(QFont('Times', 10))
botuDurdurButon.setText("Botu Durdur")
botuDurdurButon.setGeometry(5, 60, 290, 45)

kesifSeferiCheckBox = QCheckBox("Keşif Seferi", pencere)
kesifSeferiCheckBox.move(450, 210)
kesifSeferiCheckBox.setStyleSheet("color : white")
kesifSeferiCheckBox.clicked.connect(tikliMi)
kesifCombo = QComboBox(pencere)
kesifCombo.setGeometry(435, 250, 150, 35)
kesifCombo.setStyleSheet('color:white')
kesifCombo.addItem("1. Bölge")
kesifCombo.addItem("2. Bölge")
kesifCombo.addItem("3. Bölge")
kesifCombo.addItem("4. Bölge")
kesifCombo.addItem("5. Bölge")
kesifCombo.addItem("6. Bölge")
kesifCombo.addItem("7. Bölge")

ZindanCheckBox = QCheckBox("Zindan", pencere)
ZindanCheckBox.setStyleSheet("color : white")
ZindanCheckBox.move(750, 210)
ZindanCheckBox.clicked.connect(tikliMi2)
zindanCombo = QComboBox(pencere)
zindanCombo.setGeometry(735, 250, 150, 35)
zindanCombo.setStyleSheet('color:white')
zindanCombo.addItem("1. Bölge")
zindanCombo.addItem("2. Bölge")
zindanCombo.addItem("3. Bölge")
zindanCombo.addItem("4. Bölge")
zindanCombo.addItem("5. Bölge")
zindanCombo.addItem("6. Bölge")
zindanCombo.addItem("7. Bölge")

pencere.show()

sys.exit(app.exec_())
