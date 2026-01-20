# 🛡️ SecOps: Log Sensitivity Analyzer

Bu proje, **İstinye Üniversitesi** SecOps müfredatı kapsamında geliştirilmiş bir **DLP (Veri Sızıntısı Önleme)** güvenlik aracıdır.

**Geliştirici:** Yusuf Yılmaz
**Ders:** Açık Kaynak İşletim Sistemleri

---

## 🎯 Proje Amacı
Uygulama ve sunucu loglarını tarayarak **Kişisel Verileri (PII - TC Kimlik, Kredi Kartı)** ve **Hassas Sırları (Password, Token)** tespit eden bir denetim otomasyonudur.

## ✨ Özellikler
* **🔍 PII Tespiti:** Log satırlarında Regex kullanarak Kredi Kartı, E-posta ve TC Kimlik gibi kişisel verileri yakalar.
* **🔐 Secret Scanning:** Loglara yanlışlıkla basılan API anahtarlarını ve şifreleri **Shannon Entropisi (Matematiksel Analiz)** yöntemiyle bulur.
* **📊 Tehlike Analizi:** Riskli satırları "KRİTİK" veya "YÜKSEK" olarak sınıflandırır.
* **🎭 Maskeleme:** Hassas verileri otomatik olarak maskeler (Örn: `4543-****`).

## 🛠️ Teknik Odak
* **Konsept:** Data Leakage Prevention (DLP)
* **Yöntem:** Pattern Matching (Regex) & Entropy Analysis
* **Dil:** Python 3 (Native - Kütüphane gerektirmez)

## 🚀 Kurulum ve Kullanım

### 1. Depoyu İndirin

```bash
git clone [https://github.com/yusufiyilmaz/SecOps-Log-Sensitivity-Analyzer.git](https://github.com/yusufiyilmaz/SecOps-Log-Sensitivity-Analyzer.git)
cd SecOps-Log-Sensitivity-Analyzer

### 2. Taramayı başlatın 

# Test dosyasını taramak için:
python src/main.py --scan test.log

### 3. Örnek Çıktı
Program çalıştırıldığında riskli verileri raporlar ve security_report.json dosyasına kaydeder.

[KRİTİK] Satır 4: API Key / Token (Secret)

    └── Maskeleme: VERI_SILINDI_HASH
