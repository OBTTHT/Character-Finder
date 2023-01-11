from random import randint
import time
ozellikler = ["neşeli","kurnaz","gözü açık","ileri görüşlü","dürüst","duygusal","çalışkan","fedakar","kanaatkar","açık sözlü","dışa dönük","içine kapanık"]
name = str(input("Adınızı Giriniz: "))
print("Bekle! Seni Tanımaya Çalışıyorum...")
time.sleep(0.6)
r = randint(0,len(ozellikler)-1)
print("Acaba Hangi Özelliğe Sahipsin ?")
for item in ozellikler:
    time.sleep(0.3)
    print("-",item)
print("...")
time.sleep(1.5)
print("bence sen {} birisisin".format(ozellikler[r]))