# Freedom Fighters - %100 Türkçe Yama (Glacier Engine)

![Oyun](https://img.shields.io/badge/Freedom%20Fighters-Türkçe%20Yama-red?style=for-the-badge)
![Uyumluluk](https://img.shields.io/badge/Uyumluluk-Steam%20%7C%20Epic%20Games%20%7C%20GOG-blue?style=for-the-badge)
![Çeviri](https://img.shields.io/badge/%C3%87eviri%20Oran%C4%B1-%25100-success?style=for-the-badge)
![Lisans](https://img.shields.io/badge/Lisans-MIT-green?style=for-the-badge)

IO Interactive tarafından Glacier 1 oyun motoruyla geliştirilen efsanevi **Freedom Fighters** oyunu için hazırlanmış, oyunun tüm metinlerini, ara sahnelerini, görev hedeflerini, menülerini ve tüm oyun içi çatışma/telsiz seslerini kapsayan **%100 eksiksiz Türkçe Yama** çalışmasıdır.

---

## 🌟 Yama Özellikleri

- **%100 Eksiksiz Çeviri:**
  - **Ana Menü ve Ayarlar:** Kontroller, grafik/ses ayarları, zorluk seviyeleri, kayıt/yükleme arayüzü.
  - **Ara Sahneler ve Hikaye (MovieCuts):** Açılış zaman çizelgesi, haber bültenleri (Tatiana Kempinski), Chris Stone'un televizyon yayını konuşması ve tüm sinematikler.
  - **Görevler ve Harita Bilgilendirmeleri:** Her bölüm için brifingler, debrifingler, taktiksel ipuçları, hedef açıklamaları ve harita etiketleri.
  - **Eğitim ve Kontrol İpuçları:** Karizma sistemi, tim yönetimi, C4 yerleştirme, sağlık çantası kullanımı vb.
  - **Tüm Oyun İçi Çatışma ve Karakter Replikleri:**
    - Özgürlük Savaşçıları (Tim üyelerinin tüm emir, hücum, pusu, şarjör ve destek replikleri)
    - Siviller (Yardım isteme, teşekkür, araba uyarıları ve taktik ipuçları)
    - Taraf Değiştirenler (Defectors - Sovyet safından direnişe geçenlerin özel replikleri)
    - Sovyet Askerleri (Devriye diyalogları, çatışma naraları, telsiz anonsları)
    - Mahkumlar (Hücre kurtarma diyalogları)
    - Chris Stone'un tim emirleri ("Hücum!", "Toplanın!", "Mevzi alın!", "Sakin ol, nefes al")

---

## 🛡️ Özel İsim ve Karakter Uyumluluk Politikası

1. **Özel İsimler Korunmuştur:**
   - Karakter isimleri, unvanlar ve tarihi/coğrafi yer adları evrensel kurguyu bozmamak adına orijinal bırakılmıştır:
     - *Christopher "Chris" Stone, Troy Stone, Isabella Angelina, Mr. Jones, Phil, Kid, Bagzton, General Tatarin, Colonel Bulba*
     - *Manhattan, Brooklyn, Fort Jay, Governor's Island, Yonkers, SAFN Studios vb.*
2. **ASCII Türkçe Uyumluluğu:**
   - Glacier 1 oyun motoru 2003 yılında yalnızca Latin-1 (Batı Avrupa) karakter kümesiyle derlendiğinden, Türkçe font glifleri (`ç, ğ, ı, ö, ş, ü`) içermemektedir. Karakter bozulmalarını, kutu (`□`) veya soru işareti (`?`) hatalarını engellemek için tüm metinler standart **ASCII Türkçe** (`c, g, i, o, s, u`) karşılıklarıyla ve %100 imla doğruluğuyla uyarlanmıştır.
3. **Format Etiketleri Bütünlüğü:**
   - Glacier motoruna özel `$TapUse$`, `$HoldPrecisionAim$`, `%s`, `%i` gibi tüm dinamik tuş atamaları ve C printf değişkenleri birebir korunmuştur.

---

## 🚀 Kurulum Talimatları

### Yöntem 1: Tek Tıkla Otomatik Kurulum (Önerilen)
1. Bu repodaki dosyaları indirin (veya ZIP olarak indirip bir klasöre çıkartın).
2. Klasör içerisindeki **`Install_Yama.bat`** dosyasına çift tıklayın.
3. Yükleyici oyununuzun kurulu olduğu klasörü (Epic Games, Steam veya GOG) otomatik olarak tespit edecek, orijinal dosyalarınızın yedeğini alacak ve yamayı saniyeler içinde uygulayacaktır.

### Yöntem 2: Komut Satırı / Manuel Kurulum
Sisteminizde Python yüklü ise terminalden doğrudan çalıştırabilirsiniz:
```bash
python patch_game.py --game-dir "C:\Program Files\Epic Games\FreedomFighters"
```
*(Oyununuz Steam veya GOG üzerinde ise tırnak içindeki yolu kendi oyun klasörünüzle değiştirin)*

---

## 🔄 Yamayı Kaldırma (Orijinal Dosyalara Dönüş)

Yamayı dilediğiniz an tek tıkla kaldırabilir ve oyununuzu orijinal İngilizce haline geri döndürebilirsiniz:
- **`Uninstall_Yama.bat`** dosyasını çalıştırmanız yeterlidir.
- Yama kurulum sırasında `Scenes_Backup/Original_LOC_Backup.zip` yedeği aldığı için hiçbir dosya kaybı yaşanmaz.

---

## 🎮 Uyumluluk Listesi

| Platform | Uyumluluk Durumu |
| :--- | :--- |
| **Epic Games Store** | %100 Uyumlu ve Test Edildi |
| **Steam** | %100 Uyumlu |
| **GOG.com** | %100 Uyumlu |
| **Orijinal CD/DVD Sürümü** | %100 Uyumlu |

---

## 🏛️ Mimari ve Teknik Detaylar

Freedom Fighters localization sistemi IO Interactive'in tescilli ikili `.LOC` ağaç yapısını kullanır. Metinler `Scenes/` dizinindeki 88 farklı `.ZIP` arşivinde hiyerarşik düğümler halinde saklanmaktadır.

Proje kapsamında Glacier engine ikili `.LOC` okuyucu/yazıcı motoru tersine mühendislikle çözülmüş ve **88/88 dosyada %100 bayt-bayt geri-dönüşüm doğruluğu** kanıtlanmıştır.

Sistem mimarisi diyagramına erişmek için:
- **[`docs/architecture/freedom_fighters_turkish_patch.html`](docs/architecture/freedom_fighters_turkish_patch.html)** dosyasını tarayıcınızda açabilirsiniz.

---

## 📜 Lisans

Bu proje [MIT Lisansı](LICENSE) altında paylaşılmıştır.
Freedom Fighters oyununun tüm hakları IO Interactive ve Electronic Arts'a aittir.
Hazırlayan: **sqtbey**
