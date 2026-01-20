#!/usr/bin/env python3
import argparse
import re
import json
import math
import sys
import time
import os

# --- TERMİNAL RENKLENDİRME ---
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# --- YARDIMCI FONKSİYONLAR ---

def print_banner():
    """Program açılışında havalı bir başlık basar."""
    print(f"{Colors.HEADER}")
    print("╔══════════════════════════════════════════════════╗")
    print("║   ISU SecOps - Log Sensitivity Analyzer v1.0     ║")
    print("║   Modül: DLP & Entropy Scanner                   ║")
    print("╚══════════════════════════════════════════════════╝")
    print(f"{Colors.ENDC}")

def loading_animation(duration=1.5):
    """Sahte yükleme çubuğu (Profesyonel görünüm için)."""
    print(f"{Colors.BLUE}[*] Analiz motoru başlatılıyor...{Colors.ENDC}")
    toolbar_width = 40
    for i in range(toolbar_width):
        time.sleep(duration / toolbar_width)
        sys.stdout.write("█")
        sys.stdout.flush()
    sys.stdout.write("] HAZIR!\n\n")

def calculate_entropy(text):
    """
    Shannon Entropisi: Metnin rastgelelik/karmaşıklık derecesini ölçer.
    Normal kelimeler (örn: 'password') düşük entropiye,
    Rastgele şifreler (örn: 'Xy9#vK!2') yüksek entropiye sahiptir.
    """
    if not text: return 0
    entropy = 0
    for x in range(256):
        p_x = float(text.count(chr(x))) / len(text)
        if p_x > 0:
            entropy += - p_x * math.log(p_x, 2)
    return entropy

def mask_secret(text):
    """Hassas veriyi yıldızlayarak gizler (Maskeleme Önerisi)."""
    if len(text) < 5: return "*****"
    return text[:2] + "*" * (len(text)-4) + text[-2:]

# --- ANA PROGRAM ---

def main():
    parser = argparse.ArgumentParser(description="ISU SecOps - DLP Tool")
    parser.add_argument("--scan", help="Analiz edilecek log dosyası", required=True)
    args = parser.parse_args()

    print_banner()

    if not os.path.exists(args.scan):
        print(f"{Colors.FAIL}[HATA] '{args.scan}' dosyası bulunamadı!{Colors.ENDC}")
        return

    loading_animation()

    findings = []
    total_lines = 0
    
    # 1. Beklenen Özellik: PII Tespiti (Regex ile)
    patterns = {
        "Kredi Karti (PII)": r"\d{4}-\d{4}-\d{4}-\d{4}",
        "TC Kimlik (PII)": r"\d{11}",
        "Email Adresi (PII)": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    }

    try:
        with open(args.scan, "r", encoding="utf-8") as file:
            for line_num, line in enumerate(file, 1):
                total_lines += 1
                line = line.strip()
                if not line: continue

                # A) Regex Taraması (Pattern Matching)
                for p_name, p_regex in patterns.items():
                    matches = re.findall(p_regex, line)
                    for m in matches:
                        findings.append({
                            "satir": line_num,
                            "tur": p_name,
                            "risk_seviyesi": "YÜKSEK",
                            "maskeleme_onerisi": mask_secret(m)
                        })

                # B) Secret Scanning (Entropy Analizi)
                # Kelimeleri ayır ve karmaşıklığına bak
                words = line.split()
                for word in words:
                    # Uzunluğu 10'dan büyük ve karmaşıklığı 4.5 üstü ise şifredir
                    if len(word) > 10 and calculate_entropy(word) > 4.5:
                        if "http" not in word and not word.startswith("{"):
                            findings.append({
                                "satir": line_num,
                                "tur": "API Key / Token (Secret)",
                                "risk_seviyesi": "KRİTİK",
                                "maskeleme_onerisi": "VERI_SILINDI_HASH",
                                "teknik_detay": f"Entropy Skoru: {calculate_entropy(word):.2f}"
                            })

        # --- RAPORLAMA ---
        print(f"{Colors.BOLD}--- TEHLİKE ANALİZİ RAPORU ---{Colors.ENDC}")
        print(f"Taranan Satır: {total_lines}")
        print(f"Tespit Edilen Risk: {len(findings)}\n")

        if findings:
            for f in findings:
                color = Colors.FAIL if f["risk_seviyesi"] == "KRİTİK" else Colors.WARNING
                print(f"[{color}{f['risk_seviyesi']}{Colors.ENDC}] Satır {f['satir']}: {f['tur']}")
                print(f"    └── Maskeleme: {f['maskeleme_onerisi']}")
            
            # Sonuçları dosyaya kaydet
            output_file = "security_report.json"
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(findings, f, indent=4, ensure_ascii=False)
            print(f"\n{Colors.GREEN}[✓] Rapor '{output_file}' dosyasına kaydedildi.{Colors.ENDC}")
        else:
            print(f"{Colors.GREEN}[✓] Log dosyası temiz.{Colors.ENDC}")

    except Exception as e:
        print(f"{Colors.FAIL}[HATA] {e}{Colors.ENDC}")

if __name__ == "__main__":
    main()