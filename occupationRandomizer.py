f = open('occupations.csv', 'r')
s=f.read()
f.close()
s=s.split("\n")
s=s[1:len(s)-3]
d={}
for occupation in s:
    if occupation[0:1]== '"':
        occupation=occupation.split(',')
        while len(occupation)>2:
            occupation[0]=occupation[0]+','+occupation[1]
            occupation.pop(1)
    else:
        occupation=occupation.split(',')
    d[occupation[0]]=float(occupation[1])
print d

def pickRandom():
    
