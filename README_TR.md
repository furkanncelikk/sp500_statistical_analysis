# 📊 S&P 500 Kantitatif Araştırma — Piyasa Anomalisi Testleri

> **S&P 500 hisseleri üzerinde kendi kurduğum veri tabanı altyapısını kullanarak piyasa efsanelerini istatistiksel hipotez testleriyle sistematik olarak doğrulayan ya da çürüten bir araştırma portfolyosu.**

| 🇬🇧 [English Version](README.md) | 🇹🇷 Türkçe (şu an) |
|---|---|

---

## 🧑‍💻 Proje Hakkında

Bu repo, kişisel kantitatif finans araştırma portfolyomun bir parçasıdır. Tüm S&P 500 bileşenlerinin tarihsel fiyat verilerini otomatik olarak çeken, temizleyen ve kendi PostgreSQL veri ambarıma kaydeden uçtan uca bir veri pipeline'ı kurdum. Bu serinin her bir notebook'u, belirli bir piyasa hipotezini akademik düzeyde istatistiksel testlerle doğrular ya da reddeder.

**Felsefem:** *Sezgiye güvenme — veriyle test et, p-değerini raporla ve açık bir ticari karar ver.*

---

## 🗄️ Veri Altyapısı

| Katman | Açıklama |
|---|---|
| **Kaynak** | [yfinance](https://github.com/ranaroussi/yfinance) API — günlük OHLCV verisi |
| **Kapsam** | ~500 S&P 500 bileşeni · Her hisse için tam tarihsel geçmiş |
| **Depolama** | Kişisel PostgreSQL 15 veri ambarı (`sp500_dw`) |
| **Temel Tablolar** | `daily_prices` (OHLCV) · `tickers` (metadata & GICS sektörleri) · `ticker_stats` (önceden hesaplanmış istatistikler) |
| **Ön İşlem** | Kurtosis, Skewness ve Jarque-Bera istatistikleri tüm hisseler için toplu pipeline ile hesaplanıp `ticker_stats` tablosuna kaydedilir |

> **Kimlik bilgileri hakkında not:** Veritabanı bağlantı bilgileri versiyon kontrolüne dahil edilmeyen yerel bir `config.py` dosyasında saklanır (bkz. `.gitignore`). `db_utils.py` modülü bağlantıyı soyutlar — tüm notebook'lar yalnızca `fetch_data(query)` fonksiyonunu çağırır.

---

## 📁 Klasör Yapısı

```
├── db_utils.py                        # Ortak veritabanı bağlantı modülü (public)
├── config.py                          # Veritabanı kimlik bilgileri (private — gitignore'da)
│
├── H1_Tail_Risk_vs_Return.ipynb       # H1: Kurtosis uzun vadeli getiriyi öngörür mü?
├── H2_H3_Seasonality.ipynb            # H2: Ocak/Aralık Etkisi · H3: 12 ay ANOVA testi
├── H4_Weekend_Effect.ipynb            # H4: Cuma vs Pazartesi — Hafta Sonu Etkisi
├── H5_Sector_Correlation.ipynb        # H5: Sektörler arası korelasyon matrisi
│
└── README.md
```

---

## 🔬 Test Edilen Hipotezler

### H1 · Kuyruk Riski Primi: Kurtosis Ödüllendiriliyor mu?
- **Test:** Pearson Korelasyonu + OLS Regresyonu
- **İddia:** Yüksek fazla basıklığa (fat tail / Siyah Kuğu riski) sahip hisseler, ekstra riske karşılık olarak uzun vadede daha yüksek getiri sağlamalıdır.

### H2 · Ocak ve Aralık Etkisi (Santa Claus Rallisi)
- **Test:** Welch'in Bağımsız Örneklem T-Testi (tek kuyruklu)
- **İddia:** Ocak ve Aralık ayları yılın diğer aylarına kıyasla sistematik olarak daha yüksek aylık getiri sağlar.

### H3 · Mevsimsellik ANOVA — 12 Takvim Ayı (2008–Günümüz)
- **Test:** Tek Yönlü ANOVA (F-testi)
- **İddia:** 12 takvim ayının ortalama getirileri arasında istatistiksel olarak anlamlı bir fark vardır (mevsimsellik etkisi).
- **Önemli Bulgu:** 📅 **Kasım** en güçlü ay olarak öne çıktı; **Eylül** en zayıf ay — akademik literatürde belgelenen "Eylül Etkisi" ile tutarlı.

### H4 · Hafta Sonu Etkisi — Cuma vs Pazartesi
- **Test:** Welch'in Bağımsız Örneklem T-Testi (tek kuyruklu) + KDE dağılım karşılaştırması
- **İddia:** Cuma günleri günlük log getirileri, tüm S&P 500 evreni genelinde Pazartesi günlerinden istatistiksel olarak anlamlı biçimde daha yüksektir.

### H5 · Sektörel Çeşitlendirme — Sektörler Arası Korelasyon Matrisi
- **Test:** Pearson Korelasyon Matrisi (Isı Haritası)
- **İddia:** Tüm sektörler birbiriyle kusursuz bir uyum içinde hareket etmez; düşük korelasyonlu sektör çiftlerinin tespit edilmesi Markowitz Modern Portföy Teorisi prensiplerine göre riskin azaltılmasına olanak tanır.

---

## 📋 Rapor Şablonu

Her hipotez aynı 4 bölümlü yapıyı takip eder:

```
1. Hipotez Tanımı     → H₀ ve H₁ açıkça ifade edilir
2. Veri & Metodoloji  → Evren, değişkenler, test seçimi
3. İstatistiksel Bulgular → p-değeri, test istatistiği, tanımlayıcı istatistikler + görselleştirmeler
4. Ticari Karar (Quant Verdict) → DOĞRULANDI / REDDEDİLDİ + Ticarete dökülebilir mi? + ML özellik değeri
```

---

## 🛠️ Teknoloji Yığını

`Python 3.11` · `PostgreSQL 15` · `SQLAlchemy` · `Pandas` · `NumPy` · `SciPy` · `Seaborn` · `Matplotlib` · `Jupyter`

---

## 👤 Yazar

**Furkan Çelik**  
Kantitatif Araştırma · Veri Mühendisliği · Algoritmik Finans  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Bağlan-blue)](https://linkedin.com/in/celikfrkn)
[![GitHub](https://img.shields.io/badge/GitHub-Takip%20Et-black)](https://github.com/furkanncelikk)

---

*Bu proje eğitim ve araştırma amaçlıdır. Bu repodaki hiçbir şey finansal tavsiye niteliği taşımaz.*
