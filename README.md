# finalproject-otomatisasi_strukcafe
Latar Belakang: "Di industri food & beverage saat ini, kecepatan layanan dan akurasi data adalah segalanya. Kami mengembangkan sistem kasir berbasis Python ini untuk menjembatani kebutuhan cafe yang ingin beralih dari pencatatan manual ke sistem digital yang efisien."

Visi: "Fokus utama kami adalah menghadirkan aplikasi yang lightweight (ringan) namun memiliki fitur lengkap seperti perhitungan pajak otomatis dan cetak struk profesional."
1. Arsitektur Data & Library
Aplikasi ini dibangun menggunakan struktur data Dictionary untuk menyimpan menu, yang memungkinkan pencarian item secara cepat berdasarkan kode unik.
•	FPDF: Digunakan sebagai mesin pembuat dokumen. Library ini menyusun teks, garis, dan format mata uang ke dalam koordinat PDF yang presisi.
•	DateTime: Menjamin setiap struk memiliki stempel waktu yang akurat untuk keperluan audit.
•	Webbrowser & OS: Memberikan pengalaman pengguna yang mulus dengan otomatis membuka struk segera setelah transaksi selesai.

2. Fitur Utama & Logika Bisnis
A. Skema Diskon Dinamis
Sistem memiliki logika loyalty reward otomatis. Jika nilai belanja (Subtotal) melebihi Rp 100.000, sistem akan memotong harga sebesar 10%. Potongan ini dihitung sebelum pajak untuk memberikan nilai yang adil bagi konsumen.


B. Perhitungan Pajak Negara (PPN 11%)
Sesuai dengan regulasi pajak di Indonesia, sistem ini menerapkan PPN sebesar 11%. Pajak dihitung dari DPP (Dasar Pengenaan Pajak), yaitu harga setelah dikurangi diskon.
Rumus: GrandTotal=(Subtotal−Diskon)+11%
C. Multi-Metode Pembayaran
Aplikasi ini mendukung tiga skenario pembayaran modern:
1.	Cash (Tunai): Dilengkapi fitur validasi. Sistem tidak akan memproses struk jika uang kurang, dan otomatis menghitung kembalian (Change).
2.	QRIS: Mengasumsikan pembayaran digital dengan nominal pas (tanpa kembalian).
3.	Debit: Memproses transaksi kartu dengan nominal pas.
3. Detail Teknis Pencetakan Struk
Fungsi cetak_struk_pdf memiliki fitur Dynamic Paper Height. Tinggi kertas PDF tidak statis, melainkan dihitung berdasarkan rumus: 
175+(JumlahItem×12)
Hal ini memastikan struk tidak memiliki ruang kosong yang terlalu panjang jika item sedikit, dan tidak terpotong jika item sangat banyak.
4. Alur Kerja Pengguna (User Journey)
1.	Identifikasi: Kasir memasukkan nama untuk akuntabilitas laporan.
2.	Input: Kasir memasukkan kode menu (misal: "1" untuk Nutty Palme).
3.	Verifikasi: Sistem menampilkan rincian biaya (Subtotal, Diskon, Pajak) di terminal.
4.	Finalisasi: Kasir memilih metode bayar dan tipe pesanan (Dine In/Take Away).
5.	Output: File PDF dihasilkan dengan nama unik berdasarkan nomor referensi acak untuk mencegah tumpang tindih file.
5. Keunggulan Sistem Ini
•	User-Friendly: Menggunakan kode angka (1, 2, 3...) sehingga kasir tidak perlu mengetik nama menu yang panjang.
•	Akurat: Menggunakan pemisah ribuan (titik) untuk memudahkan pembacaan angka besar.
•	Lengkap: Menyertakan informasi tambahan seperti detail WiFi cafe untuk meningkatkan kepuasan pelanggan.
