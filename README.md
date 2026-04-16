# Parcial Lenguajes Formales y Compiladores

Este repositorio contiene la solución completa del parcial, donde se abordan conceptos fundamentales de **gramáticas formales, análisis sintáctico, parsers y herramientas de compilación**.

El proyecto está dividido en 5 puntos principales, cada uno enfocado en un aspecto específico del análisis de lenguajes.

---

# 📁 Estructura del proyecto

```
parcial_lenguajes_2/
│
├── punto1_2_antlr/
├── punto3_ll1/
├── punto4_comparacion/
├── punto5_yacc/
│
└── docs/
    └── documentacion_de_los_ejercicios.pdf
```

---

# 📄 Documentación completa

Este repositorio incluye un documento detallado con:

* Desarrollo paso a paso
* Explicaciones teóricas
* Procedimientos realizados
* Evidencias

📌Archivo:

```
docs/documentacion_de_los_ejercicios.pdf
```

---

# ⚙️ Requisitos generales

Para ejecutar todos los puntos necesitas:

* Python 3
* Java (para ANTLR)
* ANTLR4
* Flex
* Bison (YACC)
* GCC

---

#  Punto 1 y 2 — Gramática ANTLR (CRUD NoSQL)

##  Descripción

Se diseñó una gramática en ANTLR para modelar operaciones tipo CRUD en una base de datos NoSQL:

* CREATE
* READ
* UPDATE
* DELETE

## 📂 Contenido

* `CRUD.g4` → Gramática principal
* `test.txt` → Entradas de prueba

##  Ejecución

```bash
antlr4 CRUD.g4
javac *.java
grun CRUD prog -tree test.txt
```

##  Teoría

ANTLR permite construir analizadores sintácticos a partir de gramáticas formales.
El parser generado sigue un enfoque **LL(*)**, una extensión de los parsers predictivos LL.

Este tipo de parser:

* Analiza de izquierda a derecha
* Genera derivaciones por la izquierda
* No requiere backtracking en muchos casos

---

# Punto 3 — Verificación LL(1)

## Descripción

Se implementó un programa en Python que:

* Calcula FIRST
* Calcula FOLLOW
* Verifica si una gramática es LL(1)

## 📂 Contenido

* `ll3_verificador_punto2.py`

## Ejecución

```bash
python3 ll3_verificador_punto2.py
```

## 📚 Teoría

Una gramática es LL(1) si:

* No tiene ambigüedad
* No tiene recursión izquierda
* Sus conjuntos FIRST y FOLLOW no generan conflictos

Esto permite construir parsers predictivos eficientes sin retroceso.

---

# Punto 4 — Comparación de Parsers (LL vs CYK)

##  Descripción

Se comparó el rendimiento entre:

* Parser LL (predictivo)
* Algoritmo CYK

## 📂 Contenido

* `parsers_compare_punto4.py`
* Resultados de ejecución
* Gráfica de rendimiento

## Ejecución

```bash
python3 parsers_compare_punto4.py
```

##  Teoría

* LL → Complejidad O(n)
* CYK → Complejidad O(n³)

CYK utiliza programación dinámica y requiere la gramática en **Forma Normal de Chomsky (CNF)**.

## Análisis

Los resultados muestran que:

* LL es altamente eficiente
* CYK es más general pero computacionalmente costoso

Esto evidencia el trade-off entre:

```
Eficiencia vs Generalidad
```

---

# 🔹Punto 5 — Calculadora Booleana (YACC / FLEX)

## Descripción

Se implementó una calculadora de expresiones booleanas utilizando:

* Flex (análisis léxico)
* Bison/YACC (análisis sintáctico)

Soporta:

* AND
* OR
* NOT
* Paréntesis

## 📂 Contenido

* `calc.y`
* `calc.l`

## ▶️Compilación

```bash
bison -d calc.y
flex calc.l
gcc calc.tab.c lex.yy.c -o calc
```

## ▶️Ejecución

```bash
./calc
```

##  Teoría

El parser generado por YACC es de tipo:

```
LALR(1)
```

Características:

* Usa una pila
* Aplica operaciones SHIFT y REDUCE
* Complejidad O(n)

Se definió precedencia:

```
NOT > AND > OR
```

para evitar ambigüedad en la gramática.

---

# Conceptos clave aplicados

* Gramáticas libres de contexto (CFG)
* FIRST y FOLLOW
* Parsers LL y LALR
* Algoritmo CYK
* Forma Normal de Chomsky
* Análisis léxico y sintáctico
* Evaluación semántica

---

#  Conclusión general

El proyecto demuestra la aplicación práctica de los conceptos fundamentales de los compiladores:

* Diseño de lenguajes formales
* Construcción de parsers
* Análisis de eficiencia
* Uso de herramientas industriales (ANTLR, Flex, Bison)

Se evidencia que:

* Los parsers predictivos son eficientes pero restringidos
* Los algoritmos generales como CYK son más flexibles pero costosos
* Las herramientas como YACC permiten construir analizadores robustos de manera sistemática

---

# Autor

Julio Cesar Florez Guarnizo

