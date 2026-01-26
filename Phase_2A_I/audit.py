from .invariants import invariants_declared
from .algebraic_state import ALGEBRAIC_STATE, STATE_DECLARATION
from .registries import RESERVED_SYMBOL_DOMAINS
from symbols.schema import ALLOWED_GLYPH_FIELDS


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
            if not invariants_declared():
        raise AssertionError("Structural invariants not declared")
def audit_glyph_inertness(glyph_sets):
    for glyphs in glyph_sets:
        for name, glyph in glyphs.items():
            illegal = set(glyph.keys()) - ALLOWED_GLYPH_FIELDS
            if illegal:
                raise AssertionError(
                    f"Glyph {name} declares illegal fields: {illegal}"
                )
