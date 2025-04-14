class Task:
    def __init__(self,titile,status="to-do"):
        self.title = titile
        self.status = status

    def mark_done(self):
        self.status = "done"