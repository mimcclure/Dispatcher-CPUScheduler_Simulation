class CPU:
    def __init__(self, properties):
        for property in properties.items():
            setattr(self,property[0],property[1])