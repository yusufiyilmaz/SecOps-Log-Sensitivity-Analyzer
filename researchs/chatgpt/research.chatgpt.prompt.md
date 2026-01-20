# ChatGPT Deep Research Promptları

Bu dosya, Log Sensitivity Analyzer projesinin teknik altyapısı kurgulanırken ChatGPT (Deep Research Mode) modeline verilen komutları içerir.

### 1. Ana Komut (Master Prompt)

**Hedef:** Veri Sızıntısı Önleme (DLP) Mimarisi ve Desen Eşleştirme Stratejisi

> "Merhaba, Python tabanlı geliştireceğim 'Log Sensitivity Analyzer' projesi için 'Derin Araştırma' (Deep Research) modunda çalışmanı istiyorum.
>
> **Proje Amacı:** Uygulama ve sunucu loglarını (Apache, Nginx, Syslog) tarayarak Kişisel Verileri (PII - TC Kimlik, Kredi Kartı) ve Hassas Sırları (Şifre, Token) tespit eden bir denetim aracı geliştirmek.
>
> **Teknik Odak:** Veri Sızıntısının Önlenmesi (DLP) ve Desen Eşleştirme (Pattern Matching).
>
> **Beklenen Çıktılar (Araştırma Başlıkları):**
> 1.  **PII Tespiti:** Log satırlarında Regex kullanarak Kredi Kartı, E-posta, Telefon ve TCKN yakalamak için 'False Positive' oranı düşük, yüksek performanslı regex desenleri nelerdir?
> 2.  **Gizli Tarama (Secrets Detection):** Loglara yanlışlıkla basılan API anahtarlarını (AWS, Google Cloud) ve 'password=' değişkenlerini bulmak için kullanılan Entropy (Karmaşıklık) analizi yöntemleri.
> 3.  **Tehlike Analizi:** Bir log dosyasının ne kadar risk taşıdığını hesaplamak (Risk Scoring) için nasıl bir matematiksel model önerirsin? (Örn: 1 Kredi Kartı = 10 Puan, 1 Email = 1 Puan).
> 4.  **Maskeleme Standartları:** Tespit edilen hassas verilerin raporlanırken güvenli bir şekilde maskelenmesi (Örn: `****-****-****-1234`) için endüstri standartları (PCI-DSS) nelerdir?
>
> **Önemli Not:** Her teknik bilginin kaynağını (OWASP, NIST vb.) link olarak belirtmeni istiyorum."

## 2. Derinleştirme ve Kod Yapısı (2. Prompt)

ChatGPT'nin DLP yöntemlerini açıklamasından sonra, kodun mimarisini oluşturmak için şu komut verilmiştir:

> "DLP yöntemleri için teşekkürler. Şimdi bu teoriyi pratiğe dökelim:
>
> 1.  **Modüler Mimari:** Tarama motoru (Scanner) ve Raporlama (Reporter) modüllerini içeren, genişletilebilir bir Python proje klasör yapısı öner.
> 2.  **Büyük Veri Yönetimi:** 1GB+ boyutundaki log dosyalarını tararken RAM'i şişirmemek için Python 'Generator' (`yield`) yapısını kullanan örnek bir dosya okuma fonksiyonu (pseudocode) yaz.
> 3.  **Konfigürasyon:** Kullanıcının hangi regex desenlerinin aktif olacağını seçebilmesi için örnek bir YAML konfigürasyon dosyası yapısı hazırla.
>
> **Lütfen cevabında Python 'Clean Code' prensiplerine uygun kaynaklara referans ver.**"

[ Geri dön ](../chatgpt/research.chatgpt.chat_link.txt)

[İleri ](../chatgpt/research.chatgpt.result.md)
