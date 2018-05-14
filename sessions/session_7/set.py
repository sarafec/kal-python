song_library = [("Phantom of the Opera", "Sara Brightman"), ("Captain Nemo", "Sara Brightman"), ("November Rain", "Guns N' Roses")]
print(song_library)
song_library.sort()
print(song_library)

artists = set()
for song, artist in song_library:
	artists.add(artist)

print(artists)