from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    words = ingredients.lower().replace(",", " ").split()
    allowed = dark_spell_allowed_ingredients()
    if any(word in allowed for word in words):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
