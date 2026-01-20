# Perplexity Teknik Araştırma Sonuçları: Altyapı ve Kaynaklar

Bu rapor, Perplexity AI tarafından yapılan web taraması sonucunda belirlenen proje mimarisini ve kütüphaneleri içerir.

## 1. Seçilen Teknoloji Yığını (Tech Stack)

Yapılan karşılaştırmalar sonucu aşağıdaki kütüphaneler seçilmiştir:

| Kütüphane | Sürüm | Neden Seçildi? |
| :--- | :--- | :--- |
| **Typer** (veya Click) | `^0.9.0` | FastAPI yaratıcısından. Modern, type-hint destekli ve Click'ten daha az kod gerektiriyor. |
| **Rich** | `^13.0.0` | Terminalde tablo, panel ve progress bar için rakipsiz standart. |
| **Pytest** | `^8.0.0` | `unittest` modülüne göre daha az boilerplate kod gerektirir ve plugin desteği geniştir. |
| **Pydantic** | `^2.0.0` | Veri doğrulama (Validation) için en hızlı ve güvenilir kütüphane. |

## 2. Önerilen Proje Ağacı (Src Layout)

Python topluluğunun önerdiği (Packaging Authority) modern yapı:

```text
log-sensitivity-analyzer/
├── src/
│   ├── scanner/
│   │   ├── __init__.py
│   │   ├── main.py       # Uygulama Girişi
│   │   ├── core.py       # Tarama Motoru
│   │   └── patterns.py   # Regex Desenleri (PII)
│   └── utils/
│       └── validators.py # Luhn & TCKN Algoritmaları
├── tests/
│   ├── test_core.py
│   └── test_validators.py
├── pyproject.toml        # Modern paket ayarları (setup.py yerine)
└── README.md
```

3. Bulunan Kritik Regex Desenleri
Perplexity taraması sonucu doğruluk oranı en yüksek desenler:

Kredi Kartı (Genel): (?:\d{4}[-\s]?){3}\d{4} (Basit eşleşme, Luhn algoritması ile doğrulanmalı)

TCKN (Basit): [1-9]\d{10} (11 haneli, 0 ile başlayamaz)

## Bağlantılar
* [Sonuçları Gör ](./research.perplexity.prompt.md)
 
* [Sonuçları Gör (Result)](./research.perplexity.sources.md)
