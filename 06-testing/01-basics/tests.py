from intervals import overlapping_intervals


def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert not overlapping_intervals((2, 5), (7, 10))
    assert overlapping_intervals((7, 10), (1, 27))
    assert not overlapping_intervals((0, 4), (4,0))
    assert not overlapping_intervals((4, 0), (0, 4))