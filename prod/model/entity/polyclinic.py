class Polyclinic:
    def __init__(self, number, specialist, patient,):
        self._number = number
        self._specialist = specialist
        self._patient = patient

    @property
    def workload(self):
        return self._specialist / self._patient

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    @number.deleter
    def number(self):
        del self._number

    @property
    def specialist(self):
        return self._specialist

    @specialist.setter
    def specialist(self, specialist):
        if specialist > 0:
            self._specialist = specialist
        else:
            raise Exception()

    @specialist.deleter
    def specialist(self):
        del self._specialist

    @property
    def patient(self):
        return self._patient

    @patient.setter
    def patient(self, patient):
        if patient > 0:
            self._patient = patient
        else:
            raise Exception()

    @patient.deleter
    def patient(self):
        del self._patient

    def __str__(self):
        return (f"number = {self._number}"
                f"specialist = {self._specialist}"
                f"patient = {self._patient}")
