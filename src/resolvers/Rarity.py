from ariadne import EnumType

rarity = EnumType(
    "Rarity",
    {"ONE_STAR": 1, "TWO_STAR": 2, "THREE_STAR": 3, "FOUR_STAR": 4, "FIVE_STAR": 5},
)
