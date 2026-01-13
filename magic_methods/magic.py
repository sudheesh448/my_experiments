import time

class Playlist:
    def __init__(self,songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

    def __str__(self):
        return f"This playlist has {len(self.songs)} tracks."

    def __getitem__(self, index):
        return self.songs[index]

    def __contains__(self, song_name):
        # This allows: "Imagine" in my_hits
        return song_name in self.songs


my_hits = Playlist(["Bohemian Rhapsody", "Stairway to Heaven", "Imagine"])

print(len(my_hits))
print(my_hits)
print(my_hits[1])
print("Imagine" in my_hits)


class Timer:
    def __enter__(self):
        self.start = time.time()
        print("Timer started...")
        return self

    def __exit__(self,exc_type,exc_val,exc_tb):
        self.end = time.time()

        print(f"Timer stopped. Duration: {self.end - self.start:.2f} seconds")

timer = Timer()
with Timer():
    time.sleep(1.5)



data_store = {
    "id": 101, 
    "name": "Sudheesh", 
    "job": "Developer", 
    "country": "India"
}


class SmartDictionary:
    def __init__(self,data):
        self.__dict__['data'] = data

    def __getattr__(self,name):
        if name in self.data:
            return self.data[name]
        return  "Not found"
    def __setattr__(self,name,value):
        print(f"Adding {name} to the dictionary...")
        self.data[name] = value

user = SmartDictionary({"id":101})
user.email = "sudheesh@example.com"
print(user.email)