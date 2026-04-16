# =========================
# 1. DEFINICIÓN DE GRAMÁTICA
# =========================

# Gramática original:
# S → A a A b | B b B a
# A → ε
# B → ε

grammar = {
    "S": [["A", "a", "A", "b"], ["B", "b", "B", "a"]],
    "A": [["ε"]],
    "B": [["ε"]]
}

non_terminals = ["S", "A", "B"]
terminals = ["a", "b"]

# =========================
# 2. INICIALIZACIÓN
# =========================

FIRST = {}
FOLLOW = {}

for nt in non_terminals:
    FIRST[nt] = set()
    FOLLOW[nt] = set()

# Símbolo inicial
FOLLOW["S"].add("$")

# =========================
# 3. CÁLCULO DE FIRST
# =========================

changed = True
while changed:
    changed = False

    for nt in grammar:
        for production in grammar[nt]:

            for symbol in production:

                # Caso terminal
                if symbol in terminals:
                    if symbol not in FIRST[nt]:
                        FIRST[nt].add(symbol)
                        changed = True
                    break

                # Caso epsilon
                elif symbol == "ε":
                    if "ε" not in FIRST[nt]:
                        FIRST[nt].add("ε")
                        changed = True
                    break

                # Caso no terminal
                else:
                    before = len(FIRST[nt])

                    for val in FIRST[symbol]:
                        if val != "ε":
                            FIRST[nt].add(val)

                    if "ε" not in FIRST[symbol]:
                        break

                    if len(FIRST[nt]) > before:
                        changed = True
            else:
                if "ε" not in FIRST[nt]:
                    FIRST[nt].add("ε")
                    changed = True

# =========================
# 4. CÁLCULO DE FOLLOW
# =========================

changed = True
while changed:
    changed = False

    for nt in grammar:
        for production in grammar[nt]:

            for i in range(len(production)):
                symbol = production[i]

                if symbol in non_terminals:

                    # Caso: hay símbolos después
                    if i + 1 < len(production):
                        next_symbol = production[i + 1]

                        # Terminal
                        if next_symbol in terminals:
                            if next_symbol not in FOLLOW[symbol]:
                                FOLLOW[symbol].add(next_symbol)
                                changed = True

                        # No terminal
                        else:
                            before = len(FOLLOW[symbol])

                            for val in FIRST[next_symbol]:
                                if val != "ε":
                                    FOLLOW[symbol].add(val)

                            if "ε" in FIRST[next_symbol]:
                                for val in FOLLOW[nt]:
                                    FOLLOW[symbol].add(val)

                            if len(FOLLOW[symbol]) > before:
                                changed = True

                    # Caso: último símbolo
                    else:
                        before = len(FOLLOW[symbol])

                        for val in FOLLOW[nt]:
                            FOLLOW[symbol].add(val)

                        if len(FOLLOW[symbol]) > before:
                            changed = True

# =========================
# 5. CONSTRUCCIÓN TABLA LL(1)
# =========================

table = {}
conflict = False

for nt in grammar:
    table[nt] = {}

    for production in grammar[nt]:

        first_set = set()

        for symbol in production:

            if symbol in terminals:
                first_set.add(symbol)
                break

            elif symbol == "ε":
                first_set.add("ε")
                break

            else:
                for val in FIRST[symbol]:
                    if val != "ε":
                        first_set.add(val)

                if "ε" not in FIRST[symbol]:
                    break
        else:
            first_set.add("ε")

        # Llenado de tabla
        for terminal in first_set:
            if terminal != "ε":
                if terminal in table[nt]:
                    conflict = True
                table[nt][terminal] = production

        # Caso epsilon
        if "ε" in first_set:
            for terminal in FOLLOW[nt]:
                if terminal in table[nt]:
                    conflict = True
                table[nt][terminal] = production

# =========================
# 6. RESULTADOS
# =========================

print("=== GRAMÁTICA ===")
for nt in grammar:
    print(nt, "→", grammar[nt])

print("\n=== FIRST ===")
for nt in FIRST:
    print(nt, ":", FIRST[nt])

print("\n=== FOLLOW ===")
for nt in FOLLOW:
    print(nt, ":", FOLLOW[nt])

print("\n=== TABLA LL(1) ===")
for nt in table:
    for t in table[nt]:
        print(f"M[{nt}, {t}] = {table[nt][t]}")

print("\n=== RESULTADO FINAL ===")
if conflict:
    print(" La gramática NO es LL(1)")
else:
    print("✔ La gramática ES LL(1)")