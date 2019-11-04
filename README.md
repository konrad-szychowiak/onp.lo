# onp.lo

> **o**dwrotna **n**otacja **p**olska (**l**ogika **o**bliczeniowa)
>
>  Program tłumaczący notację postfiksową na infiksową, implementacja w języku python&nbsp;3.x.

## Zadanie

> Zaimplementuj wczytywanie formuł rachunku predykatów w odwrotnej notacji polskiej (ONP) i wypisywanie ich w postaci infiksowej. Formuły w ONP podawane są na standardowe wejście programu, a ich odpowiedniki powinny być wypisane na standardowe wyjście. Każda formuła na wejściu zapisana jest w nowej linii, w odpowiadających liniach wyjścia powinny być formuły zapisane w postaci infiksowej. [cytat]

+ Kolejne **formuły** na wejściu oddzielone są znakami nowej linii.

+ Kolejne **symbole** w obrębie formuły na wejściu oddzielone są spacjami.

+ **Stałe** oznaczone są zawsze pojedynczą małą literą alfabetu łacińskiego od a do e.

+ **Zmienne** oznaczone są zawsze pojedynczą wielką literą alfabetu łacińskiego.

+ **Symbole funkcyjne** są zawsze oznaczone pojedynczą małą literą alfabetu łacińskieg od **_f_** do **_n_**, po której następuje `/` i jedna cyfra określająca liczbę argumentów (arność) symbolu

+ **Symbole predykatywne** są zawsze oznaczone pojedynczą małą literą alfabetu łacińskieg od **_p_** do **_z_**, po której następuje `/` i jedna cyfra określająca liczbę argumentów (arność) symbolu

+ **Operatory** i **kwantyfikatory** mogą być oznaczone w jeden z następujących sposobów (program musi obsługiwać wszystkie warianty).

---

| element składni                  | symbol | przestrzeń nazw   |
| -------------------------------- |:------:| ----------------- |
| **stała**                        |  `c`   | `a`..`e`          |
| **zmienna**                      |  `X`   | `A`..`Z`          |
| **symbol funkcyjny**             | `f/1`  | `f`..`n`          |
| **symbol predykatywny**          | `p/1`  | `p`..`z`          |
| **negacja**                      |  `¬`   | `NOT`, `~`, `¬`   |
| **koniunkcja**                   |  `∧`   | `AND`, `&`, `∧`   |
| **alternatywa** (~~dysjunkcja~~) |  `∨`   | `OR`, &vert;, `∨` |
| **implikacja**                   |  `→`   | `IMPLIES`, `→`    |
| **równoważność**                 |  `↔`   | `IFF`, `↔`        |
| alternatywa **wykluczająca**     |  `⊕`   | `XOR`, `⊕`        |
| kwantyfikator **uniwersalny**     |  `∀`   | `FORALL`, `∀`     |
| kwantyfikator **egzystencjalny**  |  `∃`   | `EXISTS`, `∃`     |

### Wejście (przykład)

```py
a p/1
Z Z p/1 EXISTS
Z X X a f/2 p/1 ∃ Y Y Z f/1 p/2 FORALL → FORALL
Z Y X X b c q/3 Z Y f/1 p/2 ~ & EXISTS FORALL EXISTS
```

### Wyjście (przykład)

```py
p(a)
(EXISTS Z p(Z))
(FORALL Z ((∃ X p(f(X, a))) → (FORALL Y p(Y, f(Z)))))
(EXISTS Z (FORALL Y (EXISTS X (q(X, b, c) & (~ p(Z, f(Y)))))))
```

[cytat]: https://moodle.put.poznan.pl/mod/page/view.php?id=53864
