# https://leetcode.com/problems/letter-tile-possibilities/

def depthFirst(st, prefix, tiles):
    t = tiles
    p = prefix

    if prefix not in st:
        if prefix:
            st.add(prefix)
        for i in range(len(tiles)):
            ti = tiles[:i]
            ti_1 = tiles[i+1:]
            tii = ti+ti_1
            depthFirst(st, prefix + tiles[i], tiles[:i] + tiles[i+1:])
            print(prefix, " ", tii)

def letterTile(tile):
    s = set()
    depthFirst(s, "", tile)
    print(s)
    return len(s)

print(letterTile("abc"))
