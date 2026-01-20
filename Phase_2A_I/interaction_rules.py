ALLOWED_INTERACTIONS = {
    "VectorCarrier": {"ScalarCarrier"},
    "MatrixCarrier": {"VectorCarrier"},
    "Point": {"VectorCarrier"},
}


def assert_interaction_allowed(source, target):
    source_type = type(source).__name__
    target_type = type(target).__name__

    allowed = ALLOWED_INTERACTIONS.get(source_type, set())

    if target_type not in allowed:
        raise PermissionError(
            f"Interaction not allowed: {source_type} -> {target_type}"
        )
