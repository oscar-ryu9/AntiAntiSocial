def isTrue(s):
    return s == 'True'

class User:

    def __init__(self, csv):
        splitline = csv.split("%")
        self.id = splitline[1]
        self.name = splitline[0]
        self.passcode = splitline[2]
        self.major = splitline[3]
        self.interests = list(map(isTrue, splitline[4][1:-1].split(", ")))
        self.club = splitline[6]
        self.media = splitline[5][2:-2].split("', '")
        self.classes = list(map(int, splitline[7][1:-2].split(', ')))


    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_major(self):
        return self.major

    def get_interests(self):
        return self.interests

    def get_club(self):
        return self.club

    def get_media_account(self):
        return self.media

    def get_classes(self):
        return self.classes

    def find_mutual_friends(self):
        pass

    def print_user(self, type = "normal"):
        if type == "normal":
            print(self.name)
        else:
            print(self.id, end=", ")
            print(self.name, end=", ")
            print(self.major, end=", ")
            print(self.interests, end=", ")
            print(self.club, end=", ")
            print(self.media, end=", ")
            print(self.classes)












