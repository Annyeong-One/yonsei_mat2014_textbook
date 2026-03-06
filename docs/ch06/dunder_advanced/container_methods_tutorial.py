"""
Example 4: Container Magic Methods
Demonstrates: __len__, __getitem__, __setitem__, __delitem__, __contains__, __iter__
"""


class Playlist:
    """A custom playlist container."""
    
    def __init__(self, name):
        self.name = name
        self.songs = []
    
    def __repr__(self):
        return f"Playlist('{self.name}', {len(self.songs)} songs)"
    
    def __len__(self):
        """Return the number of songs in the playlist."""
        return len(self.songs)
    
    def __getitem__(self, index):
        """Get a song by index or slice."""
        return self.songs[index]
    
    def __setitem__(self, index, value):
        """Set a song at a specific index."""
        self.songs[index] = value
    
    def __delitem__(self, index):
        """Delete a song at a specific index."""
        del self.songs[index]
    
    def __contains__(self, song):
        """Check if a song is in the playlist."""
        return song in self.songs
    
    def __iter__(self):
        """Make the playlist iterable."""
        return iter(self.songs)
    
    def add_song(self, song):
        """Add a song to the playlist."""
        self.songs.append(song)


class CustomDict:
    """A custom dictionary-like class."""
    
    def __init__(self):
        self._data = {}
    
    def __repr__(self):
        return f"CustomDict({self._data})"
    
    def __len__(self):
        """Return number of items."""
        return len(self._data)
    
    def __getitem__(self, key):
        """Get value by key."""
        if key not in self._data:
            raise KeyError(f"Key '{key}' not found")
        return self._data[key]
    
    def __setitem__(self, key, value):
        """Set value by key."""
        print(f"Setting {key} = {value}")
        self._data[key] = value
    
    def __delitem__(self, key):
        """Delete item by key."""
        if key not in self._data:
            raise KeyError(f"Key '{key}' not found")
        del self._data[key]
    
    def __contains__(self, key):
        """Check if key exists."""
        return key in self._data
    
    def __iter__(self):
        """Iterate over keys."""
        return iter(self._data)


class Matrix:
    """A simple 2D matrix class."""
    
    def __init__(self, rows, cols, default=0):
        self.rows = rows
        self.cols = cols
        self._data = [[default for _ in range(cols)] for _ in range(rows)]
    
    def __repr__(self):
        return f"Matrix({self.rows}x{self.cols})"
    
    def __str__(self):
        """Pretty print the matrix."""
        lines = []
        for row in self._data:
            lines.append(" ".join(f"{val:6}" for val in row))
        return "\n".join(lines)
    
    def __getitem__(self, index):
        """Get item by [row, col] or [row]."""
        if isinstance(index, tuple):
            row, col = index
            return self._data[row][col]
        else:
            return self._data[index]
    
    def __setitem__(self, index, value):
        """Set item by [row, col] or [row]."""
        if isinstance(index, tuple):
            row, col = index
            self._data[row][col] = value
        else:
            self._data[index] = value
    
    def __len__(self):
        """Return number of rows."""
        return self.rows


# Examples
if __name__ == "__main__":

    # ============================================================================
    print("=== Playlist Examples ===")
    playlist = Playlist("My Favorites")
    
    # Add songs
    playlist.add_song("Song A")
    playlist.add_song("Song B")
    playlist.add_song("Song C")
    playlist.add_song("Song D")
    
    print(f"Playlist: {playlist}")
    print(f"Length: {len(playlist)}")
    
    # Access by index
    print(f"\nFirst song: {playlist[0]}")
    print(f"Last song: {playlist[-1]}")
    
    # Slicing
    print(f"First two songs: {playlist[0:2]}")
    
    # Modify
    playlist[1] = "Song B (Remix)"
    print(f"Modified second song: {playlist[1]}")
    
    # Check membership
    print(f"\n'Song A' in playlist: {'Song A' in playlist}")
    print(f"'Song Z' in playlist: {'Song Z' in playlist}")
    
    # Iterate
    print("\nAll songs:")
    for i, song in enumerate(playlist, 1):
        print(f"  {i}. {song}")
    
    # Delete
    del playlist[2]
    print(f"\nAfter deleting index 2: {len(playlist)} songs")
    for song in playlist:
        print(f"  - {song}")
    
    print("\n\n=== CustomDict Examples ===")
    cd = CustomDict()
    
    # Set items
    cd["name"] = "Alice"
    cd["age"] = 30
    cd["city"] = "New York"
    
    print(f"\nCustomDict: {cd}")
    print(f"Length: {len(cd)}")
    
    # Get items
    print(f"\nName: {cd['name']}")
    print(f"Age: {cd['age']}")
    
    # Check membership
    print(f"\n'name' in cd: {'name' in cd}")
    print(f"'country' in cd: {'country' in cd}")
    
    # Iterate
    print("\nAll keys:")
    for key in cd:
        print(f"  {key}: {cd[key]}")
    
    # Delete
    del cd["age"]
    print(f"\nAfter deleting 'age': {cd}")
    
    print("\n\n=== Matrix Examples ===")
    matrix = Matrix(3, 3, default=0)
    
    print(f"Matrix: {matrix}")
    print(f"Length (rows): {len(matrix)}")
    
    # Set values
    matrix[0, 0] = 1
    matrix[1, 1] = 5
    matrix[2, 2] = 9
    matrix[0, 2] = 3
    
    print("\nMatrix after setting values:")
    print(matrix)
    
    # Get values
    print(f"\nValue at [1, 1]: {matrix[1, 1]}")
    print(f"First row: {matrix[0]}")
    
    # Set entire row
    matrix[1] = [2, 4, 6]
    print("\nMatrix after setting row 1:")
    print(matrix)
