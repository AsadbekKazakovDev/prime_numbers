def istub(n:int)->bool:
    if n<2:
        return False
    for i in range(2,int(n**(0.5))+1):
        if n%i==0:
            return False
    return True
def istub_n(a:int)->list:
    ans=[]
    for i in range(1,a+1):
        if istub(i):
            ans.append(i)
    return ans

def summa(n):
    return (sum(istub_n(a)))

a = int(input("A soni = "))

k = summa(a)
print(f"1 dan {a} gacha tub sonlar ruyhati :\n{istub_n(a)}\n")
print(f"1 dan {a} gacha tub sonlar yig`indisi = {k} ga teng...")