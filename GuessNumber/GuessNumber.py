import random
counter=0
bil=False
while True:
    number = random.randint(1,10)
    print("Bir sayı giriniz")
    while counter<4: 
        n = input()
        if int(n) == number:
            print("Bravoo !")
            bil=True
            input()
            break
            pass
        elif int(n)<number:
            print("Daha Büyük Bir Sayı Giriniz !")
            counter=counter+1
            pass
        elif int(n)>number:
            print("Daha Küçük Bir Sayı Giriniz !")
            counter=counter+1
            pass
        pass
    counter=0
    if bil==False:
        print("Üzgünüz Bilemediniz, Tahmin Hakkınız Bitti !")
        input()
        pass
    else: 
        bil=False
    pass
