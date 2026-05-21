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

Skema MyMonero awalnya digunakan oleh dompet web dan mobile MyMonero, tetapi
proyek lain juga mengadopsi skema ini. Skema ini dirancang untuk lebih ramah
pengguna dan lebih mudah diingat daripada skema warisan.

The MyMonero scheme comprises a total of 13 words, where the first 12 words are
for the seed and the last word is for the checksum. The checksum word is used to
verify the correctness of the seed.

Deriving checksum process is the same as the [Legacy Mnemonic
Scheme](./legacy.md), you can check out the details from that page.
