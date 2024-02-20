# 1. int: Tam sayıları temsil eder.
tam_sayi = 42

# 2. float: Ondalıklı sayıları temsil eder.
ondalikli_sayi = 3.14

# 3. str: Metin veya karakter dizilerini temsil eder.
metin = "Merhaba, Dünya!"

# 4. bool: Mantıksal değerleri (True veya False) temsil eder.
durum = True

# 5. list: Birden çok öğeyi içeren bir sıralı veri yapısıdır.
liste = [1, 2, 3, 4, 5]

# 6. tuple: Değiştirilemeyen bir sıralı veri yapısıdır.
demet = (1, 2, 3, 4, 5)

# 7. set: Benzersiz öğeleri içeren bir veri yapısıdır.
kume = {1, 2, 3, 4, 5}

# 8. dict: Anahtar-değer çiftlerini içeren bir veri yapısıdır.
sozluk = {"anahtar1": "deger1", "anahtar2": "deger2"}

# 9. NoneType: Bir değerin olmadığını belirtir.
degisken = None

# 10. byte: Tek bir byte'ı temsil eder.
byte_degeri = b'a'

# 11. bytearray: Değiştirilebilir bir byte dizisini temsil eder.
byte_dizisi = bytearray(b'hello')

# 12. complex: Karmaşık sayıları temsil eder.
kompleks_sayi = 3 + 4j

# 13. frozenset: Değiştirilemez bir küme yapısıdır.
donmus_kume = frozenset({1, 2, 3, 4, 5})

# 14. range: Ardışık bir sayı dizisini temsil eder.
aralik = range(0, 10)

# 15. memoryview: Nesnelerin dahili bellek görünümlerini sağlar.
bellek_gorunumu = memoryview(byte_dizisi)

# 16. ellipsis (...): Özel bir nesne, genellikle dilin özelliklerinde kullanılır.
nokta = ...

# 17. NotImplemented: Bir işlemin belirli bir operatörü desteklemediğini belirtmek için kullanılır.
# Örnek kullanım: 1 + 2i + 3 + 4i
not_implemented = NotImplemented

# 18. module: Python'daki bir modülü temsil eder.
import math
modul = math


# 1. capitalize(): Stringin ilk harfini büyük yapar
metin = "python"
buyuk_ilk_harf = metin.capitalize()

# 2. upper(): Stringin tüm karakterlerini büyük harfe dönüştürür
buyuk_metin = metin.upper()

# 3. lower(): Stringin tüm karakterlerini küçük harfe dönüştürür
kucuk_metin = metin.lower()

# 4. count(): Belirtilen alt dizenin string içinde kaç kez geçtiğini sayar
sayi_t = metin.count('t')

# 5. find(): Belirtilen alt dizenin başlangıç indeksini döndürür, yoksa -1 döndürür
index = metin.find('th')

# 6. replace(): Belirtilen alt dizenin tüm örneklerini başka bir dizeyle değiştirir
yeni_metin = metin.replace('py', 'Py')

# 7. split(): Belirtilen ayırıcıya göre stringi böler ve bir liste döndürür
kelimeler = metin.split(' ')

# 8. join(): Bir listedeki öğeleri bir string içinde birleştirir
liste = ['Python', 'Programlama']
birlesik_metin = ' '.join(liste)

# 9. strip(): Stringin başındaki ve sonundaki boşlukları kaldırır
duz_metin = "  Python  ".strip()

# 10. startswith(): Stringin belirtilen alt dizeyle başlayıp başlamadığını kontrol eder
if metin.startswith('py'):
    print("String 'py' ile başlıyor")

# 11. endswith(): Stringin belirtilen alt dizeyle bitip bitmediğini kontrol eder
if metin.endswith('on'):
    print("String 'on' ile bitiyor")

# 12. isalpha(): Stringin sadece alfabetik karakterler içerip içermediğini kontrol eder
if metin.isalpha():
    print("String sadece harflerden oluşuyor")

# 13. isdigit(): Stringin sadece rakamlar içerip içermediğini kontrol eder
if metin.isdigit():
    print("String sadece rakamlardan oluşuyor")

# 14. isalnum(): Stringin sadece alfasayısal karakterler içerip içermediğini kontrol eder
if metin.isalnum():
    print("String alfasayısal karakterlerden oluşuyor")

# 15. title(): Her kelimenin baş harfini büyük yapar
bas_harf_buyuk = metin.title()

# 16. swapcase(): Stringdeki büyük harfleri küçük, küçük harfleri büyük yapar
ters_metin = metin.swapcase()

# 17. center(): Stringi belirli bir genişliğe kadar belirtilen karakterlerle merkezler
merkezlenmis_metin = metin.center(20, '*')

# 18. ljust(): Stringi belirli bir genişliğe kadar sola yaslar ve sağa belirtilen karakterleri ekler
yaslanmis_metin = metin.ljust(15, '-')

# 19. rjust(): Stringi belirli bir genişliğe kadar sağa yaslar ve sola belirtilen karakterleri ekler
yaslanmis_metin = metin.rjust(15, '-')

# 20. zfill(): Stringin belirtilen genişliğe kadar başına sıfır ekler
zfill_metin = metin.zfill(10)

# 1. Karakter Dizilimi ve İndeksleme
metin = "Python"
ilk_karakter = metin[0]  # İlk karakteri seçer
son_karakter = metin[-1]  # Son karakteri seçer

# 2. String Dilimleme (Slicing)
alt_metin = metin[1:4]  # 1. indeksten 4. indekse kadar olan alt metni seçer

# 3. String Birleştirme (Concatenation)
birlesik_metin = metin + " Programlama"  # İki stringi birleştirir

# 4. String Uzunluğu
uzunluk = len(metin)  # Stringin karakter sayısını döndürür

# 5. String Dönüşüm (Conversion)
sayi = 42
sayi_str = str(sayi)  # Bir sayıyı stringe dönüştürür

# 6. String Karakter Dizilerini Arama
index = metin.find('th')  # 'th' karakter dizisinin indeksini bulur

# 7. String Karakterlerini Değiştirme ve Silme
yeni_metin = metin.replace('Py', 'Jy')  # 'Py' ifadesini 'Jy' ile değiştirir

# 8. String Büyüklük ve Küçüklük
buyuk_metin = metin.upper()  # Tüm harfleri büyük harfe dönüştürür
kucuk_metin = metin.lower()  # Tüm harfleri küçük harfe dönüştürür

# 9. String Formatlama
isim = "Ahmet"
yas = 30
formatli_metin = "Benim adım {} ve {} yaşındayım.".format(isim, yas)  # Değişkenleri string içine yerleştirir

# 10. String Karakterlerinin Kontrolü
if metin.isalpha():  # Metin sadece alfabetik karakterler içeriyorsa
    print("Metin sadece harflerden oluşuyor.")

# 11. String Karakterlerini Ayırma ve Birleştirme
parcalar = metin.split('t')  # 't' karakteriyle metni ayırır

# 12. String Karakterlerini Ters Çevirme
ters_metin = metin[::-1]  # Stringi ters çevirir

# 13. Karakterlerin Sayısını Hesaplama
sayi_t = metin.count('t')  # 't' karakterinin metin içinde kaç kez geçtiğini sayar

# 14. Başlangıç ve Bitiş Kontrolü
if metin.startswith('Py'):  # Metin 'Py' ile başlıyorsa
    print("Metin 'Py' ile başlıyor.")

# 15. Boşlukları Kaldırma
duz_metin = "  Python  "
duz_metin = duz_metin.strip()  # Stringin başındaki ve sonundaki boşlukları kaldırır


# 16. Karakterlerin İndeksini Bulma
index_of_t = metin.index('t')  # 't' karakterinin indeksini bulur

# 17. Karakterleri Tersine Çevirme
ters_metin = reversed(metin)  # Stringin karakterlerini tersine çevirir

# 18. Karakterlerin Alfabetik Sıralama
alfabetik_sirali_metin = sorted(metin)  # Stringin karakterlerini alfabetik olarak sıralar

# 19. İlk Harfi Büyük Yapma
bas_harf_buyuk = metin.capitalize()  # Stringin ilk harfini büyük yapar

# 20. Sayıları Stringe Dönüştürme
sayi_str = ''.join(str(sayi) for sayi in range(10))  # 0'dan 9'a kadar olan sayıları stringe dönüştürür



##Listelerle çalışmak



