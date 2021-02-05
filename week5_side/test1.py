class nisit:
    def __init__(self,name,sesname,year,de,sex,form):
        self.name = name 
        self.year =year
        self.de = de #department=สาขาวิชา
        self.sex = sex
        self.form = form
    
    def introduce(self):
        print("--------Introduce myself---------")
        print("name:",self.name)
        print("year:")
        print("department:",self.de)
        print("sex:",self.sex)
        print("school from:",self.form)

C=nisit("chadchalidh","insenla","1","computer ed.","male","keannakhon witayalai")
C.introduce()