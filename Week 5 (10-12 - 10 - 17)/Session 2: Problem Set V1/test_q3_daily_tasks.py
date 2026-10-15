from q3_daily_tasks import Node, add_first


def test_add_first_adds_new_head():
    task_1 = Node("shake tree")
    task_2 = Node("dig fossils")
    task_3 = Node("catch bugs")
    task_1.next = task_2
    task_2.next = task_3

    updated = add_first(task_1, "check turnip prices")

    assert updated.value == "check turnip prices"
    assert updated.next is task_1
    assert updated.next.next is task_2
