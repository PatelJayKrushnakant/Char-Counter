string=input("Enter Whatever You Want")
a={}
countchar=0
def abc(string):
    string=string.lower()
    x=97
    i=0
    while i<26:
        countchar=string.count(chr(x))
        if countchar > 0:
            a[chr(x)]=countchar
        i=i+1
        countchar=0
        x=x+1
        sortedDict= sorted(a, key=a.get, reverse=True)
    for items in sortedDict:
        print(items,"=",a[items])
abc(string)
