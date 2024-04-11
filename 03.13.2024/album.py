def makeAlbum(artist,album,song):
    album = {
        "Artist": artist,
        "Album": album,
    }
    if song:
        album['Song'] = song
    return album

i=1
while(i<=3):
    singer = input("Enter artist name: ");
    albumname = input("Enter the album name: ")
    songname = input("Enter the Songname: ")
    print(f" These are your Album details: {makeAlbum(singer,albumname,songname)}")
    i+=1
    
print("Thank You")