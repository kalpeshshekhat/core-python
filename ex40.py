class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

jane_man = Song(["Mein yaha tu waha, yeh kaisi duriya"])

mere_saath_chal = Song(["Chal mere saath hi chal, Yeh meri jane jiger",
                         "Yeh zamana hai agar to zamane ko lekar chal"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

jane_man.sing_me_a_song()

mere_saath_chal.sing_me_a_song()
