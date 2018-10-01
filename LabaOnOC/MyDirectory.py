import os

class directory:

    def __init__(self, track):
        self.track = track

    def display_info(self):
        print("Вы указали путь: ", self.track)
        print(os.listdir("."), "\n")

        