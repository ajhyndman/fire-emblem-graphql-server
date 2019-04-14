from ariadne import EnumType


move_type = EnumType(
    "MoveType",
    {
        "ARMORED": "Armored",
        "CAVALRY": "Cavalry",
        "FLYING": "Flying",
        "INFANTRY": "Infantry",
    },
)
