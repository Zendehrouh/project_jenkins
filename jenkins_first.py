
#import json

class ClassName():
    """make a class with two input ."""

    def __init__(self, user, cred):
        #super(, self).__init__()
        self.user = user
        self.cred = cred

    def toJsonFile(self):
        f = {"cred" : self.cred, "user" : self.user}
        #json_file = json.dumps(f)
        return print("json file is:", f)
