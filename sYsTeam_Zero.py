print("""




█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█         
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█    to sYsTeam Zero
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█          







┌─────         •✧✧•      •✧✧•      •✧✧•      •✧✧•     •✧✧•    •✧✧•                   ─────┐
 Bu bir program değil sistemdir. Sisteme hesap oluşturmanın ardından
sisteme giriş yapacaksınız ve 7 tane matematiksel programa ulaşıp istediğinizi
ihtiyacınız olduğu kadar kullanarak kapatma imkanı sunulan bir sisteme giriş yapmış olacaksınız 
└─────            •✧✧•     •✧✧• •✧✧•   •✧✧•   •✧✧•   •✧✧•                            ─────┘





»»————-　★　————-«« Bunlardan yedincisi olan hesap makinesinde 8 adet işlem bulunmaktadır »»————-　★　————-««
[1] Toplama işlemi

[2] Çıkartma işlemi

[3] Çarpma işlemi

[4] Bölme işlemi

[5] Üslü ifadeleri hesaplama işlemi

[6] Faktoriyel bulma

[7] EBOB bulma

[8] EKOK bulma
»»————-　★　————-«« Profesyonel bir hesap makinası olması sebebiyle farklı farklı işlemler yapabilirsiniz »»————-　★　————-««

şimdi sayfayı en aşağıya kaydırarak başlayabilirsiniz

████─────────────────────────────████
───██████────────░█───█░────────██████
────██?▓████─────██───██─────████▓?██
─────██?░░▓███─────█─█─────███▓░░?██
─────██?░░░░▓███───█─█───███▓░░░░?██
──────██?░?░░░▓██──███──██▓░░░?░?██
──────██?░░░?░░▓███─█─██▓░░░?░░░?██
─────██?░░?░░░?░░▓█████▓░░?░░░?░░?██
─────██?░░░░░░░░?░▓███▓░?░░░░░░░░?██
─────█████████▒░░░░▓█▓░░░░▒█████████
───────█████████▒░░▒█▒░░▒█████████
────███?░░░░░░░██░░▓█▓░░██░░░░░░░?███
─────███?░░?░?░░░░░███░░░░░?░?░░?███
───────██?░░░░░?░░▓███▓░░?░░░░░?██
────────██?░?░░░░▓█████▓░░░░?░?██
────────██?░░░▓████─█─████▓░░░?██
─────────██?▓███────█────███▓?██
─────────██████───────────██████
──────────███──────────────████


""")


print("Bir hesap oluşturun")
hsp = input("kullanıcı adı belirleyin:")
mail = input("E-Mail adresinizi giriniz:")
password = input("Parolanızı belirleyiniz:")
for k in range(4):
    print("hesap oluşturuluyor ....")
print("hesap oluşturma işlemi başarılı. Şimdi giriş yapınız")

defkullanici = hsp
defparola = password

def login():
    global defparola
    while (True):
        kullanici = input("kullanıcı adınızı giriniz:")
        parola = input("parolanızı giriniz:")

        if ((kullanici == defkullanici) and ((parola == defparola))):
            print(" giriş yapılıyor ...")
            print(" giriş yapılıyor ...")
            time.sleep(3)
            print("GİRİŞ BAŞARILI")

            break

        elif ((kullanici != defkullanici) and ((parola == defparola))):
            print("kullanıcı adınızı yanlış girdiniz")
            print("lütfen tekrar deneyiniz")

        elif ((kullanici == defkullanici) and ((parola != defparola))):
            print("şifrenizi yanlış girdiniz")
            print("şifrenizi değiştirmek ister misiniz? (E/H)")

            cevap = input()
            if cevap == "E":
                print("Yeni şifrenizi giriniz:")
                defparola = input()
                for x in (range(int((4)))):
                    print("şifreniz kaydediliyor ......")
                print("ŞİFRENİZ KAYDEDİLDİ.")
                print("Şimdi tekrar deneyin")

        else:
            print("GİRİŞ BAŞARISIZ")
            print("lütfen tekrar deneyin")



def hacimbulma():
    print("hesaplamak istediğiniz şekli 'küre' , 'küp','silindir','dikdörtgenler prizması','koni','kare piramit'"
          ",'üçgen prizma','dikdörtgen prizma' şeklinde yazınız:")
    sekil = input()
    if sekil == "küre":
      r =  int(input("yarıçap r değerini giriniz:"))
      hacim = ((4/3)*3.14*(r**3))
      print("kürenizin hacmi:"),hacim
      return (hacim)

    elif sekil == "küp":
        a = int(input("küpe bir kenar uzunluğu veriniz:"))
        hacim = (a**3)
        print("küpün hacmi:"),hacim
        return (hacim)

    elif sekil == "silindir":
        r1 = int(input("silindirin dairelerinin yarı çapını giriniz:"))
        h = int(input("silindirin yüksekliğini giriniz:"))
        hacim = 3.14 * r1**2 * h
        print("silindirin hacmi :"),hacim
        return (hacim)

    elif sekil == "dikdörtgenler prizması":
        uzunluk = int(input("dikdörtgenler prizmasının uzunluğunu giriniz:"))
        yukseklik = int(input("dikdörtgenler prizmasının yüksekliğini giriniz:"))
        genislik = int(input(" dikdörtgenler prizmasının genişliğini giriniz:"))
        hacim = uzunluk*yukseklik*genislik
        print("dikdörtgenler prizmasının hacmi:"),hacim
        return (hacim)

    elif sekil == "koni":
        r = int(input("Koninin yarıçap r değerini giriniz:"))
        h = int(input("Koninin yüksekliğini giriniz:"))
        hacim = (1/3)*(3.14)*(r**2)*(h)
        print("Koninin hacmi :")
        return (hacim)

    elif sekil == "kare piramit":
        # g * u = taban alanı ve taban alanı * yükseklik / 3 = piramit formülü
        g = int(input("piramidin genişliğini giriniz:"))
        u = int(input("piramidin uzunluğunu giriniz:"))
        h = int(input("piramidin yüksekliğini giriniz:"))
        hacim = ((g * u) * (h)) / 3
        print("piramitin hacmi :")
        return(hacim)

    elif sekil == "üçgen prizma":
        ucgentaban = int(input("üçgen prizmanın üçgenlerinden bir tanesinin tabanını giriniz :"))
        ucgenhight = int(input("üçgen prizmanın üçgenlerinden bir tanesinin yüksekliğini giriniz:"))
        uzunluk = int(input("üçgen prizmanın taban uzunluğunu giriniz:"))
        hacim = ((ucgentaban * ucgenhight)/2) * uzunluk
        return hacim

    elif sekil == "dikdörtgen prizma":
        uzunluk = int(input("Dikdörtgen prizmanızın uzunluğunu giriniz:"))
        genislik = int(input("Dikdörtgen prizmanızın genişliğini giriniz"))
        hight = int(input("Dikdörtgen prizmanızın yüksekliğini giriniz"))
        hacim = uzunluk * hight * genislik
        return hacim

    else:
        print("lütfen listede verilenlerden birini giriniz. Harf çeşitleri önemlidir")

def alanhesaplama():
    print("alanını hesaplamak istediğiniz şekli giriniz.[Daire , Kare , Dikdörtgen , Paralelkenar , Üçgen(eşkenar) , Yamuk , Silindir]")
    sekil = input()
    if sekil == ("Daire"):
        r = int(input("bir yarıçap r değeri giriniz:"))
        alan = (3.14*r**2)
        print("Dairenizin alanı :"),alan
        return(alan)

    elif sekil == ("Kare"):
        kenar = int(input("karenin bir kenarının uzunluğunu giriniz:"))
        alan = kenar**2
        print("karenizin alanı :"),alan
        return alan

    elif sekil == ("Dikdörtgen"):
        uk = int(input("uzun kenarın uzunluğunu giriniz:"))
        kk = int(input("kısa kenarın uzunluğunu giriniz:"))
        alan = (uk+kk)*2
        print("Dikdörtgeninizin alanı :"),alan
        return alan

    elif sekil == ("Paralelkenar"):
        taban = int(input("taban uzunluğunu giriniz:"))
        yukseklik = int(input("paralelkenarın yüksekliğini giriniz:"))
        alan = (taban*yukseklik)
        print("paralelkenarınızın uzunluğu :"),alan
        return alan

    elif sekil == ("Üçgen"):
        bk = int(input("üçgenin bir kenar uzunluğunu giriniz :"))
        alan = bk*bk
        print("üçgeninizin alanı :"),alan
        return alan

    elif sekil == ("Yamuk"):
        taban1 = int(input("birinci taban uzunluğunu giriniz:"))
        taban2 = int(input("ikinci taban uzunluğunu giriniz:"))
        h = int(input("yamuğun yüksekliğini giriniz:"))
        alan = (taban1 + taban2)*h/2
        print("yamuğunuzun alanı :"),alan
        return alan

    elif sekil == ("Silindir"):
        yaricap_r = int(input("Silindirin yarıçap r değerini giriniz:"))
        h = int(input("Silindirin yüksekliğini giriniz:"))
        alan = (2*3.14) + (yaricap_r + h)
        print("silinidirinizin alanı :"),alan
        return alan

    else:
        print("lütfen listede verilenlerden birini giriniz. Harf çeşitleri önemlidir")

def cevrehesaplama():
    print("Çevresini hesaplamak istediğiniz şekli giriniz.('çember'),('dikdörtgen'),('kare'),('eşkenar üçgen')"
          "('beşgen'),('algıgen')")
    sekil = input()
    if sekil == "çember":
        r = int(input("çemberin yarıçap (r) değerini giriniz:"))
        cevre = 2*3.14*r
        print("Çemberinizin çevresi :"),cevre
        return cevre

    elif sekil == "dikdörtgen":
        u = int(input("Dikdörtgenin uzun kenarının uzunluğunu giriniz:"))
        k = int(input("Dikdörtgenin kısa kenarının uzunluğunu giriniz:"))
        cevre = 2*(u + k)
        print("Dikdörtgeninizin çevresi :"),cevre
        return cevre

    elif sekil == "kare":
        a = int(input("karenin bir kenarının uzunluğunu giriniz:"))
        cevre = a*4
        print("Karenizin çevresi :"),cevre
        return cevre

    elif sekil == "eşkenar üçgen":
        a = int(input("eşkenar üçgenin bir kenarının uzunluğunu giriniz :"))
        cevre = a*3
        print("Üçgeninizin çevresi :"),cevre
        return cevre

    elif sekil == "beşgen":
        a = int(input("beşgenin  bir kenarının uzunluğunu giriniz  :"))
        cevre = a*5
        print("beşgeninizin çevresi :"),cevre
        return cevre

    elif sekil == "altıgen":
        a = int(input("Altıgenin bir kenarının uzunluğunu giriniz:"))
        cevre = a*6
        print("altıgeninizin çevresi :"),cevre
        return cevre

    else:
        print("lütfen listede verilen şekillerden birini giriniz")



def asal_sayi_bulma():

    a = int(input("Sayınızı giriniz:"))

    asal = 1
    for bolen in range(2, a):
        if a % bolen == 0:
            print("sayınız asal değildir")
            asal = 0
            break

    if asal == 1:
        print("sayınız asaldır")





#asal = 1 yazarak aslında true varsayım yapılıyor. Sonra for döngüsünde a bolen(c olsun)c'ye tam bölününce asalı
#sıfırlıyor. Sonra baktın asal = 1 demekki bir değişim olmamış. Bu for döngüsü gerçekleşmemiş içindeki tam bölünme
#olayı gerçekleşmemiş , asal olduğunu anlıyor.


def tam_bolen_bulma():
    a = int(input("Tam bölenlerini bulmak istediğiniz sayıyı giriniz :"))
    liste = []
    for c in range (1,a) :
        if (a % c) == 0:
            liste.append(c)
    return liste
#1 rakamından girilen sayıya kadar listeye atıyor. a % c = 0 olanları yani tam bölünenleri append ederek tam böleni buluyor


def karekokhesaplama():
    a = int(input("Karekökünü bulmak istediğiniz sayıyı giriniz :"))
    import math

    return math.sqrt(a)


def hesapmakinesi():
    print("""

    **********************************************************

    ________________Hesap Makinesi'ne hoşgeldiniz_________________

    [1] Toplama işlemi

    [2] Çıkartma işlemi

    [3] Çarpma işlemi

    [4] Bölme işlemi

    [5] Üslü ifadeleri hesaplama işlemi

    [6] Faktoriyel bulma

    [7] EBOB bulma

    [8] EKOK bulma



    **********************************************************

    """)
    import math
    import time
    data = int(input("Yapmak istediğiniz işlemin numarasını giriniz:"))
    time.sleep(1)
    if data == 1:

        a = int(input("a değerini giriniz:"))
        b = int(input("b değerini giriniz:"))
        m = input("bir değişken daha oluşturmak istiyorsanız (oluştur) yazabilirsiniz. Devam etmek için 'enter'")

        if m == "oluştur":
            c = int(input("c değerini giriniz:"))
            return (a + b + c)


        else:
            return (a + b)



    elif data == 2:

        time.sleep(1)
        a = int(input("a değerini giriniz:"))
        b = int(input("b değerini giriniz:"))
        m = input("bir değişken daha oluşturmak istiyorsanız (oluştur) yazabilirsiniz. Devam etmek için 'enter'")

        if m == "oluştur":
            c = int(input("c değerini giriniz:"))
            return (a - b - c)

        else:
            return (a - b)

    elif data == 3:

        time.sleep(1)
        a = int(input("a değerini giriniz:"))
        b = int(input("b değerini giriniz:"))
        m = input("bir değişken daha oluşturmak istiyorsanız (oluştur) yazabilirsiniz. Devam etmek için 'enter'")

        if m == "oluştur":
            c = int(input("c değerini giriniz:"))
            return (a * b * c)

        else:
            return (a * b)


    elif data == 4:

        time.sleep(1)
        a = int(input("a değerini giriniz:"))
        b = int(input("b değerini giriniz:"))
        m = input("bir değişken daha oluşturmak istiyorsanız (oluştur) yazabilirsiniz. Devam etmek için 'enter'")

        if m == "oluştur":
            c = int(input("c değerini giriniz:"))
            return (a / b / c)

        else:
            return (a / b)


    elif data == 5:

        time.sleep(1)
        a = int(input("a değerini giriniz:"))
        b = int(input("b değerini giriniz:"))

        return a ** b


    elif data == 6:
        time.sleep(1)
        a = int(input("Faktoriyelini bulmak istediğiniz sayıyı giriniz:"))

        return ("Sayınızın faktoriyeli :", math.factorial(a))



    elif data == 7:
        time.sleep(1)
        a = int(input("Birinci sayıyı giriniz :"))
        b = int(input("ikinci sayıyı giriniz:"))
        return math.gcd(a, b)


    elif data == 8:
        def ekok_bulma(sayi1, sayi2):
            i = 2
            ekok = 1
            while True:
                if (sayi1 % i == 0 and sayi2 % i == 0):
                    ekok *= i

                    sayi1 //= i
                    sayi2 //= i


                elif (sayi1 % i == 0 and sayi2 % i != 0):
                    ekok *= i

                    sayi1 //= i


                elif (sayi1 % i != 0 and sayi2 % i == 0):
                    ekok *= i

                    sayi2 //= i
                else:
                    i += 1
                if (sayi1 == 1 and sayi2 == 1):
                    break
            return ekok

        sayi1 = int(input("Sayı-1:"))
        sayi2 = int(input("Sayı-2:"))

        print("Ekok:", ekok_bulma(sayi1, sayi2))






""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""












import time


while (True):
    print(login())

    break

while (True):
    choice = input("bir program seçin [ Hacim bulma ] / [ Alan bulma ] / [ Çevre bulma ]"
                   " / [ Asal sayı kontrol ] / [ Tam bölen bulma ]"
                   " / [ Karekök hesaplama ] / [ hesap makinesi ]\n'SİSTEMİ KAPAT' yazarak sistemi kapayabilirsiniz")
    time.sleep(1)
    if choice == "Hacim bulma":

            while True:
                print(hacimbulma())
                kapama = input(
                    "'kapat' yazarak hacim bulma programımızı kapatabilirsiniz. Devam etmek için herhangi bir tuşa basınız")
                if kapama == "kapat":
                    for p in (range(3)):
                        print("çıkış yapılıyor...")
                        time.sleep(0.4)
                    break



    elif choice == "Alan bulma":

            while True:
                print(alanhesaplama())
                kapama = input(
                    "'kapat' yazarak alan bulma programımızı kapatabilirsiniz. Devam etmek için herhangi bir tuşa basınız")
                if kapama == "kapat":
                    for p in (range(3)):
                        print("çıkış yapılıyor...")
                        time.sleep(0.4)
                    break


    elif choice == "Çevre bulma":


        while True:
            print(cevrehesaplama())
            kapama = input("'kapat' yazarak çevre bulma programımızı kapatabilirsiniz. Devam etmek için herhangi bir"
                           "tuşa basınız")
            if kapama == "kapat":
                for p in (range(3)):
                    print("çıkış yapılıyor ...")
                    time.sleep(0.4)
                break

    elif choice == "SİSTEMİ KAPAT":
        for i in range(3):
            print("sYstem Zero kapatılıyor  ......")
            time.sleep(0.4)
        print("""
_░▒███████
░██▓▒░░▒▓██
██▓▒░__░▒▓██___██████
██▓▒░____░▓███▓__░▒▓██
██▓▒░___░▓██▓_____░▒▓██
██▓▒░_______________░▒▓██
_██▓▒░______________░▒▓██
__██▓▒░____________░▒▓██
___██▓▒░__________░▒▓██
____██▓▒░________░▒▓██
_____██▓▒░_____░▒▓██
______██▓▒░__░▒▓██
_______█▓▒░░▒▓██
________░▒▓██
______░▒▓██
____░▒▓██
        
        
        """)
        break


    elif choice == "Asal sayı kontrol":
        while True:
            print(asal_sayi_bulma())
            kapama = input("'kapat' yazarak asal sayı kontrol programımızı kapatabilirsiniz. Devam etmek için herhangi bir"
                           "tuşa basınız")
            if kapama == "kapat":
                for p in (range(3)):
                    print("çıkış yapılıyor ...")
                    time.sleep(0.4)
                break

    elif choice == "Tam bölen bulma":
        while True:
            print(tam_bolen_bulma())
            kapama = input(
                "'kapat' yazarak tam bölen bulma programımızı kapatabilirsiniz. Devam etmek için herhangi bir"
                "tuşa basınız")
            if kapama == "kapat":
                for p in (range(3)):
                    print("çıkış yapılıyor ...")
                    time.sleep(0.4)
                break



    elif choice == "Karekök hesaplama":
        while True:
            print(karekokhesaplama())
            kapama = input(
                "'kapat' yazarak karekök hesaplama bulma programımızı kapatabilirsiniz. Devam etmek için herhangi bir"
                "tuşa basınız")
            if kapama == "kapat":
                for p in (range(3)):
                    print("çıkış yapılıyor ...")
                    time.sleep(0.4)
                break


    elif choice == "hesap makinesi":
        while True :


            print(hesapmakinesi())

            kapama = input(
                "'kapat' ile hesap makinesini kapatabilirsiniz. Devam etmek için 'rastgele "
                "tuşa basınız")
            if kapama == "kapat":
                for p in (range(3)):
                    print("çıkış yapılıyor ...")
                    time.sleep(0.2)
                break





    else:
        print("Lütfen girmek istediğiniz programın ismini doğru giriniz. Büyük küçük harf uyumu önemlidir")




















