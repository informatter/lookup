# Lookup 🔍

Custom Hash table implementation in Python 🐍 just  for fun, but also to understand a little deeper the different types of implementations that can be done for
resizing and collision handling 🤖 Who knows, perhaps I will end up implementing a basic cache system which can be deployed in a cloud provider! lets see 🤷

In the future I would also like to implement it in Golang as an excuse to start learning the language 🚀

All the coding sessions will be recorded live 🎥 and uploaded to [nicodes](https://www.youtube.com/channel/UCKGZLR6ETz-Z3e1hzkuy2Ig)

## Initial Resources 📖
- https://en.wikipedia.org/wiki/Hash_function
- https://en.wikipedia.org/wiki/Hash_table
- **Collision handling - open addressing**
    - https://github.com/aliaamohamedali/Algorithms/blob/master/introduction-to-algorithms-3rd-edition.pdf (Chapter 11 Hash tables)
    - https://courses.csail.mit.edu/6.006/fall11/lectures/lecture10.pdf
    - https://webdocs.cs.ualberta.ca/~holte/T26/open-addr.html
    - https://en.m.wikipedia.org/wiki/Linear_probing
    - https://en.m.wikipedia.org/wiki/Quadratic_probing
    - https://en.m.wikipedia.org/wiki/Double_hashing


## Install dependencies

The only dependency used is **pytest**

`pip install -r requirements.txt`

## Tests 🧪

**Activate virtual environment**

Windows 🪟

`env/scripts/activate.ps1`

macOS 🍎 / Linux 🐧

`source env/bin/activate`

**Run tests**


To run all unit tests: 
- `pytest` to include print statements : `pytest -s`

To run a specific test:
- `pytest tests/test_lookup.py::test_resize_up`

Stress test: 
- `python main.py`



## TODO
- Turn in to cache?
- API?
- CLI client?
- How does it handle concurrency?
- Make a Go version 