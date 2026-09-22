from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    words = ingredients.lower().replace(",", " ").split()
    allowed = light_spell_allowed_ingredients()
    if any(word in allowed for word in words):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
