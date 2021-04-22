
import json

class ClassName():
    """make a class with two input ."""

    def __init__(self, user, cred):
        #super(, self).__init__()
        self.user = user
        self.cred = cred

    def to_jsonFile()
        f = {"cred" : cred, "user" : user}
        json_file = json.dumps(f)
        print(json_file)
