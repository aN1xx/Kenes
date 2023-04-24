"""
Transliterate Cyrillic → Latin in every possible way
"""

from .schemas import Schemas  # noqa: F403,F401

KAZ_TRANSLITERATION = Schemas.custom_kaz.value  # type: ignore
