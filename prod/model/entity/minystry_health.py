from prod.model.entity.polyclinic import Polyclinic


class MinystryHealth:
    DEFAULT_SIZE = 100

    def __init__(self, size=DEFAULT_SIZE):
        self._ls = []
        if size > 0:
            self._size = size
        else:
            self._size = Polyclinics.DEFAULT_SIZE

    @property
    def size(self):
        return self._size

    def __len__(self):
        return len(self._ls)

    def add(self, polyclinic):
        if isinstance(polyclinic, Polyclinic):
            self._ls.append(polyclinic)

    def __getitem__(self, index):
        if isinstance(index, int) and 0 <= index < len(self):
            return self._ls[index]
        else:
            raise Exception()

    def __setitem__(self, index, value):
        if isinstance(index, int) and 0 <= index < len(self):
            self._ls[index] = value
        else:
            raise Exception()

    def __delitem__(self, index):
        if isinstance(index, int) and 0 <= index < len(self):
            del self._ls[index]
        else:
            raise Exception()

    def __str__(self):
        if not self._ls:
            return f"Polyclinic doesn't work.It has {self._size} "
        else:
            msg = "Polyclinic list:\n"
            for polyclinic in self._ls:
                msg += str(polyclinic) + "\n"
            msg += f"There are {self._size - len(self)} visitors."
            return msg





