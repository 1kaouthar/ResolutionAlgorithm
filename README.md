### Resolution Algorithm

This Python script provides functionalities for resolution algorithms in propositional logic. It includes functions to create logical formulas, check if a formula is in Conjunctive Normal Form (CNF), convert formulas to CNF, parse logical expressions from strings, and validate CNF clauses.

### Usage

To use this script, follow these steps:

1. Clone the repository or download the script.
2. Ensure you have Python installed on your system.
3. Run the script in your preferred Python environment.

### Functions

1. **Constants:**
   - `VARIABLE`, `NEGATION`, `DISJUNCTION`, `CONJUNCTION`, `CONDITION`: Define constants for different types of logical connectives.

2. **Logical Formula Creation:**
   - `variable(name)`: Create a variable object.
   - `not_(formula)`: Create a negation object.
   - `connective(type_, left, right)`: Create a connective object.
   - `or_(left, right)`: Create a disjunction (OR) object.
   - `and_(left, right)`: Create a conjunction (AND) object.
   - `implies(left, right)`: Create a conditional (IMPLIES) object.

3. **CNF Verification and Conversion:**
   - `is_cnf(formula)`: Check if a formula is in CNF.
   - `is_cnf_disjunction(formula)`: Check if a disjunction is in CNF.
   - `is_cnf_atom(formula)`: Check if an atom is in CNF.
   - `cnf(formula)`: Convert a formula to CNF.
   - `negated_cnf(formula)`: Convert a negated formula to CNF.

4. **String Conversion:**
   - `group(formula)`: Group a formula for string conversion.
   - `stringify(formula)`: Convert a formula to a string.

5. **Precedence:**
   - `precedence(expression)`: Determine the precedence of operators in an expression.

6. **Parsing:**
   - `parse(expression)`: Parse a string into a logical formula.

7. **CNF Clause Validation:**
   - `valide(clauses)`: Check the validity of CNF clauses.

8. **Utility Functions:**
   - `check_str_validity(string, whitelist)`: Check the validity of characters in a string.
   - `dom_result(formula, not_formula, cnf_formula, clauses, is_valid)`: Display the result in the DOM.
   - `clear_dom()`: Clear the DOM.

### Running the Script

1. Run the script in a Python environment.
2. Enter the logical formula when prompted.
3. The script will display the formula, its negation, CNF formula, CNF clauses, and whether it is valid or not.

### Example

An example of a logical formula is `(p ^ q) v (~r → s)`.

### Note

Ensure that the logical formulas you input follow the rules of propositional logic and are well-formed. Invalid characters will result in errors.# ResolutionAlgorithm
This Python script provides functionalities for resolution algorithms in propositional logic. It includes functions to create logical formulas, check if a formula is in Conjunctive Normal Form (CNF), convert formulas to CNF, parse logical expressions from strings, and validate CNF clauses
