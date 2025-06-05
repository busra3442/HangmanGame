import random

with open('word_list','r') as f: # dosyayı okuma modunda açtık as f diyerek f i takma ad yaptık
    words = f.readlines() # dosyadaki satırları tek tek okur ve words değişkenine atar

word = random.choice(words)[:-1] # son karakteri almaması için bunu yapıyoruz(:-1)


# word = "Secret" projeye böyle başladık ama daha eğlenceli ve işlevsel hale getirmek için
# random modülü ve bir kelime dosyası ile bilgisayarın rastegele seçim yapmasını isteyelim


# oyuncu bir harf bilirse hakkı değişmiyor ama eğer harfi yanlış tahmin ederse
# hakkı 1 azalıyor

allowed_errors = 7 # izin verilen hata sayısı
guesses = [] # tahminler listemiz başlangıçta boş koşullara göre ekliycez(append)
done = False # boolean ifademizi while döngüsünü kontrol etmek için kullanıcaz

while not done:
    for letter in word: # letter : harf
        if letter.lower() in guesses: # lower ın amacı harfin büyük küçük olmasını görmezden gelmek
            print(letter, end = " ") # end işlemi ile satır sonu yapmasını önleriz bir sonraki boşluğa atlar

        else:
            print("_", end = " ")

    print("") # kelime ile işimiz bittiğinde yeni bir satır yazdırıcaz

    guess = input(f"Allowed Errors Left {allowed_errors}, Next Guess: ") # kalan hata miktarını söyleyip sonraki tahmini alıcam
    guesses.append(guess.lower()) # alınan harfi tahminler listesine ekliyorum
    if guess.lower() not in word.lower(): # eğer tahmin edilen harf kelimede yoksa
        allowed_errors -= 1 # hata hakkım 1 azalıyor
        if allowed_errors == 0:
            break # hata hakkım 0 olursa while döngüsünden çıkılır

    done = True # aksi ispatlanana kadar kelimeyi bulduğumuzu varsaydığımız anlamına gelir
    for letter in word:
        if letter.lower() not in guesses: # eğer harf tahminler listesinde yoksa while döngüsü tekrar döner
            done = False

if done:
    print(f"You found the word! It was {word}!" )
else:
    print(f"Game Over! The word was {word}!")

