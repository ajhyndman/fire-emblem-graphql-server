from aiodataloader import DataLoader

from src.request import requestApiRows


RARITY_KEYS = {
    1: "ONE_STAR",
    2: "TWO_STAR",
    3: "THREE_STAR",
    4: "FOUR_STAR",
    5: "FIVE_STAR",
}


async def batch_get_base_stats(keys):
    # Fetch base stats for all heroes and then filter by provided keys.
    # This isn't ideal, but when trying to filter by hero hames in the
    # "allHeroes" case, the query string generated exceeded max URL size!
    rows = await requestApiRows(
        {
            "action": "cargoquery",
            "tables": ",".join(["Heroes", "HeroBaseStats"]),
            "fields": ",".join(
                [
                    "Heroes._pageName=Name",
                    "HP",
                    "Atk",
                    "Spd",
                    "Def",
                    "Res",
                    "HeroBaseStats.Rarity",
                    "HeroBaseStats.Variation",
                ]
            ),
            "join_on": "HeroBaseStats._pageName=Heroes._pageName",
            "where": 'HeroBaseStats.Variation IN ("Neut")',
        }
    )

    base_stats_by_key = []

    for key in keys:
        base_stats = {
            RARITY_KEYS[int(row["Rarity"])]: {
                "HP": row["HP"],
                "ATK": row["Atk"],
                "SPD": row["Spd"],
                "DEF": row["Def"],
                "RES": row["Res"],
            }
            for row in rows
            if row["Name"] == key
        }

        base_stats_by_key.append(base_stats)

    return base_stats_by_key


class BaseStatsLoader(DataLoader):
    async def batch_load_fn(self, keys):  # pylint: disable=E0202
        return await batch_get_base_stats(keys)
