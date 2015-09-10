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
