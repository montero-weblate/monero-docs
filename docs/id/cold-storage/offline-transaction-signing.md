# Penandatanganan Transaksi Offline

!!! Peringatan! Ini **BUKAN** pengaturan penyimpanan dingin yang
direkomendasikan, karena kompleksitas yang tinggi, potensi kesalahan yang besar,
dan penggunaan komputer serbaguna untuk penandatanganan transaksi (meskipun
offline).

    Published for educational purposes only to understand "what would it take to sign offline".

    It is generally better to use a hardware wallet like Trezor or Ledger.

    Opinions may vary.

!!! Catatan: Ini adalah tutorial tamu yang disumbangkan oleh
[crocket](https://github.com/crocket).

Penandatanganan transaksi offline meliputi:

* Membuat transaksi tanpa tanda tangan pada dompet online yang hanya dapat
  dilihat
* Memindahkan transaksi yang belum ditandatangani ke mesin offline
* Menandatangani transaksi yang belum ditandatangani pada mesin offline
* Pindahkan transaksi yang telah ditandatangani kembali ke dompet daring yang
  hanya dapat dilihat
* Menyiarakan transaksi

## Membuat dompet offline baru

Untuk membuat dompet offline baru, jalankan perintah berikut:

```
monero-wallet-cli --generate-new-wallet /path/to/wallet-file
```

di perangkat yang tidak terhubung ke internet. Catat seed tersebut di atas
kertas dengan menjalankan perintah `seed` pada dompet offline.

## Membuat dompet offline baru dengan frasa sandi offset benih

Kata sandi benih dan kata sandi offset benih digabungkan untuk membuat benih
baru. Anda dapat menyimpan kata sandi benih dan kata sandi offset benih di
tempat yang terpisah sehingga pencuri tidak dapat mencuri dana Anda tanpa
mencuri kata sandi benih dan kata sandi offset benih tersebut. Saya
merekomendasikan 6 hingga 8 kata (bahasa Inggris) sebagai frasa sandi offset
benih, karena satu kata bahasa Inggris rata-rata memiliki 11 bit entropi dan 8
kata memiliki 88 bit entropi. Dengan frasa sandi benih, Anda juga dapat membuat
dompet umpan yang berisi sedikit uang dan dapat melindungi Anda dari penyiksa
atau pemeras yang menuntut uang dari Anda.

Jika Anda ingin membuat dompet offline dengan seed dan frasa sandi seed, buatlah
dompet offline, catat seed tersebut di atas kertas, hapus berkas dompet, buat
frasa sandi offset seed, catat frasa sandi offset seed di atas kertas, dan
jalankan

```
monero-wallet-cli --generate-new-wallet /path/to/wallet-file \
---restore-deterministic-wallet
```

Untuk memulihkan dari seed dan frasa sandi offset seed. Saat Anda memulihkan
dari seed, Anda dapat memasukkan frasa sandi offset seed.

Hasilkan frasa sandi offset awal pada mesin offline atau dengan diceware karena
manusia kurang mahir dalam membuat frasa sandi acak.

Jika Anda ingin membangun kembali dompet offline yang sudah ada yang menerima
atau mengirim transaksi, Anda perlu melakukan langkah tambahan. Lihat
`Memulihkan dompet offline`.

## Membuat dompet baru yang hanya dapat dilihat

Untuk membuat dompet baca-saja, salin alamat utama dan kunci tampilan rahasia
dari dompet offline ke perangkat online tempat dompet baca-saja akan dibuat.
Anda dapat memperoleh alamat utama dengan menjalankan perintah `address` pada
dompet offline, dan kunci tampilan rahasia dengan menjalankan perintah `viewkey`
pada dompet offline tersebut.

Anda dapat menggunakan kartu microSD dan dua pembaca kartu microSD USB untuk
mentransfer data antara dompet offline dan dompet yang hanya dapat dilihat. Anda
juga dapat menggunakan flash drive USB.

Untuk membuat dompet yang hanya dapat dilihat di mesin daring, jalankan

```
monero-wallet-cli --generate-from-view-key /path/to/wallet-file \
--daemon-address remote-node-address:port
```

Jika Anda ingin memulihkan dompet yang hanya dapat dilihat yang pernah menerima
atau mengirim transaksi, silakan lihat `Memulihkan dompet yang hanya dapat
dilihat`.

## Meluncurkan dompet offline

Jalankan

```
monero-wallet-cli --wallet-file /path/to/wallet-file
```

## Meluncurkan dompet hanya-lihat

Jalankan

```
monero-wallet-cli --wallet-file /path/to/wallet-file \
--daemon-address remote-node-address:port
```

Sinkronisasi dompet Anda melalui clearnet aman dilakukan. Jika Anda ingin
menyiarkan transaksi tanpa mengungkapkan alamat IP Anda, jalankan perintah
berikut

```
monero-wallet-cli --wallet-file /path/to/wallet-file \
--daemon-address tor-or-i2p-remote-node-address:port \
--proxy 127.0.0.1:tor-or-i2p-port
```

Sinkronisasi dompet melalui clearnet jauh lebih cepat daripada melakukannya
melalui Tor atau i2p. Oleh karena itu, pertimbangkan untuk melakukan
sinkronisasi melalui clearnet meskipun Anda menyiarkan transaksi melalui Tor
atau i2p.

## Penandatanganan transaksi offline

Jalankan perintah dompet apa pun yang mentransfer Monero ke alamat mana pun.
Misalnya,

```
transfer xmr-address amount-of-xmr-to-send
```

Perintah transfer apa pun pada dompet hanya-lihat akan membuat
`unsigned_monero_tx` di direktori kerja saat ini.

Pindahkan `unsigned_monero_tx` ke mesin offline yang memiliki dompet offline.
Jalankan

```
sign_transfer
```

di dompet offline pada direktori yang berisi berkas `unsigned_monero_tx`. Berkas
`signed_monero_tx` akan dibuat di direktori kerja saat ini. Pindahkan berkas
`signed_monero_tx` ke mesin online yang menggunakan dompet hanya-baca. Di
direktori yang berisi berkas `signed_monero_tx`, jalankan dompet hanya-baca,
lalu jalankan

```
submit_transfer
```

Karena dompet hanya-baca tidak memiliki gambar kunci, dompet tersebut tidak
dapat melihat transaksi keluar. Agar dompet hanya-baca dapat melihat transaksi
keluar, dompet tersebut harus mengekspor output baru yang dibuat oleh
`submit_transfer` ke dompet offline yang akan membuat gambar kunci dari output
baru tersebut.

Jalankan

```
export_outputs outputs
```

pada dompet yang hanya dapat dilihat. Pindahkan berkas `outputs` ke komputer
offline yang menggunakan dompet offline. Buka dompet offline tersebut, lalu
jalankan

```
import_outputs /path/to/outputs
```

Ekspor gambar-gambar utama yang dihasilkan dari hasil baru dengan menjalankan

```
export_key_images key_images
```

di dompet offline. Pindahkan berkas `key_images` ke perangkat yang memiliki
dompet hanya-baca. Buka dompet hanya-baca tersebut, lalu jalankan

```
import_key_images /path/to/key_images
```

## Memperbarui perangkat lunak dompet pada mesin penandatanganan offline

Saat Anda memperbarui perangkat offline yang menggunakan dompet offline, Anda
tidak bisa begitu saja menghubungkan perangkat tersebut ke internet dan
memperbarui perangkat lunak dompet, karena hal itu akan membuat dompet offline
terpapar ke internet.

Sebaliknya, jalankan media instalasi sistem operasi, hapus seluruh sistem
berkas, lalu sambungkan ke internet, dan instal semuanya dari awal lagi.

Jika sistem berkas root Anda dienkripsi, media instalasi sistem operasi dapat
terhubung ke internet sejak awal karena data yang dienkripsi tetap aman hingga
dienkripsi.

## Memulihkan dompet offline

Setelah memperbarui perangkat lunak dompet pada mesin penandatanganan offline
dengan menghapus seluruh datanya dan menginstal ulang semuanya, Anda harus
memulihkan dompet offline tersebut.

Pulihkan dompet offline dari frasa benih (dan frasa sandi offset benih) dengan
menjalankan

```
monero-wallet-cli --generate-new-wallet wallet-file --restore-deterministic-wallet
```

Dompet offline yang baru tidak dapat menandatangani transaksi baru karena tidak
memiliki semua output transaksi yang mendahului transaksi baru yang belum
ditandatangani tersebut. Oleh karena itu, dompet tersebut harus terlebih dahulu
mengimpor semua output dari dompet yang hanya dapat dilihat.

Pada dompet yang hanya dapat dilihat yang dibuat dari dompet offline, jalankan

```
export_outputs all all_outputs
```

`all` penting karena `export_outputs` hanya mengekspor output baru yang
sebelumnya belum diekspor, tetapi

```
export_outputs all
```

mengekspor semua hasil. Pindahkan berkas `all_outputs` ke mesin offline yang
memiliki dompet offline. Jalankan

```
import_outputs /path/to/all_outputs
```

pada dompet offline yang baru.

## Mengembalikan dompet hanya-lihat

Jika Anda merekonstruksi dompet hanya-lihat, karena tidak memiliki citra kunci,
dompet tersebut tidak dapat melihat transaksi keluar. Jika tidak dapat melihat
transaksi keluar, dompet tersebut akan melaporkan saldo akun yang salah. Oleh
karena itu, dompet tersebut harus mengimpor semua citra kunci dari dompet
offline yang sesuai.

Pada dompet offline, jalankan

```
export_key_images all all_key_images
```

`export_key_images` tidak berfungsi karena hanya mengekspor gambar kunci baru
yang belum pernah diekspor sebelumnya.

```
export_key_images all
```

Mengekspor semua gambar kunci. Pindahkan file `all_key_images` ke mesin dengan
dompet hanya-lihat. Jalankan

```
import_key_images /path/to/all_key_images
```
