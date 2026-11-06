from q5_sorting_plants_by_rarity import TreeNode, sort_plants


def test_returns_plants_in_ascending_rarity_order():
    collection = TreeNode(
        3, "Monstera",
        TreeNode(1, "Pothos", None, TreeNode(2, "Spider Plant")),
        TreeNode(5, "Witchcraft Orchid", TreeNode(4, "Hoya Motoskei")),
    )

    assert sort_plants(collection) == [
        (1, "Pothos"),
        (2, "Spider Plant"),
        (3, "Monstera"),
        (4, "Hoya Motoskei"),
        (5, "Witchcraft Orchid"),
    ]


def test_empty_collection():
    assert sort_plants(None) == []


def test_single_plant():
    assert sort_plants(TreeNode(2, "Fern")) == [(2, "Fern")]
