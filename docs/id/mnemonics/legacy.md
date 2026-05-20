---
title: Legacy Mnemonic Scheme
---

Skema mnemonik warisan adalah skema mnemonik tertua dan paling banyak digunakan
dalam ekosistem Monero. Skema ini terdiri dari total 25 kata, di mana 24 kata
pertama adalah untuk benih dan kata terakhir adalah untuk checksum. Kata
checksum digunakan untuk memverifikasi kebenaran benih.

24 kata pertama dipilih secara acak dari daftar 1626 kata yang dijelaskan dalam
[`src/mnemonics/english.h`](https://github.com/monero-project/monero/blob/master/src/mnemonics/english.h)
(Daftar kata untuk bahasa lain dapat ditemukan di
[`src/mnemonics`](https://github.com/monero-project/monero/tree/master/src/mnemonics)).
Kata checksum dipilih dengan menghitung [indeks checksum
CRC32](https://en.wikipedia.org/wiki/Cyclic_redundancy_check) dari string yang
dibuat dengan menggabungkan karakter pertama yang panjangnya `prefix_length`
dari setiap kata yang dipilih. `prefix_length` adalah jumlah karakter yang akan
digunakan dari setiap kata untuk menghitung checksum. [Dalam kasus daftar kata
bahasa Inggris, `prefix_length` adalah
3](https://github.com/monero-project/monero/blob/master/src/mnemonics/english.h#L52C47-L52C48).

Example of calculating the checksum word:

1. Randomly select (don't forget that randomness should be [cryptographically
   secure](https://en.wikipedia.org/wiki/Cryptographically_secure_pseudorandom_number_generator))
   24 words from the wordlist. For example, let's say the chosen words are `lush
   bagpipe stacking mice imitate village gang efficient strained different
   together vain puck roped pancakes shocking liar moisture memoir sorry
   syndrome kettle swept dehydrate`.
2. Take the first 3 characters of each word and concatenate them. In this case,
   it will be
   `lusbagstamicimivilganeffstrdiftogvaipucroppansholiamoimemsorsynketswedeh`.
3. Calculate the CRC32 checksum of the concatenated string. In this case, the
   checksum gives us the decimal number `2248614488`.
4. Take the checksum index modulo 24. In this case, the modulo gives us `8`.
5. The 8th index of the wordlist is `strained` (don't forget that the wordlist
   is 0-indexed). So, the checksum word is `strained`.
