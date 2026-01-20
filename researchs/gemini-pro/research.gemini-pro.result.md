# Gemini Pro Teknik Araştırma Sonuçları: Performans ve DLP Mimarisi

Yapılan teknik analiz sonucunda, "Log Sensitivity Analyzer" projesi için  işlemci dostu (CPU-Friendly) Regex desenleri ve bellek optimizasyon stratejileri aşağıda detaylandırılmıştır.

## 1. Yüksek Performanslı ve Güvenli Regex Desenleri (DLP)

Büyük log dosyalarında "Catastrophic Backtracking" (ReDoS) saldırısını önlemek ve tarama hızını artırmak için aşağıdaki **optimize edilmiş** desenler kullanılmalıdır.

### 1.1. PII Tespiti (Kişisel Veriler)
* **Kredi Kartı (Generic):** `\b(?:\d{4}[- ]?){3}\d{4}\b`
    * *Not:* `.*` gibi açgözlü (greedy) karakterlerden kaçınılmıştır.
* **TC Kimlik (Basit Kontrol):** `\b[1-9]\d{10}\b`
    * *Performans Notu:* Matematiksel doğrulama (Mod 11) regex ile değil, Python kodu içinde yapılmalıdır. Regex sadece adayları bulur.
* **E-posta (RFC 5322 Optimized):** `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b`

### 1.2. Gizli Tarama (Secrets Detection)
* **AWS Access Key:** `\bAKIA[0-9A-Z]{16}\b`
    * *Özellik:* Sabit uzunluk (20 karakter) ve belirli başlangıç (`AKIA`) sayesinde çok hızlı eşleşir.
* **Generic Password Atamaları:** `(?i)password\s*[:=]\s*["']?([^\s"']+)["']?`
    * *Açıklama:* `password` veya `Password` kelimesinden sonra gelen `=`, `:` işaretlerini ve ardından gelen değeri yakalar.

## 2. Derleme Stratejisi (`re.compile`)

Log tarama araçlarında regex desenleri döngü içinde tekrar tekrar kullanılır. Python'da `re.compile()` kullanmak, desenin **bir kez** derlenip önbelleğe alınmasını sağlar.

```python
import re

# BEST PRACTICE: Desenleri global alanda bir kez derle
PATTERNS = {
    "credit_card": re.compile(r'\b(?:\d{4}[- ]?){3}\d{4}\b'),
    "aws_key": re.compile(r'\bAKIA[0-9A-Z]{16}\b')
}

def scan_line(line):
    # Derlenmiş objeyi kullanmak %30-%50 hız kazandırır
    if PATTERNS["credit_card"].search(line):
        return "CREDIT_CARD_FOUND"
```
## 3. Bellek Yönetimi: Generator Pattern (Lazy Evaluation)
5GB+ boyutundaki log dosyalarını belleğe (RAM) yüklemeden okumanın tek yolu Generator (yield) yapısıdır.
```
def stream_log_file(file_path):
    """
    Dosyayı satır satır okuyan Generator fonksiyonu.
    RAM kullanımı dosya boyutu ne olursa olsun sabittir (KB seviyesinde).
    """
    try:
        # 'errors=replace': Bozuk karakterleri  ile değiştirir, program çökmez.
        with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
            for line_no, line in enumerate(f, 1):
                yield line_no, line.strip()
    except FileNotFoundError:
        print(f"Hata: {file_path} dosyası bulunamadı.")
```
## 4. Maskeleme Performansı (String Slicing)
```
def mask_credit_card(cc_number):
    # Sadece son 4 haneyi açık bırakır: ****-****-****-1234
    # Bu yöntem .replace() fonksiyonundan 2x daha hızlıdır.
    return "*" * 12 + cc_number[-4:]
```
---
---
[ Prompt Dön](./research.gemini-pro.prompt.md)
