import logging
from aiodataloader import DataLoader

from src.request import requestApiRows


async def batch_get_heroes(keys):
    rows = await requestApiRows(
        {
            "action": "cargoquery",
            "tables": ",".join(["Heroes", "HeroBaseStats", "HeroGrowths"]),
            "fields": ",".join(
                [
                    "Heroes._pageName=FullName",
                    "Name",
                    "Title",
                    "Origin",
                    "WeaponType",
                    "MoveType",
                    "SummonRarities",
                    "RewardRarities",
                    "ReleaseDate",
                    "PoolDate",
                    "HeroGrowths.HP",
                    "HeroGrowths.Atk",
                    "HeroGrowths.Spd",
                    "HeroGrowths.Def",
                    "HeroGrowths.Res",
                ]
            ),
            "group_by": "Heroes._pageName",
            "join_on": ",".join(
                [
                    "HeroBaseStats._pageName = Heroes._pageName",
                    "Heroes._pageName = HeroGrowths._pageName",
                ]
            ),
        }
    )

    heroes = [
        {"name": row["Name"], "title": row["Title"], "weaponType": row["WeaponType"]}
        for row in rows
    ]

    return [heroes]


class HeroesLoader(DataLoader):
    async def batch_load_fn(self, keys):  # pylint: disable=E0202
        return await batch_get_heroes(keys)
