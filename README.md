# Lookup 🔍

Custom Hash table implementation in Python 🐍 just  for fun, but also to understand a little deeper the different types of implementations that can be done for
resizing and collision handling 🤖 Who knows, perhaps I will end up implementing a basic cache system which can be deployed in a cloud provider! lets see 🤷

In the future I would also like to implement it in Golang as an excuse to start learning the language 🚀

All the coding sessions will be recorded live 🎥 and uploaded to [nicodes](https://www.youtube.com/channel/UCKGZLR6ETz-Z3e1hzkuy2Ig)

### Initial Resources
- https://en.wikipedia.org/wiki/Hash_function
- https://en.wikipedia.org/wiki/Hash_table
- **Collision handling - open addressing**
    - https://github.com/aliaamohamedali/Algorithms/blob/master/introduction-to-algorithms-3rd-edition.pdf (Chapter 11 Hash tables)
    - https://courses.csail.mit.edu/6.006/fall11/lectures/lecture10.pdf
    - https://webdocs.cs.ualberta.ca/~holte/T26/open-addr.html
    - https://en.m.wikipedia.org/wiki/Linear_probing
    - https://en.m.wikipedia.org/wiki/Quadratic_probing
    - https://en.m.wikipedia.org/wiki/Double_hashing

### Tests
- Run unit tests: `pytest`
- Run stress test: `python main.py`



### TODO
- Improve resize logic
- How does it handle concurrency?
- Turn in to cache?
- Make a Go version 