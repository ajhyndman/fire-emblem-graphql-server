from promise import Promise
from promise.dataloader import DataLoader

from src.request import requestApiQuery


def batch_get_heroes():
    rows = requestApiQuery({
        'action': 'cargoquery',
        'tables': ','.join([
            'Heroes',
            'HeroBaseStats',
            'HeroGrowths',
        ]),
        'fields': ','.join([
            'Heroes._pageName=FullName',
            'Name',
            'Title',
            'Origin',
            'WeaponType',
            'MoveType',
            'SummonRarities',
            'RewardRarities',
            'ReleaseDate',
            'PoolDate',
            'HeroGrowths.HP',
            'HeroGrowths.Atk',
            'HeroGrowths.Spd',
            'HeroGrowths.Def',
            'HeroGrowths.Res',
        ]),
        'group_by': 'Heroes._pageName',
        'join_on': ','.join([
            'HeroBaseStats._pageName = Heroes._pageName',
            'Heroes._pageName = HeroGrowths._pageName',
        ]),
    })

    heroes = [{'name': row['Name'], 'title': row['Title'], 'weaponType': row['WeaponType']} for row in rows]

    return heroes


class HeroesLoader(DataLoader):
    def batch_load_fn(self, keys):
        return batch_get_heroes()
