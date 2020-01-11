from abc import ABC

class DBObject:
    _uid = 0 
    def get_uid(self):
        DBObject._uid += 1
        return DBObject._uid
        