"""
Glyph Schema — Phase 2B-I

Defines the allowed static fields for all inert glyph substrates.
No additional fields are permitted.
"""

ALLOWED_GLYPH_FIELDS = {
    "id",
    "stroke_count",
    "stroke_types",
    "symmetry",
    "orientation",
    "attachment_faces",
    "closedness",
    "interior_space",
    "planarity",
}
