import pytest
from main import creating_folfer, deleting_folder


def test_creating_folder():
    folder = creating_folfer()
    assert folder[0] == 201 and folder[1] == 200
    deleting_folder()


fixture = [400, 401, 403, 404, 406, 409, 413, 423, 429, 503, 507]


@pytest.mark.parametrize('a', fixture)
def test_creating_folder_(a):
    folder = creating_folfer()
    assert folder[0] != a
    deleting_folder()
