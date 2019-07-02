class Person():
    def __init__(self,name , age):
        self.name = name
        self.age = age
    @classmethod
    def older(cls, origin1, origin2):
        if origin1.age > origin2.age:
            return(origin1)
        else:
            return(origin2)
