#   made_by_dillski

import os
import re
import time

NAMA_SAYA = "~dillski`s"        
WARNA_RAHASIA = "merah"        
PETUNJUK_SETELAH = 3

os.system("")  

# Kode warna ANSI
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"

PALET = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]


def pelangi(teks):
    """Mewarnai teks huruf per huruf dengan warna pelangi."""
    hasil = ""
    for i, huruf in enumerate(teks):
        hasil += PALET[i % len(PALET)] + BOLD + huruf
    return hasil + RESET


def panjang_tampil(teks):
    """Panjang teks yang terlihat (kode warna diabaikan, emoji = 2 kolom)."""
    bersih = re.sub(r"\033\[[0-9;]*m", "", teks)
    return sum(2 if ord(c) >= 0x1F000 else 1 for c in bersih)


def kotak(baris, warna=CYAN, lebar=46):
    """Mencetak teks di dalam kotak dekoratif."""
    print(warna + "╔" + "═" * lebar + "╗" + RESET)
    for b in baris:
        sisa = max(lebar - panjang_tampil(b), 0)
        kiri = sisa // 2
        kanan = sisa - kiri
        print(warna + "║" + RESET + " " * kiri + b + " " * kanan + warna + "║" + RESET)
    print(warna + "╚" + "═" * lebar + "╝" + RESET)


def watermark():
    print(DIM + "─" * 48 + RESET)
    print(DIM + f"  {NAMA_SAYA}".ljust(47) + RESET)
    print(DIM + "─" * 48 + RESET)


def ketik(teks, jeda=0.02):
    """Efek mesin ketik."""
    for huruf in teks:
        print(huruf, end="", flush=True)
        time.sleep(jeda)
    print()


def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print()
    kotak([
        "",
        pelangi("  T E B A K   W A R N A  "),
        "",
        f"{WHITE}Tebak warna bersama coach dill{RESET}",
        "",
    ], CYAN)
    watermark()


def petunjuk_warna():
    """Petunjuk kecil agar game tidak membosankan."""
    return f"{YELLOW} Petunjuk: warnanya sama dengan warna bendera Indonesia bagian atas!{RESET}"


def main():
    mulai = True                                   

    while mulai:                                   
        banner()
        ketik(f"{GREEN}{BOLD}>>>Welcome to the game!<<<{RESET}")  

        jawaban = input(
            f"{CYAN}=> Mau main? ({GREEN}ya{CYAN}/{RED}tidak{CYAN}): {RESET}"
        ).strip().lower()                          

        if jawaban == "ya":                        
            tebakan = ""                          
            percobaan = 0

            print()
            print(f"{MAGENTA}Aku sedang memikirkan sebuah warna...{RESET}")

            while tebakan.lower() != WARNA_RAHASIA:   
                tebakan = input(
                    f"{YELLOW}> Tebakan warna: {RESET}"
                ).strip()                          
                percobaan += 1

                if tebakan.lower() != WARNA_RAHASIA:
                    print(f"{RED}> Salah! Coba lagi (percobaan ke-{percobaan}){RESET}")
                    if percobaan >= PETUNJUK_SETELAH:
                        print(petunjuk_warna())

            
            print()
            kotak([
                "",
                f"{GREEN}{BOLD} Tebakan benar! {RESET}",
                f"{WHITE}Warnanya: {RED}{BOLD}{WARNA_RAHASIA.upper()}{RESET}",
                f"{WHITE}Selesai dalam {percobaan}x percobaan{RESET}",
                "",
            ], GREEN)
            input(DIM + "\n(Tekan Enter untuk kembali ke menu)" + RESET)

        elif jawaban == "tidak":                   
            mulai = False                         

        else:                                      
            print(f"{RED} Masukkan jawaban ya atau tidak!{RESET}")
            time.sleep(1.5)

   
    print()
    kotak([
        "",
        pelangi("Terima kasih sudah bermain"),
        "",
    ], MAGENTA)
    watermark()                                    


if __name__ == "__main__":
    main()

#   made_by_dillski