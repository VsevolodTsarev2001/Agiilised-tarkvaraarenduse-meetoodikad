print ("hello world!")
logs=[]

def liitumine(a,b):
    logs.append('liitumine')
    if isinstance(a,str) or isinstance(b,str):
        print("Vale andmed")
        return ""
    return a+b

def korrutamine(a,b):
    logs.append('korrutamine')
    if isinstance(a,str) or isinstance(b,str):
        print("Vale andmed")
        return ""
    return a*b
def lahutamine(a,b):
    logs.append('lahutamine')
    if isinstance(a,str) or isinstance(b,str):
        print("Vale andmed")
        return ""
    return a-b

def jagamine(a,b):
    try:
        logs.append('jagamine')
        if isinstance(a,str) or isinstance(b,str):
            print("Vale andmed")
            return ""
        return a/b
    except ZeroDivisionError:
        print("Ei saa jagada nullile")

def logsKuuvamine(logs):
    jag = 0
    korr = 0
    liit = 0
    lahut = 0
    for elem in logs:
        if elem == 'korrutamine':
            korr += 1
        elif elem == 'jagamine':
            jag += 1
        elif elem == 'liitumine':
            liit += 1
        elif elem == 'lahutamine':
            lahut += 1
    return [jag,korr,liit,lahut]

print(jagamine(5,0))
print(korrutamine(5,5))
print(liitumine(5,5))
print(logsKuuvamine(logs))