from lookup import Lookup


if __name__ == "__main__":
    
    lookup  = Lookup()

    lookup.insert("foo",55)
    assert lookup.size == 1

    lookup.insert("foo",65)
    assert lookup.size == 1

    delete_result = lookup.delete("foo")
    assert lookup.size == 0
    assert delete_result is True

    delete_result = lookup.delete("foo")
    assert delete_result is False

    get_result = lookup.get("foo")
    assert get_result is None

    lookup.insert("foo",55)
    lookup.insert("faa",55)
    assert lookup.size == 2
    get_result = lookup.get("faa")
    assert get_result is not None

