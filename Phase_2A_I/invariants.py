STRUCTURAL_INVARIANTS = {
    "cardinality",
    "containment",
    "composition",
    "reference",
    "phase_ordering",
}
CARDINALITY_RULES = {
    "ScalarCarrier": {
        "min": 0,
        "max": None,
    },
    "VectorCarrier": {
        "min": 1,
        "max": None,
    },
    "MatrixCarrier": {
        "min": 1,
        "max": None,
    },
    "Point": {
        "min": 1,
        "max": None,
    },
}
CONTAINMENT_RULES = {
    "VectorCarrier": {"ScalarCarrier"},
    "MatrixCarrier": {"VectorCarrier"},
}
COMPOSITION_RULES = {
    "disallow_mixed_carriers": True,
    "require_homogeneous_containment": True,
}
REFERENCE_RULES = {
    "allow_self_reference": False,
    "allow_forward_reference": False,
    "allow_cross_phase_reference": False,
}

PHASE_ORDERING_RULES = {
    "PHASE_2A_I": {
        "forbidden": {
            "symbols",
            "tokens",
            "recursion",
            "environments",
            "evaluation",
        }
    }
}
def invariants_declared():
    return True
