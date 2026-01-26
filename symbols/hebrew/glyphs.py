"""
Hebrew Glyph Declarations — Phase 2B-I

Glyphs are declared as inert shapes only.
"""

HEBREW_GLYPHS = {
    "ALEPH": {
        "id": "HEB_ALEPH",
        "stroke_count": 3,
        "stroke_types": {"line", "angle"},
        "symmetry": "none",
        "orientation": "fixed",
        "attachment_faces": {"top", "bottom"},
        "closedness": "open",
        "interior_space": "none",
        "planarity": "2D",
    },

    "BET": {
        "id": "HEB_BET",
        "stroke_count": 3,
        "stroke_types": {"line", "angle"},
        "symmetry": "none",
        "orientation": "fixed",
        "attachment_faces": {"left"},
        "closedness": "partial",
        "interior_space": "bounded",
        "planarity": "2D",
    },
}
