"""OCP Quickstart examples.

Run this script from the OCP repository root. Generated files are written to ``files/``.
See the Quickstart page of the documentation for explanations of each example.
"""

import primitives.speck as speck
import implementations.implementations as imp
import visualisations.visualisations as vis
import attacks.attacks as attacks


# ---------------------------------------------------------------------------
# Example 1: generate an implementation (Python and C, rolled and unrolled)
# ---------------------------------------------------------------------------
cipher = speck.SPECK_PERMUTATION(version=32)   # full rounds (r=22)
tv = cipher.test_vectors[0]                     # an (input, output) test vector

# Python, rolled
imp.generate_implementation(cipher, f"files/{cipher.name}.py", "python")
imp.test_implementation_python(cipher, cipher.name, tv[0], tv[1])

# Python, unrolled
imp.generate_implementation(cipher, f"files/{cipher.name}_unrolled.py", "python", True)
imp.test_implementation_python(cipher, f"{cipher.name}_unrolled", tv[0], tv[1])

# C, rolled
imp.generate_implementation(cipher, f"files/{cipher.name}.c", "c")
imp.test_implementation_c(cipher, cipher.name, tv[0], tv[1])

# C, unrolled
imp.generate_implementation(cipher, f"files/{cipher.name}_unrolled.c", "c", True)
imp.test_implementation_c(cipher, f"{cipher.name}_unrolled", tv[0], tv[1])


# ---------------------------------------------------------------------------
# Example 2: generate a figure
# ---------------------------------------------------------------------------
cipher = speck.SPECK_PERMUTATION(r=2, version=32)   # 2 rounds for a compact figure
vis.generate_figure(cipher, f"files/{cipher.name}.pdf")


# ---------------------------------------------------------------------------
# Example 3: MILP-based search for differential trails
# ---------------------------------------------------------------------------
cipher = speck.SPECK_PERMUTATION(r=5, version=32)   # 5 rounds for a fast search
trails = attacks.diff_attacks(
    cipher,
    goal="DIFFERENTIALPATH_PROB",        # default: best differential trail (max probability)
    constraints=["INPUT_NOT_ZERO"],      # default: remove the trivial all-zero trail
    objective_target="OPTIMAL",          # default: minimize the trail weight
    config_model=None,                   # default: MILP model
    config_solver=None,                  # default: MILP solver (Gurobi)
    show_mode=0,                         # default: print the first and last round of the trail
)


# ---------------------------------------------------------------------------
# Example 4: SAT-based search for differential trails
# ---------------------------------------------------------------------------
cipher = speck.SPECK_PERMUTATION(r=5, version=32)   # 5 rounds for a fast search
trails = attacks.diff_attacks(
    cipher,
    goal="DIFFERENTIALPATH_PROB",        # default: best differential trail (max probability)
    constraints=["INPUT_NOT_ZERO"],      # default: remove the trivial all-zero trail
    objective_target="OPTIMAL",          # default: minimize the trail weight
    config_model={"model_type": "sat"},  # switch to a SAT model
    config_solver=None,                  # default: SAT solver via PySAT
    show_mode=0,                         # default: print the first and last round of the trail
)


# ---------------------------------------------------------------------------
# Example 5: MILP-based search for linear trails
# ---------------------------------------------------------------------------
cipher = speck.SPECK_PERMUTATION(r=5, version=32)   # 5 rounds for a fast search
trails = attacks.linear_attacks(
    cipher,
    goal="LINEARPATH_CORR",              # default: best linear trail (max correlation)
    constraints=["INPUT_NOT_ZERO"],      # default: remove the trivial all-zero trail
    objective_target="OPTIMAL",          # default: minimize the trail weight
    config_model=None,                   # default: MILP model
    config_solver=None,                  # default: MILP solver (Gurobi)
    show_mode=0,                         # default: print the first and last round of the trail
)


# ---------------------------------------------------------------------------
# Example 6: SAT-based search for linear trails
# ---------------------------------------------------------------------------
cipher = speck.SPECK_PERMUTATION(r=5, version=32)   # 5 rounds for a fast search
trails = attacks.linear_attacks(
    cipher,
    goal="LINEARPATH_CORR",              # default: best linear trail (max correlation)
    constraints=["INPUT_NOT_ZERO"],      # default: remove the trivial all-zero trail
    objective_target="OPTIMAL",          # default: minimize the trail weight
    config_model={"model_type": "sat"},  # switch to a SAT model
    config_solver=None,                  # default: SAT solver via PySAT
    show_mode=0,                         # default: print the first and last round of the trail
)
