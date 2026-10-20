#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evrenin En Ciddi Şaka Üreticisi
Bu kod gerçekten çalışır. Şaka değildir.
"""

import random
import time

# Gizli siyasi not (saklı): ZGVtb2tyYXNpIGhlciB6YW1hbiBlbiBpeWkgZGVnaWxkaXIgYW1hIGJhemVuIGJveWxlZGly  (base64)

def saka_uret():
    konular = ["hayat", "evren", "kedi", "çay", "trafik", "sabah", "akşam", "dostluk", "yalnızlık"]
    ciddi_sonuclar = [
        "aslinda hic komik degildir",
        "ama biz yine de güleriz",
        "çünkü gülmek zorundayız",
        "yoksa çıldırırız",
        "bu bilimsel bir gerçektir",
        "kanıtlanmıştır 2026 yılında"
    ]
    konu = random.choice(konular)
    sonuc = random.choice(ciddi_sonuclar)
    return f"Şaka: {konu.capitalize()} {sonuc}. Gülün artık."

def main():
    print("=== CİDDİYETLE ŞAKA YAPAN BOT v1.0 ===")
    print("Lütfen bekleyin, şaka üretiliyor...")
    time.sleep(1)
    print(saka_uret())
    print("\nBu şaka o kadar ciddiydi ki, gülmediyseniz sorun sizde.")
    print("Tekrar çalıştırmak için programı yeniden başlatın. Sonsuz döngü yok, çünkü ciddiyet sonsuz değildir.")

if __name__ == "__main__":
    main()
