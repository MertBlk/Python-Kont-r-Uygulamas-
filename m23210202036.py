def kontor_al(kontor_miktari):
    while True:
        try:
            alinan_kontor = int(input("Kontör miktarı giriniz: "))
            if alinan_kontor < 0 or alinan_kontor >= 120:
                print("0'dan küçük 120'den büyük değer girilmez.")
            else:
                kontor_miktari += alinan_kontor
                print(f"{alinan_kontor} liralık kontör aldınız.")
                break
        except ValueError:
            print("Geçersiz değer girildi, lütfen tekrar deneyin.")
    return kontor_miktari


def gorusme_yap(kontor_miktari, gorusme_suresi, toplam_gorusme_suresi):
    if kontor_miktari < gorusme_suresi * 0.12:
        print("Telefonda yeterli kontör olmadığı için görüşme yapamazsınız.")
        return kontor_miktari, toplam_gorusme_suresi  # Toplam görüşme süresini de döndürüyoruz
    else:
        kontor_miktari -= gorusme_suresi * 0.12
        toplam_gorusme_suresi += gorusme_suresi  # Toplam görüşme süresine ekleme yapılıyor
        print(f"{gorusme_suresi} dakika görüşme yaptınız.")
        print(f"Toplam {toplam_gorusme_suresi} dakika görüşme yaptınız.")  # Toplam görüşme süresi yazdırılıyor
        
        return kontor_miktari, toplam_gorusme_suresi  # Güncellenmiş kontör ve toplam görüşme süresini döndürüyoruz
    

def kontor_bilgisi(kontor_miktari):
    print("Telefonda {:.1f} liralık kontör vardır.".format(kontor_miktari))


def gorusme_bilgisi(toplam_gorusme_suresi):
    print(f"Toplam {toplam_gorusme_suresi} dakika görüşme yaptınız.")


kontor_miktari = 0.0
toplam_gorusme_suresi = 0

while True:
    print("\n--- Telefon Uygulaması ---")
    print("1- Kontör Al")
    print("2- Görüşme Yap")
    print("3- Bilgiler")
    print("9- Çıkış")
    secim = input("\nSeçiminiz: ")

    if secim == "1":
        kontor_miktari = kontor_al(kontor_miktari)
    elif secim == "2":
        try:
            gorusme_suresi = int(input("Kaç dakika görüşme yapacaksınız: "))
            kontor_miktari, toplam_gorusme_suresi = gorusme_yap(kontor_miktari, gorusme_suresi, toplam_gorusme_suresi)
        except ValueError:
            print("Geçersiz değer girildi, lütfen tekrar deneyin.")
    elif secim == "3":
        while True:
            print("\n--- Bilgi Menüsü ---")
            print("1- Kontör Bilgisi")
            print("2- Görüşme Bilgisi")
            print("9- Çıkış")
            menu_secim = input("\nSeçiminiz: ")
            if menu_secim == "1":
                kontor_bilgisi(kontor_miktari)
            elif menu_secim == "2":
                gorusme_bilgisi(toplam_gorusme_suresi)
            elif menu_secim == "9":
                break
            else:
                print("Geçersiz bir seçim yaptınız.")
    elif secim == "9":
        print("Çıkış yaptınız.")
        break
    else:
        print("Geçersiz bir seçim yaptınız.")
