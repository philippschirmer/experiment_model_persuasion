
def test_first_attempt():
    yield MyPage
    yield pages.Survey, dict(name="Bob", age=20)
