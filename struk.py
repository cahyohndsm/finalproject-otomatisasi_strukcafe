import datetime
from fpdf import FPDF
import os
import webbrowser
import random

# Database menu Skena Cafe
menu_cafe = {
    "Coffee & Non-Coffee": {
        "1": {"nama": "Nutty Palme", "harga": 20000},
        "2": {"nama": "Red Velvet", "harga": 22000},
        "3": {"nama": "Salted Caramel", "harga": 28000},
        "4": {"nama": "Espresso", "harga": 14000},
        "5": {"nama": "Vanila", "harga": 20000},
        "6": {"nama": "Klepon Late", "harga": 20000},
        "7": {"nama": "Matcha", "harga": 24000},
    },
    "Main Course & Snacks": {
        "8": {"nama": "Croffle Maple", "harga": 25000},
        "9": {"nama": "Truffle Fries", "harga": 22000},
        "10": {"nama": "Nasi Gila", "harga": 18000},
        "11": {"nama": "Tom Yum", "harga": 24000},
        "12": {"nama": "Chicken Katsu", "harga": 20000},
        "13": {"nama": "Spageti Bolognese", "harga": 25000},
        "14": {"nama": "Nasi Goreng Seafood", "harga": 25000},
    }
}

def cetak_struk_pdf(nama_kasir, keranjang, subtotal, diskon, pajak, grand_total, bayar, metode, tipe_pesanan):
    waktu = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    kembalian = bayar - grand_total
    no_ref = "".join([str(random.randint(0, 9)) for _ in range(10)])
    
    filename = f"Struk_Skena_{no_ref[:5]}.pdf"
    # Menyesuaikan tinggi kertas berdasarkan jumlah item
    tinggi_kertas = 175 + (len(keranjang) * 12)
    
    try:
        pdf = FPDF(format=(80, tinggi_kertas))
        pdf.add_page()
        pdf.set_margins(left=7, top=10, right=7)
        
        # --- HEADER ---
        pdf.set_font("Courier", 'B', 12)
        pdf.cell(0, 5, "SKENA CAFE", ln=True, align='C')
        pdf.set_font("Courier", size=8)
        pdf.cell(0, 4, "No. 105 Sorosutan Umbulharjo", ln=True, align='C')
        pdf.cell(0, 4, "Yogyakarta", ln=True, align='C')
        pdf.ln(2)
        pdf.cell(0, 1, "-"*38, ln=True, align='C')
        
        # --- INFO TRANSAKSI ---
        pdf.set_font("Courier", size=8)
        pdf.cell(25, 4, "No. Ref", 0); pdf.cell(5, 4, f": {no_ref}", ln=True)
        pdf.cell(25, 4, "Kasir", 0); pdf.cell(5, 4, f": {nama_kasir.upper()}", ln=True)
        pdf.cell(25, 4, "Metode", 0); pdf.cell(5, 4, f": {metode}", ln=True)
        pdf.cell(25, 4, "Tipe", 0); pdf.cell(5, 4, f": {tipe_pesanan}", ln=True)
        pdf.ln(2)
        pdf.cell(0, 1, "-"*38, ln=True, align='C')
        pdf.ln(2)

        # --- DAFTAR ITEM ---
        for item in keranjang:
            pdf.set_font("Courier", 'B', 9)
            pdf.cell(0, 4, item['nama'], ln=True)
            pdf.set_font("Courier", size=9)
            pdf.cell(35, 4, f"{item['qty']} x {item['harga']:,}".replace(',', '.'), 0)
            pdf.cell(0, 4, f"{item['subtotal']:,}".replace(',', '.'), ln=True, align='R')

        pdf.ln(2)
        pdf.cell(0, 1, "-"*38, ln=True, align='C')
        
        # --- RINCIAN BIAYA (Subtotal, Diskon, Pajak) ---
        pdf.ln(2)
        pdf.set_font("Courier", size=9)
        pdf.cell(35, 4, "Subtotal", 0); pdf.cell(0, 4, f"{subtotal:,}".replace(',', '.'), ln=True, align='R')
        if diskon > 0:
            pdf.cell(35, 4, "Diskon (10%)", 0); pdf.cell(0, 4, f"-{diskon:,}".replace(',', '.'), ln=True, align='R')
        pdf.cell(35, 4, "Tax (11%)", 0); pdf.cell(0, 4, f"{pajak:,}".replace(',', '.'), ln=True, align='R')
        
        pdf.set_font("Courier", 'B', 10)
        pdf.cell(35, 6, "GRAND TOTAL", 0); pdf.cell(0, 6, f"{grand_total:,}".replace(',', '.'), ln=True, align='R')
        
        pdf.set_font("Courier", size=9)
        pdf.cell(35, 4, f"Bayar ({metode})", 0); pdf.cell(0, 4, f"{bayar:,}".replace(',', '.'), ln=True, align='R')
        pdf.cell(35, 4, "Kembalian", 0); pdf.cell(0, 4, f"{max(0, kembalian):,}".replace(',', '.'), ln=True, align='R')
        
        # --- FOOTER ---
        pdf.ln(5)
        pdf.set_font("Courier", 'I', 8)
        pdf.cell(0, 4, "WiFi: Skena Cafe / wajibskena", ln=True, align='C')
        pdf.ln(3)
        pdf.set_font("Courier", 'B', 10)
        pdf.cell(0, 5, "THANK YOU!", ln=True, align='C')

        pdf.output(filename)
        print(f"\n[System] Struk berhasil dibuat: {filename}")
        webbrowser.open(f'file:///{os.path.abspath(filename)}')
            
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("=== SKENA CAFE POS SYSTEM ===")
    nama_kasir = input("Nama Kasir: ")
    keranjang = []
    subtotal_akhir = 0
    
    # 1. Tampilkan Menu
    print("\n[MENU SKENA CAFE]")
    for kat, items in menu_cafe.items():
        print(f"--- {kat} ---")
        for k, d in items.items():
            print(f" {k}. {d['nama']} (Rp {d['harga']:,})".replace(',', '.'))
    
    # 2. Input Pesanan
    while True:
        pilihan = input("\nMasukkan Kode Menu (atau 'DONE'): ")
        if pilihan.upper() == 'DONE': break
        
        item_ditemukan = None
        for kat in menu_cafe.values():
            if pilihan in kat:
                item_ditemukan = kat[pilihan]
                break
        
        if item_ditemukan:
            try:
                qty = int(input(f"Jumlah untuk {item_ditemukan['nama']}: "))
                if qty > 0:
                    sub = item_ditemukan['harga'] * qty
                    keranjang.append({"nama": item_ditemukan['nama'], "harga": item_ditemukan['harga'], "qty": qty, "subtotal": sub})
                    subtotal_akhir += sub
            except ValueError:
                print("!! Masukkan angka valid !!")
        else:
            print("!! Kode menu salah !!")

    if not keranjang: return

    # 3. Logika Diskon & Pajak
    # Diskon 10% jika belanja di atas 100.000
    diskon = int(subtotal_akhir * 0.10) if subtotal_akhir > 100000 else 0
    # Pajak 11% dari harga setelah diskon
    pajak = int((subtotal_akhir - diskon) * 0.11)
    grand_total = (subtotal_akhir - diskon) + pajak

    # 4. Pilih Metode Pembayaran
    print(f"\nSubtotal    : Rp {subtotal_akhir:,}".replace(',', '.'))
    print(f"Diskon      : Rp {diskon:,}".replace(',', '.'))
    print(f"Pajak (11%) : Rp {pajak:,}".replace(',', '.'))
    print(f"GRAND TOTAL : Rp {grand_total:,}".replace(',', '.'))
    
    print("\nMETODE PEMBAYARAN:")
    print("1. Cash (Tunai)\n2. QRIS\n3. Debit")
    m_pilih = input("Pilih (1/2/3): ")
    
    metode = "CASH"
    if m_pilih == '1':
        while True:
            bayar = int(input("Masukkan Uang Tunai: "))
            if bayar >= grand_total: break
            print(f"!! Uang kurang Rp {grand_total - bayar:,} !!".replace(',', '.'))
    elif m_pilih == '2':
        metode = "QRIS"
        bayar = grand_total # QRIS dianggap uang pas
        print("Mencetak QR Code... Pembayaran Berhasil!")
    elif m_pilih == '3':
        metode = "DEBIT"
        bayar = grand_total # Debit dianggap uang pas
        print("Silakan gesek/tap kartu... Pembayaran Berhasil!")

    tipe = "DINE IN" if input("Dine In? (y/n): ").lower() == 'y' else "TAKE AWAY"
    
    # 5. Cetak
    cetak_struk_pdf(nama_kasir, keranjang, subtotal_akhir, diskon, pajak, grand_total, bayar, metode, tipe)

if __name__ == "__main__":
    main()