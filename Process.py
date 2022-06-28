class Process:
    def __init__(self, properties):
        for property in properties.items():
            setattr(self,property[0],property[1])

    def __repr__(self):
        return f"Process {self.id}"