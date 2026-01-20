# ChatGPT Derin Araştırma Sonuçları: DLP ve PII Analiz Mimarisi

Yapılan "Derin Araştırma" sonucunda, **Log Sensitivity Analyzer** projesi için endüstri standartlarına (PCI-DSS, NIST) uygun tespit, analiz ve maskeleme stratejileri aşağıda detaylandırılmıştır.

## 1. PII Tespiti ve Regex Stratejisi (High Precision)

Düşük "False Positive" (Hatalı Tespit) oranı için sadece Regex yetmez, algoritmik doğrulama şarttır.

### 1.1. Kredi Kartı (PAN)
* **Regex Deseni:** `\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})\b` (Visa/Mastercard)
* **Doğrulama:** Regex ile yakalanan adaylar **Luhn Algoritması (Mod 10)** ile doğrulanmalıdır.
* **Maskeleme (PCI-DSS):** `****-****-****-1234` (Sadece son 4 hane açık).
 
### 1.2. TC Kimlik Numarası (TCKN)
* **Regex Deseni:** `\b[1-9]{1}[0-9]{9}[02468]{1}\b`
* **Doğrulama:** 11 haneli sayı, TCKN matematiksel algoritmasına (ilk 10 hane toplamı vb.) uymalıdır.
* **Maskeleme:** `12*******90` (İlk 2 ve son 2 hane açık, ortası maskeli).

## 2. Gizli Tarama (Secrets Detection via Entropy)

Loglarda unutulan API Key veya Şifreler genellikle rastgele karakterlerden oluşur.
* **Yöntem:** Shannon Entropy Analizi.
* **Mantık:** "password" kelimesi düşük entropilidir, ancak "J8#kA2!9s" yüksek entropilidir.
* **Eşik Değeri:** Entropi puanı > 4.5 olan stringler "Potansiyel Sır" (Potential Secret) olarak işaretlenmelidir.

```python
# Örnek Entropi Hesaplama Mantığı
import math
def shannon_entropy(data):
    if not data: return 0
    entropy = 0
    for x in set(data):
        p_x = float(data.count(x)) / len(data)
        entropy += - p_x * math.log(p_x, 2)
    return entropy
```
## 3. Tehlike Analizi ve Risk Skorlaması
Dosyanın ne kadar tehlikeli olduğunu ölçmek için aşağıdaki Ağırlıklı Risk Matrisi kullanılmalıdır:
| Bulgu Tipi | Risk Seviyesi | Puan (Ağırlık) |
| :--- | :--- | :--- |
| **Kredi Kartı** | KRİTİK | 100 Puan |
| **API Anahtarı** | YÜKSEK | 70 Puan |
| **TCKN** | ORTA | 50 Puan |

 Toplam Risk Skoru = (Bulgu Sayısı × Ağırlık Puanı)

Karar: Skor > 500 ise dosya "Acil İncelenmeli".

## 4. Önerilen Proje Mimarisi

DLP ve Performans gereksinimlerine uygun modüler yapı aşağıdadır:

```text
src/
├── core/
│   ├── scanner.py    # Ana tarama döngüsü (Generator kullanır)
│   ├── analyzer.py   # Regex ve Entropi motoru
│   └── scorer.py     # Risk puanlama modülü
├── utils/
│   ├── validators.py # Luhn ve TCKN algoritmaları
│   └── masker.py     # Veri maskeleme fonksiyonları
└── reports/
    └── json_builder.py # Denetim raporu oluşturucu
```

---
[ Geri dön ](../chatgpt/research.chatgpt.prompt.md)

[İleri ](../chatgpt/research.chatgpt.sources.md)
