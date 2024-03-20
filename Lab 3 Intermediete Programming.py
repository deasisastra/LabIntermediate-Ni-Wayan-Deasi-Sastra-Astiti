def guest_secret_word(kata_rahasia) :
    tebakan_huruf = []
    kesempatan = 8    

    print("Selamat Datang di Hangman!")
    print("Coba untuk menebak kata")
    
    while kesempatan > 0:
        guess = input("Tebak huruf dalam kata rahasia: ")

        if len(guess) != 1:
            print("Beri saya satu huruf.")
        elif not guess.isalpha():
            print("Beri saya satu huruf.")
        elif guess.lower() in tebakan_huruf:
            print("Anda sudah menebak huruf tersebut.")
        else:
            tebakan_huruf.append(guess.lower())
            if guess.lower() in kata_rahasia.lower():
                print("Selamat, anda menebak satu huruf!")
            else:
                kesempatan -= 1
                print("Semoga beruntung, anda memiliki {} kesempatan lagi.".format(kesempatan))
        display = ""
        for letter in kata_rahasia:
            if letter.lower() in tebakan_huruf:
                display += letter
            else:
                display += "_"
        print(display)
        if "_" not in display:
            print("Selamat! Anda telah menebak Kata:", kata_rahasia)
            break
        if kesempatan == 0:
            print("Maaf, anda gagal menebak. Katanya adalah:", kata_rahasia)
kata_rahasia="Mempertanggungjawabkan"
guest_secret_word(kata_rahasia)