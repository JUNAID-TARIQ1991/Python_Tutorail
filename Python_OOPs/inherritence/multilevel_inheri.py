class InvaidOperationError(Exception):
    pass


class stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise IndentationError("Stram is alredy open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise IndentationError("Stram is alredy close")
        self.opened = False


class FileStream(stream):
    def read(self):
        print("Reading data from file")


class NetworkStream(stream):
    def read(self):
        print("Reading data from network")


file1 = stream
file1.open
