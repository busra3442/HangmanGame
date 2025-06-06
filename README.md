# 🕵️‍♂️ Word Guessing Game / Hangman Game

Python ile yazılmış basit bir kelime tahmin (hangman tarzı) oyunudur. Bilgisayar, `word_list` adlı dosyadan rastgele bir kelime seçer ve oyuncudan bu kelimeyi harf harf tahmin etmesini ister.

## 🎮 Oyun Kuralları

- Bilgisayar rastgele bir kelime seçer.
- Oyuncu her turda bir harf tahmin eder.
- Doğru tahminlerde hata hakkı azalmaz.
- Yanlış tahminlerde hata hakkı 1 azalır.
- Toplam 7 yanlış yapma hakkınız vardır.
- Kelimenin tüm harfleri doğru tahmin edilirse oyunu kazanırsınız.
- Tüm haklar biterse oyun sona erer.

## 📂 Dosyalar

- `game.py` → Oyun mantığını içeren Python dosyası.
- `word_list` → Her satırında bir kelime bulunan metin dosyası. Bilgisayar bu dosyadan rastgele kelime seçer.

## 💡 Özellikler

- Küçük/büyük harf duyarsız tahmin.
- Dinamik kelime seçimi (`word_list` dosyasından).
- Tahmin edilen harflerin ekranda gösterimi.
- Basit terminal arayüzü.



