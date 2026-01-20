# Gemini  Deep Research Promptları

Bu dosya, Log Sensitivity Analyzer projesinin performans ve güvenlik standartları belirlenirken Gemini flash modeline verilen komutları içerir.

## 1. PII ve Secret Tespiti (DLP Stratejisi)
 
**Hedef:** Karmaşık veri yapılarını (PII) en hızlı ve en doğru şekilde yakalamak.

> "Merhaba Gemini, 'Log Sensitivity Analyzer' projem için senden teknik bir rehberlik bekliyorum.
>
> **Görev:** Log dosyalarındaki TCKN, Kredi Kartı ve API Key gibi verileri tespit edecek Python fonksiyonları yazacağız.
> 
> 1. **Performanslı Regex:** Bu veriler için 'Catastrophic Backtracking' (ReDoS) riski taşımayan, optimize edilmiş regex desenleri öner.
> 2. **Luhn Algoritması:** Sadece regex ile kredi kartı bulmak çok fazla 'False Positive' (yanlış alarm) üretir. Yakalanan kart numaralarını doğrulamak için Luhn algoritmasını en hızlı nasıl entegre edebilirim?
> 3. **Maskeleme:** Hassas verileri `****-****` şeklinde maskelerken string birleştirme yerine daha hızlı olan 'slicing' yöntemini kullanan bir örnek kod sağla."

## 2. Büyük Veri ve Bellek Yönetimi  
 
**Hedef:** 10GB+ boyutundaki log dosyalarını tararken sistemin çökmesini engellemek.

> "Veri tespit yöntemleri tamam. Şimdi işleme kapasitesine odaklanalım:
> 
> 1. **Generator Kullanımı:** Python'da `yield` anahtar kelimesiyle dosyayı satır satır okuyan ve bellekte minimum yer kaplayan bir 'stream' yapısı kur.
> 2. **Hata Yakalama:** Loglar içindeki bozuk karakterler (encoding issues) için `errors='replace'` kullanımının avantajlarını açıkla.
> 3. **Compilation:** `re.compile()` fonksiyonunun bir döngü içinde neden kritik olduğunu teknik olarak açıkla."

---
[Geri Dön ](./research.gemini-fast.chat_link.txt)

[ İleri ](./research.gemini-fast.result.md)
