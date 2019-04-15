from aiodataloader import DataLoader

from src.request import requestApiRows


async def batch_get_skills(keys):
    rows = await requestApiRows(
        {
            "action": "cargoquery",
            "tables": "Skills",
            "fields": ",".join(
                [
                    "WikiName",
                    "Description",
                    "SP",
                    "CanUseMove",
                    "CanUseWeapon",
                    "Exclusive",
                    "UseRange",
                    "Might",
                    "Scategory=Category",
                ]
            ),
        }
    )

    skills = []

    for key in keys:
        skill = next(row for row in rows if row["WikiName"] == key)

        skills.append({
            "name": skill["WikiName"],
            "effect": skill["Description"],
        })

    return skills


class SkillsLoader(DataLoader):
    async def batch_load_fn(self, keys):  # pylint: disable=E0202
        return await batch_get_skills(keys)

