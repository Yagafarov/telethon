# Telegram Ma'lumotlar Yuklab Olish va Tafsilotlar Faylini Yaratish

Ushbu Python skripti belgilangan bir Telegram suhbatini kuzatib borib, media fayllarini yuklab olishni va suhbat tafsilotlarini JSON fayliga saqlashni amalga oshiradi. Shuningdek, har bir yuklab olingan faylning tafsilotlarini o'z ichiga olgan matn faylini ham yaratadi.

## O'rnatish

1. Repositoryni ko'chirib oling:
```bash
git clone https://github.com/yagafarov/telethon.git
cd sizningreponingiz
```
```bash
python -m venv venv
source venv/bin/activate
```
## Foydalanish

1. Telegram API kalitlarini `config.py` fayliga kiriting.
2. Python skriptini ishga tushiring.
3. Telegramda kuzatmoqchi bo'lgan suhbatni toping.
4. Yuklab olishni xohlagan media turlari bo'yicha ma'lum etilgan teglarga ega bo'lgan xabarlarni yuboring.

## Talablar

- Python 3.x
- [Telethon](https://github.com/telethon/telethon) kutubxonasi
- Telegram API kalitlari

## Fayl Tuzilishi

- `config.py`: Telegram API kalitlarini o'z ichiga olgan fayl.
- `listen.py`: Asosiy Python skripti.
- `README.md`: Ushbu fayl.
- `<yuklab olgan suhbat nomi>/`
  - `images/`: Yuklab olingan tasvir fayllari uchun papka.
  - `videos/`: Yuklab olingan video fayllari uchun papka.
  - `audios/`: Yuklab olingan ovoz fayllari uchun papka.
  - `files/`: Qolgan yuklab olingan fayllar uchun papka.
  - `downloaded_data_details.txt`: Yuklab olingan media fayllarining tafsilotlarini o'z ichiga olgan matn fayli.
- `dialogs.json`: Kuzatilgan suhbatlar tafsilotlarini o'z ichiga olgan JSON fayli.

## Namuna Foydalanish

1. `#yukla SuhbatNomi`: Yuklab olishni istagan suhbat nomini belgilay, media fayllarini yuklab oling.
2. `#yukla SuhbatFoydalanuvchiNomi`: Yuklab olishni istagan suhbat foydalanuvchining nomini belgilay, media fayllarini yuklab oling.
3. `#yukla SuhbatID`: Yuklab olishni istagan suhbatning ID sini belgilay, media fayllarini yuklab oling.

## Ruxsatnoma

Ushbu skript [MIT Ruxsatnomasi](https://opensource.org/licenses/MIT) bilan litsenziyalangan.
