class Pet:
    
    def __init__(self, kind, legs) -> None:
        self._kind = kind
        self._legs = legs

    @property
    def kind(self):
        return self._kind
    
    @kind.setter
    def kind(self, kind : str):
        if kind and "str" in str(type(kind)):
            self._kind == kind
        else:
            raise Exception("Pet.kind must be a non-empty string")

    @property
    def legs(self):
        return self._legs
    
    @legs.setter
    def legs(self, legs : int):
        if legs and "int" in str(type(legs)):
            self._legs == legs
        else:
            raise Exception("Pet.legs must be an integer")

    def start(self):
        print(f"{self.kind} is running")

    def stop(self):
        print("Pet stopped")

cat = Pet("Cat", 4)
fish = Pet("Fish", 0)

# print(type("String"))

cat.legs = 10