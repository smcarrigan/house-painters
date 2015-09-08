class Painter(object):
    def __init__(self):
        self.job_class_name = "Apprentice"
        self.working_job = False
        self.health = 10
        self.terminated = False
        self.equipment = {'paintbrush' : 1,
                     '1-gallon-paint' : 1,
                     '5-gallon-paint' : 0,
                     'roller' : 0,
                     'sprayer' : 0,
                     'ladder' : 0,
                     'scaffolding' : 0 }


if __name__ == '__main__':
    painter1 = Painter()
    painter2 = Painter()
    painter1.working_job = True
    painter2.equipment['roller'] = 5
    print(painter1.equipment)
    print(painter2.equipment)
