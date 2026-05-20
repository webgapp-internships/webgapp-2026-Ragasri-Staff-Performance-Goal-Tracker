class grade:
    def __init__(stud,name,mark):
        stud.name=name
        stud.mark=mark
    def show(stud):
        print("name : ",stud.name, "mark : ",stud.mark)
m1=grade("srii",99)
m2=grade("abi",98)
m3=grade("anu",89)
m1.show()
m2.show()
m3.show()            