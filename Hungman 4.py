import random
score = 0

def select_word() :
    kata_rahasia= ["Mempertanggungjawabkan", "Berencana", "Bepergian", "Berseluncur", "Pemandangan", "Pegunungan", "Laboratorium", "Perkakas", "Belalai", "Surabaya"]
    secretword = kata_rahasia[random.randint(0,len(kata_rahasia)-1)]
    kata_rahasia.remove(secretword)
    return secretword

def guest_secret_word() :
    global score
    kata_rahasia = select_word()
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
            print("Selamat! Anda telah menebak Kata (win):", kata_rahasia)
            score += 1  
            print("Skor Anda saat ini:", score)
            break
        if kesempatan == 0:
            print("Maaf, anda gagal menebak (Lose). Katanya adalah:", kata_rahasia)
def main_lagi() :
    while 1 :
        play = input ("Mau main lagi? (yes/no):"). lower()
        if play == 'yes':
            guest_secret_word() 
        elif play == 'no' :
            print ("Terimakasih telah bermain")
            break
        else :
            print ("please input yes or no")

guest_secret_word()
main_lagi()