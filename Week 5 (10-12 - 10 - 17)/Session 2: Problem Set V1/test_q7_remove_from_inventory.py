from q7_remove_from_inventory import Node, delete_item


def test_delete_item_removes_first_match():
    slingshot = Node("Slingshot")
    peaches = Node("Peaches")
    beetle = Node("Scarab Beetle")
    slingshot.next = peaches
    peaches.next = beetle

    result = delete_item(slingshot, "Peaches")

    assert result.value == "Slingshot"
    assert result.next.value == "Scarab Beetle"


def test_delete_item_missing_value_leaves_list_unchanged():
    slingshot = Node("Slingshot")
    peaches = Node("Peaches")
    slingshot.next = peaches

    result = delete_item(slingshot, "Triceratops Torso")

    assert result.value == "Slingshot"
    assert result.next.value == "Peaches"
