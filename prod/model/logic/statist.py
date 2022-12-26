from prod.model.entity import *

class Statistic:
    coefficient_normal = 0.031
    low = []
    high = []

    @staticmethod
    def workload(self,value):
        value = Polyclinic.specialist / Polyclinic.patient
        if workload >= 0.031:
            low.append(Polyclinic.number,Statistic.workload(value))
        else:
            high.append(Polyclinic.number,Statistic.workload(value))

        return sorted(low)
        return sorted(high)


