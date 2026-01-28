# --- Interface / mediation nouns (inert) ---
"""
Major Icon Nouns — Phase 2B-I

These are inert noun substrates.
No subjecthood, objecthood, or behavior is defined here.
"""

ICON_NOUNS = {

    # --- Core structural nouns ---

    "STONE": {
        "id": "ICON_STONE",
        "faces": {"top", "bottom", "left", "right", "front", "back"},
        "symmetry": "none",
        "orientation": "fixed",
        "modularity": "block",
        "interior_space": "none",
        "stackable": True,
        "planarity": "3D",
    },

    "TERRACOTTA_BLOCK": {
        "id": "ICON_TERRACOTTA_BLOCK",
        "faces": {"top", "bottom", "left", "right", "front", "back"},
        "symmetry": "bilateral",
        "orientation": "fixed",
        "modularity": "unit",
        "interior_space": "none",
        "stackable": True,
        "planarity": "3D",
    },

    "SEAL": {
        "id": "ICON_SEAL",
        "faces": {"front", "back"},
        "symmetry": "radial",
        "orientation": "fixed",
        "modularity": "surface",
        "interior_space": "none",
        "stackable": False,
        "planarity": "2D",
    },

    # --- Container-like nouns (still inert) ---

    "JAR": {
        "id": "ICON_JAR",
        "faces": {"top", "bottom", "side"},
        "symmetry": "radial",
        "orientation": "fixed",
        "modularity": "unit",
        "interior_space": "bounded",
        "stackable": False,
        "planarity": "3D",
    },

    "ARK": {
        "id": "ICON_ARK",
        "faces": {"top", "bottom", "side", "interior"},
        "symmetry": "bilateral",
        "orientation": "fixed",
        "modularity": "composite",
        "interior_space": "bounded",
        "stackable": False,
        "planarity": "3D",
    },

    # --- Movement / linkage-shaped nouns (no motion yet) ---

    "WHEEL": {
        "id": "ICON_WHEEL",
        "faces": {"axial"},
        "symmetry": "radial",
        "orientation": "rotatable",
        "modularity": "unit",
        "interior_space": "bounded",
        "stackable": False,
        "planarity": "2D",
    },

    "CART": {
        "id": "ICON_CART",
        "faces": {"top", "bottom", "side"},
        "symmetry": "bilateral",
        "orientation": "fixed",
        "modularity": "composite",
        "interior_space": "bounded",
        "stackable": False,
        "planarity": "3D",
    },

    "BUS": {
        "id": "ICON_BUS",
        "faces": {"front", "back", "top", "bottom"},
        "symmetry": "bilateral",
        "orientation": "fixed",
        "modularity": "linear",
        "interior_space": "bounded",
        "stackable": False,
        "planarity": "3D",
    },

    # --- Vertical / stratification nouns ---

    "TOWER": {
        "id": "ICON_TOWER",
        "faces": {"top", "bottom", "side"},
        "symmetry": "radial",
        "orientation": "vertical",
        "modularity": "stack",
        "interior_space": "bounded",
        "stackable": True,
        "planarity": "3D",
    },

    # --- Registry / domain-like nouns (still inert) ---

    "GRID": {
        "id": "ICON_GRID",
        "faces": {"cell"},
        "symmetry": "orthogonal",
        "orientation": "fixed",
        "modularity": "matrix",
        "interior_space": "none",
        "stackable": False,
        "planarity": "2D",
    },

    "REGISTRY": {
        "id": "ICON_REGISTRY",
        "faces": {"cell", "boundary"},
        "symmetry": "orthogonal",
        "orientation": "fixed",
        "modularity": "matrix",
        "interior_space": "bounded",
        "stackable": False,
        "planarity": "2D",
    },
}
    "WORSHIPER": {
        "id": "ICON_WORSHIPER",
        "faces": {"front"},
        "symmetry": "bilateral",
        "orientation": "fixed",
        "modularity": "unit",
        "interior_space": "none",
        "stackable": False,
        "planarity": "2D",
    },

    "INTERFACE": {
        "id": "ICON_INTERFACE",
        "faces": {"front", "back"},
        "symmetry": "orthogonal",
        "orientation": "fixed",
        "modularity": "surface",
        "interior_space": "none",
        "stackable": False,
        "planarity": "2D",
    },

    "TERMINAL": {
        "id": "ICON_TERMINAL",
        "faces": {"front"},
        "symmetry": "orthogonal",
        "orientation": "fixed",
        "modularity": "endpoint",
        "interior_space": "none",
        "stackable": False,
        "planarity": "2D",
    },        "symmetry": "radial",
        "orientation": "fixed",
        "modularity": "surface",
        "interior_space": "none",
        "stackable": False,
        "planarity": "2D",
    },

    # --- Container-like nouns (still inert) ---

    "JAR": {
        "id": "ICON_JAR",
        "faces": {"top", "bottom", "side"},
        "symmetry": "radial",
        "orientation": "fixed",
        "modularity": "unit",
        "interior_space": "bounded",
        "stackable": False,
        "planarity": "3D",
    },

    "ARK": {
        "id": "ICON_ARK",
        "faces": {"top", "bottom", "side", "interior"},
        "symmetry": "bilateral",
        "orientation": "fixed",
        "modularity": "composite",
        "interior_space": "bounded",
        "stackable": False,
        "planarity": "3D",
    },

    # --- Movement / linkage-shaped nouns (no motion yet) ---

    "WHEEL": {
        "id": "ICON_WHEEL",
        "faces": {"axial"},
        "symmetry": "radial",
        "orientation": "rotatable",
        "modularity": "unit",
        "interior_space": "bounded",
        "stackable": False,
        "planarity": "2D",
    },

    "CART": {
        "id": "ICON_CART",
        "faces": {"top", "bottom", "side"},
        "symmetry": "bilateral",
        "orientation": "fixed",
        "modularity": "composite",
        "interior_space": "bounded",
        "stackable": False,
        "planarity": "3D",
    },

    "BUS": {
        "id": "ICON_BUS",
        "faces": {"front", "back", "top", "bottom"},
        "symmetry": "bilateral",
        "orientation": "fixed",
        "modularity": "linear",
        "interior_space": "bounded",
        "stackable": False,
        "planarity": "3D",
    },

    # --- Vertical / stratification nouns ---

    "TOWER": {
        "id": "ICON_TOWER",
        "faces": {"top", "bottom", "side"},
        "symmetry": "radial",
        "orientation": "vertical",
        "modularity": "stack",
        "interior_space": "bounded",
        "stackable": True,
        "planarity": "3D",
    },

    # --- Registry / domain-like nouns (still inert) ---

    "GRID": {
        "id": "ICON_GRID",
        "faces": {"cell"},
        "symmetry": "orthogonal",
        "orientation": "fixed",
        "modularity": "matrix",
        "interior_space": "none",
        "stackable": False,
        "planarity": "2D",
    },

    "REGISTRY": {
        "id": "ICON_REGISTRY",
        "faces": {"cell", "boundary"},
        "symmetry": "orthogonal",
        "orientation": "fixed",
        "modularity": "matrix",
        "interior_space": "bounded",
        "stackable": False,
        "planarity": "2D",
    },
}
