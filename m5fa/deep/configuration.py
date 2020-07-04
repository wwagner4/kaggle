from pathlib import Path
import helpers as hlp

subsets = [
    ('mini', ["FOODS_1_001", "HOBBIES_1_021", "HOUSEHOLD_2_491"]),
    ('medium', ['HOBBIES_2_135', 'HOBBIES_2_136', 'HOBBIES_2_137', 'HOBBIES_2_138', 'HOBBIES_2_139', 'HOBBIES_2_140',
                'HOBBIES_2_141', 'HOBBIES_2_142', 'HOBBIES_2_143', 'HOBBIES_2_144', 'HOBBIES_2_145', 'HOBBIES_2_146',
                'HOBBIES_2_147', 'HOBBIES_2_148', 'HOBBIES_2_149', 'HOUSEHOLD_1_001', 'HOUSEHOLD_1_002',
                'HOUSEHOLD_1_003',
                'HOUSEHOLD_1_004', 'HOUSEHOLD_1_005', 'HOUSEHOLD_1_006', 'HOUSEHOLD_1_007', 'HOUSEHOLD_1_008',
                'HOUSEHOLD_1_009',
                'HOUSEHOLD_1_010', 'HOUSEHOLD_1_011', 'HOUSEHOLD_1_012', 'HOUSEHOLD_1_013', 'HOUSEHOLD_1_014',
                'HOUSEHOLD_1_015',
                'HOUSEHOLD_1_016', 'HOUSEHOLD_1_017', 'HOUSEHOLD_1_018', 'HOUSEHOLD_1_019', 'HOUSEHOLD_1_020',
                'HOUSEHOLD_1_021',
                'HOUSEHOLD_1_022',
                ]),
    ('large', ['FOODS_3_811', 'FOODS_3_812', 'FOODS_3_813', 'FOODS_3_814',
               'FOODS_3_815', 'FOODS_3_816', 'FOODS_3_817', 'FOODS_3_818',
               'FOODS_3_819', 'FOODS_3_820', 'FOODS_3_821', 'FOODS_3_822',
               'FOODS_3_823', 'FOODS_3_824', 'FOODS_3_825', 'FOODS_3_826',
               'FOODS_3_827',
               'HOBBIES_1_001', 'HOBBIES_1_002', 'HOBBIES_1_003', 'HOBBIES_1_004',
               'HOBBIES_1_005', 'HOBBIES_1_006', 'HOBBIES_1_007', 'HOBBIES_1_008',
               'HOBBIES_1_009', 'HOBBIES_1_010', 'HOBBIES_1_011', 'HOBBIES_1_012',
               'HOBBIES_1_013', 'HOBBIES_1_014', 'HOBBIES_1_015', 'HOBBIES_1_016',
               'HOBBIES_1_017', 'HOBBIES_1_018', 'HOBBIES_1_019', 'HOBBIES_1_020',
               'HOBBIES_1_021', 'HOBBIES_1_022', 'HOBBIES_1_023', 'HOBBIES_1_024',
               'HOBBIES_1_025', 'HOBBIES_1_026', 'HOBBIES_1_027', 'HOBBIES_1_028',
               'HOBBIES_1_029', 'HOBBIES_1_030', 'HOBBIES_1_031', 'HOBBIES_1_032',
               'HOBBIES_1_033', 'HOBBIES_1_034', 'HOBBIES_1_035', 'HOBBIES_1_036',
               'HOBBIES_1_037', 'HOBBIES_1_038', 'HOBBIES_1_039', 'HOBBIES_1_040',
               'HOBBIES_1_041', 'HOBBIES_1_042', 'HOBBIES_1_043',
               ]),
]


def create_fnam(subs_nam: str) -> str:
    return f"sp5_02_{subs_nam}"


def create_trained_model_path(subs_nam: str) -> Path:
    return Path(hlp.get_datadir()) / f"tfm_{subs_nam}"
