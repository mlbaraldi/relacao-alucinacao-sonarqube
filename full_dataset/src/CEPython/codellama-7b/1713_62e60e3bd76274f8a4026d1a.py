

def from_raw_values(cls, values):
    bookmarks = []
    for value in values:
        bookmarks.append(Bookmark(value))
    return bookmarks
