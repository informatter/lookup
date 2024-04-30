from lookup import Lookup


if __name__ == "__main__":
    
    lookup  = Lookup(length=5)

    lookup.insert(5,"a")
    print(lookup.buckets)
    assert lookup.size == 1

    lookup.insert(4,"a")
    print(lookup.buckets)
    assert lookup.size == 2

    lookup.insert(10,"a")   
    print(lookup.buckets)
    assert lookup.size == 3

    lookup.insert(11,"a")   
    print(lookup.buckets)
    assert lookup.size == 4

    lookup.insert(3,"a")   
    print(lookup.buckets)
    assert lookup.size == 5

    lookup.insert(0,"a")   
    print(lookup.buckets)
    assert lookup.size == 5

    r = lookup.search(5)
    assert r != None

    r = lookup.search(25)
    assert r is None

    r = lookup.delete(25)
    assert r is False

    r = lookup.delete(10)
    assert r is True
    print(lookup.buckets)
    r = lookup.search(3)
    assert r != None


