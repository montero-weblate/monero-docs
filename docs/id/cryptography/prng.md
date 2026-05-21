---
title: Monero Pseudorandom Number Generator
---
# Generator Bilangan Pseudoacak Monero

Monero menggunakan PRNG berdasarkan fungsi hashing Keccak. Pada dasarnya,
keluaran putaran hashing sebelumnya adalah masukan untuk yang berikutnya.

Benih awal berasal dari sumber entropi yang disediakan oleh sistem operasi. Di
Linux dan MacOS, benih berasal dari `/dev/urandom`. Di Windows, panggilan WinAPI
`CryptGenRandom` digunakan untuk penyemaian.

Tidak ada penyemaian ulang.

## Caveats

* This concerns the reference C++ implementation of Monero. Please note there
  are many alternative implementations of private key generation, including
  JavaScript, Python, Android/Java. These should be researched case by case for
  correctness.
* In Monero source code you can also find libsodium based random bytes
  generator. It is part of the embedded library and apparently is not used in
  actual Monero code.

## Referensi

* [Source
  code](https://github.com/monero-project/monero/blob/1a4298685aa9e694bc555ae69be59d14d3790465/src/crypto/random.c)
* [StackExchange answer](https://monero.stackexchange.com/a/2076/3218)
