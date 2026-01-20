from .algebraic_state import ALGEBRAIC_STATE, STATE_DECLARATION
from .registries import RESERVED_SYMBOL_DOMAINS


def run_phase_2A_I_audit():
    if STATE_DECLARATION != "EMPTY":
        raise AssertionError("Algebraic state is not empty")

    if ALGEBRAIC_STATE:
        raise AssertionError("Algebraic state has been populated")

    for domain, value in RESERVED_SYMBOL_DOMAINS.items():
        if value is not None:
            raise AssertionError(
                f"Reserved domain '{domain}' has been populated"
            )
