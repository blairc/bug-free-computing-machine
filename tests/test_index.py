import pathlib


def test_index_contains_header():
    html = (pathlib.Path(__file__).resolve().parent.parent / "index.html").read_text()
    assert "<h1>blairchristensen.com</h1>" in html

