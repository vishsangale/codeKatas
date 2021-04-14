import json
import pytest


class SearchByTag:
    def __init__(self, data_file, query_tag):
        with open(data_file) as data_file:
            self._data = json.load(data_file)
        self.query = query_tag
        self.first_val = None

    def search(self):
        self.first_val = None
        if not self._data or len(self._data) == 0 or len(self._data["items"]) == 0:
            return

        for items in self._data.values():
            for item in items:
                if "tags" in item:
                    for tag in item["tags"]:
                        if self.query == tag:
                            if not self.first_val:
                                self.first_val = item
                            yield item
        if not self.first_val:
            return

    def first(self):
        return self.first_val


def test_class():
    filename = "katas/pindrop/sample.json"
    s = SearchByTag(filename, "crime")
    l = 0
    for i in s.search():
        l += 1
    assert l == 3
    assert {"name": "The Godfather", "tags": ["70s", "drama", "crime"]} == s.first()
    data = s.search()
    assert {"name": "The Godfather", "tags": ["70s", "drama", "crime"]} == next(data)
    assert {"name": "The Dark Knight", "tags": ["action", "crime", "drama"]} == next(
        data
    )
    assert {
        "name": "The Godfather: Part II",
        "tags": ["70s", "crime", "drama"],
    } == next(data)

    s = SearchByTag(filename, "crimes")
    l = 0
    for i in s.search():
        l += 1
    assert l == 0
    assert None == s.first()

    filename = "katas/pindrop/empty_array.json"
    with pytest.raises(StopIteration):
        s = SearchByTag(filename, "crime")

        next(s.search())

    filename = "katas/pindrop/without_tags.json"
    s = SearchByTag(filename, "crime")
    with pytest.raises(StopIteration):

        next(s.search())
