# EBS-Tema practica

* Pentru rezolvarea temei practice, am ales sa folosim limbajul de programare Python.
* Pentru partea de paralelizare am ales sa folosim thread-urile. Am creat thread-urile cu ajutorul bibliotecii `threading`.
* Ca factor de paralelizare, am ales ca pentru generarea fiecarui obiect creat (fie subscriptie, fie publicatie) sa fie creat un nou thread.
* Am rulat codul pentru pentru doua tipuri de paralelizare:
  * 1<sup>st</sup>: fara paralelizare;
  * 2<sup>nd</sup>: cu paralelizare pentru fiecare obiect creat;
* Am rulat pentru diferite numere de mesaje (100, 10 000 mesaje (publicatii, respectiv subscriptii)).
* Timpii obtinuti pentru rularea pe 10 000 de publicatii au fost:
  * Timp de generare 100 publicatii fara thread-uri: 0.0011636999999999897;
  * Timp de generare 100 publicatii cu thread-uri: 0.0352605;
  
  * Timp de generare 1000 publicatii fara thread-uri :0.003995800158008933; 
  * Timp de generare 1000 publicatii cu thread-uri: 0.2095170000102371;
  
* Tipurile de procesoare pe care a fost rulat codul sunt:
  * Procesor	Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz   1.99 GHz;
  * AMD Ryzen 9.4900HS;

