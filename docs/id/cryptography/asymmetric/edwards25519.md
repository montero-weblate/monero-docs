---
title: Edwards25519 Elliptic Curve
---
# Kurva Elips Edwards25519

!!! Catatan: Penulis sama sekali bukan seorang kriptografer. Harap skeptis
terhadap keakuratannya.

!!! note Artikel ini hanya tentang kurva yang mendasar. Derivasi kunci publik
dan algoritma penandatanganan akan dibahas secara terpisah.

Monero menggunakan kurva eliptik edwards25519 sebagai dasar untuk pembuatan
pasangan kuncinya.

Kurva berasal dari skema tanda tangan Ed25519. Meskipun Monero mengambil kurva
tanpa perubahan, skema ini tidak benar-benar mengikuti sisa Ed25519.

Kurva edwards25519 adalah [setara secara birasional dengan
Curve25519](https://tools.ietf.org/html/rfc7748#section-4.1).

## Definisi

Ini adalah definisi kurva edwards25519 standar, tidak ada hal spesifik Monero di
sini, kecuali konvensi penamaan. Konvensi berasal dari whitepaper CryptoNote dan
banyak digunakan dalam literatur Monero.

### Persamaan kurva

    −x^2 + y^2 = 1 − (121665/121666) * x^2 * y^2

Catatan:

* kurva berada dalam dua dimensi (tidak ada yang istimewa, seperti semua kurva
  di sekolah menengah)
* kurva dicerminkan di bawah sumbu y karena bagian `y^2` dari persamaan (bukan
  polinomial)

### Titik dasar: `G`

Titik dasar adalah titik spesifik pada kurva. Titik ini digunakan sebagai dasar
untuk perhitungan lebih lanjut. Ini adalah pilihan arbitrer oleh penulis kurva,
hanya untuk menstandarkan skema.

Perhatikan bahwa cukup untuk menentukan nilai y dan tanda nilai x. Itu karena x
spesifik dapat dihitung dari persamaan kurva.

    G = (x, 4/5)  # take the point with the positive x

    # The hex representation of the base point
    5866666666666666666666666666666666666666666666666666666666666666    

### Orde prima dari titik dasar: `l`

Dalam istilah awam, "kanvas" tempat kurva digambar diasumsikan memiliki
"resolusi" yang terbatas, jadi koordinat titik harus "membungkus" pada suatu
titik. Ini dicapai dengan modulo nilai `l` (huruf L kecil). Dengan kata lain,
`l` mendefinisikan skalar maksimum yang dapat kami gunakan.

    l = 2^252 + 27742317777372353535851937790883648493
    # => 7237005577332262213973186563042994240857116359379907606001950938285454250989

`l` adalah bilangan prima yang ditentukan oleh penulis kurva.

Dalam praktik ini adalah kekuatan kunci privat.

### Jumlah total titik pada kurva

Jumlah total titik pada kurva juga merupakan bilangan prima:

    q = 2^255 - 19

Dalam praktik tidak semua titik "berguna" dan oleh karena itu kekuatan kunci
privat dibatasi pada `l` yang dijelaskan di atas.

## Implementasi

Monero menggunakan implementasi Ref10 (tampaknya dimodifikasi) oleh Daniel J.
Bernstein.

## Referensi

* [Pengantar (Relatif Mudah Dipahami) tentang Kriptografi Kurva
  Eliptik](https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/)
* [RFC 8032 yang mendefinisikan EdDSA](https://tools.ietf.org/html/rfc8032)
* [Memahami Kriptografi
  Monero](https://steemit.com/monero/@luigi1111/understanding-monero-cryptography-privacy-introduction)
  - tulisan yang sangat baik oleh Luigi
* [Jawaban
  StackOverflow](https://monero.stackexchange.com/questions/2290/why-how-does-monero-generate-public-ed25519-keys-without-using-the-standard-publ)
* [Implementasi
  Python](https://github.com/monero-project/mininero/blob/master/ed25519.py) -
  bukan yang referensi tetapi lebih mudah dipahami
* [Enkode titik ke
  hex](https://monero.stackexchange.com/questions/6050/what-is-the-base-point-g-from-the-whitepaper-and-how-is-it-represented-as-a)
* [EdDSA di Wikipedia](https://en.wikipedia.org/wiki/EdDSA)
