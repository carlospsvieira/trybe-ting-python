import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    pq = PriorityQueue()
    pq.enqueue({"qtd_linhas": 4})
    pq.enqueue({"qtd_linhas": 7})
    pq.enqueue({"qtd_linhas": 2})
    pq.enqueue({"qtd_linhas": 9})
    pq.enqueue({"qtd_linhas": 5})
    pq.enqueue({"qtd_linhas": 3})

    assert len(pq) == 6

    values = [2, 3, 4, 5, 7, 9]
    for value in values:
        item = pq.dequeue()
        assert item is not None
        assert item["qtd_linhas"] == value

    with pytest.raises(IndexError):
        pq.dequeue()
