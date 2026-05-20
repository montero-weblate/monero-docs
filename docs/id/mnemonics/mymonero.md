---
title: MyMonero Mnemonic Scheme
---

Skema MyMonero dapat dianggap sebagai versi 13 kata dari [Skema Mnemonik
Warisan](./legacy.md). Sebagian besar proses tetap sama dalam kedua skema,
tetapi tentu saja ada hal-hal yang berbeda. Misalnya, metode untuk menurunkan
checksum dan metode untuk menurunkan benih heksadesimal sama, tetapi karena
MyMonero menghasilkan benih heksadesimal yang lebih pendek, menurunkan kunci
privat dari benih heksadesimal itu berbeda dibandingkan dengan Warisan.

Bagi pengguna yang ingin mengonversi benih MyMonero ke benih warisan, konverter
offline dapat ditemukan di
[xmr.llcoins.net](https://github.com/luigi1111/xmr.llcoins.net/).

The MyMonero scheme was initially used by MyMonero web and mobile wallet, but
other projects also adopted this scheme. The scheme is designed to be more
user-friendly and easier to remember than the legacy scheme.

The MyMonero scheme comprises a total of 13 words, where the first 12 words are
for the seed and the last word is for the checksum. The checksum word is used to
verify the correctness of the seed.

Deriving checksum process is the same as the [Legacy Mnemonic
Scheme](./legacy.md), you can check out the details from that page.
