---
title: Asymmetric Cryptography in Monero
---
# Kriptografi Asimetris di Monero

!!! Catatan: Penulis sama sekali bukan seorang kriptografer. Harap skeptis
terhadap keakuratannya.

Sebelum kita sampai ke hal-hal spesifik Monero, sedikit konteks. Kita berbicara
tentang kriptografi asimetris di sini. "Asimetris" berarti ada dua kunci:

* kunci privat (digunakan terutama untuk menandatangani data dan untuk
  mendekripsi data)
* kunci publik (digunakan terutama untuk verifikasi tanda tangan dan enkripsi
  data)

Ini berbeda dengan kriptografi simetris yang menggunakan satu kunci. Kunci ini
adalah rahasia yang dibagikan di antara pihak-pihak.

Secara historis, kriptografi asimetris didasarkan pada masalah faktorisasi
bilangan bulat yang sangat besar kembali menjadi bilangan prima (yang secara
praktis tidak mungkin untuk bilangan bulat yang cukup besar).

Baru-baru ini, kriptografi asimetris didasarkan pada gagasan matematis kurva
eliptik. Edwards25519 adalah kurva eliptik tertentu yang diteliti dengan baik
dan distandarkan yang digunakan dalam Monero.
