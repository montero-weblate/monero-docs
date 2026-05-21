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

Skema MyMonero terdiri dari total 13 kata, di mana 12 kata pertama adalah untuk
benih dan kata terakhir adalah untuk checksum. Kata checksum digunakan untuk
memverifikasi kebenaran benih.

Deriving checksum process is the same as the [Legacy Mnemonic
Scheme](./legacy.md), you can check out the details from that page.
