# Définition des constantes
VARIABLE = "variable"
NEGATION = "negation"
DISJUNCTION = "disjunction"
CONJUNCTION = "conjunction"
CONDITION = "condition"

# Fonctions pour créer des objets de formules logiques
def variable(name):
    return {"type": VARIABLE, "name": name}

def not_(formula):
    return {"type": NEGATION, "formula": formula}

def connective(type_, left, right):
    return {"type": type_, "left": left, "right": right}

def or_(left, right):
    return connective(DISJUNCTION, left, right)

def and_(left, right):
    return connective(CONJUNCTION, left, right)

def implies(left, right):
    return connective(CONDITION, left, right)

# Vérification si une formule est en CNF
def is_cnf(formula):
    return (
        is_cnf_disjunction(formula) or
        (formula["type"] == CONJUNCTION and
         (is_cnf(formula["left"]) or is_cnf_disjunction(formula["left"])) and
         (is_cnf(formula["right"]) or is_cnf_disjunction(formula["right"])))
    )

def is_cnf_disjunction(formula):
    return (
        is_cnf_atom(formula) or
        (formula["type"] == DISJUNCTION and
         (is_cnf_disjunction(formula["left"]) or is_cnf_atom(formula["left"])) and
         (is_cnf_disjunction(formula["right"]) or is_cnf_atom(formula["right"])))
    )

def is_cnf_atom(formula):
    return (
        formula["type"] == VARIABLE or
        (formula["type"] == NEGATION and formula["formula"]["type"] == VARIABLE)
    )

# Conversion d'une formule en CNF
def cnf(formula):
    if is_cnf(formula):
        return formula
    if formula["type"] == NEGATION:
        return negated_cnf(formula["formula"])
    if formula["type"] == CONJUNCTION:
        return and_(cnf(formula["left"]), cnf(formula["right"]))
    if formula["type"] == DISJUNCTION:
        left = cnf(formula["left"])
        right = cnf(formula["right"])
        return (
            right if left["type"] != CONJUNCTION else
            (right if right["type"] != CONJUNCTION else
             cnf(and_(or_(left["left"], right["left"]),
                       or_(left["left"], right["right"]),
                       or_(left["right"], right["left"]),
                       or_(left["right"], right["right"]))))
        )
    if formula["type"] == CONDITION:
        return cnf(or_(not_(formula["left"]), formula["right"]))

def negated_cnf(formula):
    if formula["type"] == NEGATION:
        return cnf(formula["formula"])
    if formula["type"] == DISJUNCTION:
        return cnf(and_(not_(formula["left"]), not_(formula["right"])))
    if formula["type"] == CONJUNCTION:
        return cnf(or_(not_(formula["left"]), not_(formula["right"])))
    if formula["type"] == CONDITION:
        return cnf(and_(formula["left"], not_(formula["right"])))

# Fonctions pour la conversion en chaîne de caractères
def group(formula):
    if formula["type"] in [VARIABLE, NEGATION]:
        return stringify(formula)
    return "(" + stringify(formula) + ")"

def stringify(formula):
    if formula["type"] == VARIABLE:
        return formula["name"]
    if formula["type"] == NEGATION:
        return "~" + group(formula["formula"])
    if formula["type"] == CONJUNCTION:
        return group(formula["left"]) + "^" + group(formula["right"])
    if formula["type"] == DISJUNCTION:
        return group(formula["left"]) + "v" + group(formula["right"])
    if formula["type"] == CONDITION:
        return group(formula["left"]) + "→" + group(formula["right"])

# Fonction pour déterminer la précédence des opérateurs
def precedence(expression):
    output = "(("
    preced = {"^": ")^(", "v": "))v((", "→": "))→((", "(": "((", ")": "))"}
    for ch in expression:
        output += preced[ch] if ch in preced else ch
    return output + "))"

# Fonction pour analyser une chaîne de caractères et la convertir en formule logique
def parse(expression):
    iter_exp = iter(expression)
    def recur(end):
        formula = None
        connectives = []
        for ch in iter_exp:
            if ch == end:
                break
            if ch in "^v~→":
                connectives.append(ch)
            else:
                arg = recur(")") if ch == "(" else variable(ch)
                while connectives:
                    oper = connectives.pop()
                    if oper == "~":
                        arg = not_(arg)
                    elif oper == "^":
                        arg = and_(formula, arg)
                    elif oper == "v":
                        arg = or_(formula, arg)
                    elif oper == "→":
                        arg = implies(formula, arg)
                formula = arg
        return formula
    return recur("")


    return recur("")

# Fonction pour vérifier la validité des clauses CNF
def valide(clauses):
    atoms = []
    not_atoms = {}

    for clause in clauses:
        updated_clause = clause[1:-1] if clause[0] == "(" else clause
        single_atoms = updated_clause.split("v")
        for atom in single_atoms:
            atoms.append(atom)
            if atom[0] == "~":
                not_atoms[atom] = not_atoms.get(atom, 0) + 1
            else:
                not_atom = "~" + atom
                not_atoms[not_atom] = not_atoms.get(not_atom, 0) - 1

    for a in not_atoms:
        if not_atoms[a]:
            return False
    return True

# Fonction pour vérifier la validité des caractères dans une chaîne
def check_str_validity(string, whitelist):
    return all(char in whitelist for char in string)

# Fonction pour afficher le résultat dans le DOM
def dom_result(formula, not_formula, cnf_formula, clauses, is_valid):
    print("Formula:", formula)
    print("Not Formula:", not_formula)
    print("CNF Formula:", cnf_formula)
    print("Clauses:", clauses)
    print("Result:", "valide" if is_valid else "invalide")

# Fonction pour effacer le DOM
def clear_dom():
    print("Clearing DOM...")

# Point d'entrée de l'application
def main():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    whitelist = "~v^>()→" + alpha + alpha.upper()  # Définir la variable whitelist ici
    while True:
        clear_dom()
        original_formula = precedence(input("Enter the formula: "))

        if not check_str_validity(original_formula, whitelist):
            print("Invalid characters in formula")
            continue

        formula = parse(original_formula)
        to_str_formula = stringify(formula)
        not_formula = "~(" + to_str_formula + ")"
        cnf_formula = stringify(cnf(parse(not_formula)))
        clauses = cnf_formula.split("^")
        for i in range(len(clauses)):
            clauses[i] = clauses[i].replace("(", "").replace(")", "")
        print("clauses : ", clauses)
        is_valid = valide(clauses)

        dom_result(to_str_formula, not_formula, cnf_formula, clauses, is_valid)

if __name__ == "__main__":
    main()
