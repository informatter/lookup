from lookup import Lookup

def test_deletion_when_table_is_empty():
    lookup  = Lookup(length=5)
    r = lookup.delete(7)
    assert r == False

def test_deletion_when_table_is_not_empty_and_probing_does_not_need_to_be_done():
    lookup  = Lookup(length=5)
    lookup.insert(5,"a")
    r = lookup.delete(5)
    assert r == True

    r = lookup.delete(5)
    assert r == False

    r = lookup.delete(7)
    assert r == False

def  test_deletion_when_table_is_not_empty_and_probing_needs_to_be_done():
    lookup  = Lookup(length=5)
    lookup.insert(5,"a")
    lookup.insert(11,"a")
    lookup.insert(10,"a")
    lookup.insert(4,"a")
    lookup.insert(3,"a")
    r = lookup.delete(3)
    assert r == True


def test_search_when_table_is_empty():
    lookup  = Lookup(length=5)
    r = lookup.search(3)
    assert r is None


def test_search_when_table_is_not_empty_and_probing_does_not_need_to_be_done():
    lookup  = Lookup(length=5)
    lookup.insert(5,"a")
    r = lookup.search(5)
    assert r is not None
    r = lookup.search(6)
    assert r is None

def test_search_when_table_is_not_empty_and_probing_needs_to_be_done():
    lookup  = Lookup(length=5)
    lookup.insert(5,"a")
    lookup.insert(11,"a")
    lookup.insert(10,"a")
    lookup.insert(4,"a")
    lookup.insert(3,"bb")

    r = lookup.search(3)
    assert r is not None
    assert r == "bb"


def test_insertion_when_resizing_is_not_needed():
    lookup  = Lookup(length=5)
    lookup.insert(5,"a")
    lookup.insert(11,"a")


def test_resize_up():
    lookup  = Lookup(length=5)
    lookup.insert(5,"a")
    assert lookup.get_size() == 1

    lookup.insert(4,"a")
    assert lookup.get_size() == 2

    lookup.insert(10,"a")   
    assert lookup.get_size() == 3

    lookup.insert(11,"a")   
    assert lookup.get_size() == 4
    assert lookup.length == 10

def test_resize_down():
    lookup  = Lookup(length=45)
    lookup.insert(5,"a")
    lookup.insert(4,"a")
    lookup.insert(10,"a")
    lookup.insert(11,"a") 
    lookup.insert(20,"a") 
    r = lookup.delete(5)
    assert r == True
    assert lookup.length == 45 // 2

def test_insertion():

    lookup  = Lookup(length=5)
    lookup.insert(5,"a")
    assert lookup.get_size() == 1

    lookup.insert(4,"a")
    assert lookup.get_size() == 2

    lookup.insert(10,"a")   
    assert lookup.get_size() == 3

    lookup.insert(11,"a")   
    assert lookup.get_size() == 4


def test_end_to_end():
    lookup  = Lookup(length=5)
    lookup.insert(5,"a")
    assert lookup.get_size() == 1

    lookup.insert(5,"b")
    assert lookup.get_size() == 1
    r = lookup.search(5)
    assert r is not None and r == "b"

    lookup.insert(4,"a")
    assert lookup.get_size() == 2

    lookup.insert(10,"a")   
    assert lookup.get_size() == 3

    lookup.insert(11,"a")   
    assert lookup.get_size() == 4


    lookup.insert(3,"a") 
    assert lookup.get_size() == 5
    
    lookup.insert(0,"a")   
    assert lookup.get_size() == 6

    r = lookup.search(5)
    assert r != None

    r = lookup.search(25)
    assert r is None

    r = lookup.delete(25)
    assert r is False

    r = lookup.delete(10)
    assert r is True
    r = lookup.search(3)
    assert r != None
