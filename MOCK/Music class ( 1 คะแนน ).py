class Song :
    def __init__(self, name, genre, durations):
        self.name = name
        self.genre = genre
        self.durations = durations

    def show_info(self) :
        time = self.durations // 60
        time = str(time) + "." + f"{(self.durations % 60):02d}"
        return f"{self.name} <|> {self.genre} <|> {time}"

Rickroll = Song(input(), input(), int(input()))
print(Rickroll.show_info())