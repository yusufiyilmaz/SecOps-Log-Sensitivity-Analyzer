# Gemini Pro Deep Research Promptları

Bu dosya, Log Sensitivity Analyzer  projesinin performans optimizasyonu ve kodlama standartları belirlenirken Google Gemini Pro modeline verilen komutları içerir.

## 1. Yüksek Performanslı Regex ve DLP Stratejisi

**Hedef:** İşlemciyi yormayan (CPU-Friendly), ReDoS saldırılarına karşı güvenli ve DLP odaklı Regex desenleri.

> "Merhaba Gemini, Python tabanlı geliştireceğim 'Log Sensitivity Analyzer' (DLP Denetim Aracı) projem için 'Senior Python Engineer' rolünde çalışmanı istiyorum.
>
> **Proje Amacı:** Uygulama ve sunucu loglarını tarayarak Kişisel Verileri (PII) ve Hassas Sırları (Secrets) tespit etmek.
>
> **Beklenti:** 
> 1.  **Optimize Regexler:** Aşağıdaki veriler için 'Catastrophic Backtracking' (ReDoS) riski taşımayan en performanslı regex desenlerini yaz:
>     * **PII:** Kredi Kartı (16 hane), TCKN (11 hane), E-posta ve Telefon.
>     * **Secrets:** Yaygın API Key formatları (AWS, Google) ve 'password=' atamaları.
> 2.  **Derleme (Compilation):** Python `re` modülünde `re.compile()` kullanımının 5GB+ log dosyalarını tararken sağlayacağı performans farkını teknik olarak açıkla.
>
> **Önemli Not:** Regex performans testleri veya güvenlik kaynaklarına (OWASP ReDoS Cheat Sheet vb.) link vermeni istiyorum."

## 2. Bellek Yönetimi ve Büyük Veri İşleme

**Hedef:** RAM kullanımını minimumda tutarak devasa log dosyalarını (Big Data) işlemek.

> "Regex desenleri anlaşıldı. Şimdi veri işleme (Data Processing) kısmına geçelim:
>
> 1.  **Lazy Evaluation (Generator):** Python'da `yield` yapısını kullanarak, log dosyasını satır satır okuyan ve belleği şişirmeyen bir 'Generator Fonksiyonu' örneği kodla.
> 2.  **Hata Yönetimi:** Log dosyalarında sıkça rastlanan `utf-8` decoding hatalarını programı çökertmeden yönetmek için `errors='replace'` veya `errors='ignore'` stratejilerinden hangisini önerirsin?
> 3.  **Maskeleme Performansı:** Tespit edilen veriyi (örn: Kredi Kartı) maskelerken (örn: `****-1234`) string manipülasyonu yerine en hızlı Python yöntemini (slice vb.) göster.
>
> **Lütfen cevabında Python resmi dokümantasyonuna (Python Docs) referans ver.**"
