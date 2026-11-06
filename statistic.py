
class Stat:
    def __init__(self, old_snapshot: dict, new_snaphot: dict): 
        self.old = old_snapshot,
        self.new = new_snaphot

    def find_deleted_file(self):
        return self.old.keys() - self.new.keys()

    def find_new_file(self):
        return self.new.keys() - self.old.keys()

    def comparison(self):
        difference = 0
        for file in self.old.keys() & self.new.keys():
            difference += self.new[file] - self.old[file]

        return difference - self.find_deleted_file + self.find_new_file