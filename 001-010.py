
#001: Multiples of 3 and 5
def project001():
    sum=0
    for i in range(1000):
        if i%3==0 or i%5==0:
            sum+=i
    return sum

#002: Even Fibonacci numbers
def project002():
    x1=1
    x2=1
    sum=0
    while True:
        y=x1+x2
        if y>4000000:
            break
        if y%2==0:
            sum+=y
        x2=x1
        x1=y
    return sum

#003: Largest prime factor
def project003():
    g=600851475143
    g1=600851475143
    i=1
    primfactors=[]
    g_bool=False
    while True:
        if g_bool==True:
            break
        while True:
            i+=1
            if i==g:
                if g==g1:
                    #print g,"ist primzahl"
                    g_bool=True
                else:
                    #print g,"ist groesster primfaktor"
                    primfactors.append(g)
                    g_bool=True
                break
            if g%i==0:
                g=g/i
                primfactors.append(i)
                i=1
                break
    return max(primfactors)

#004: Largest palindrome product
def project004():
    ymax=0
    imax=0
    jmax=0
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            y=i*j
            helpi=True
            for k in range(len(str(y))//2):
                if str(y)[k]!=str(y)[-(k+1)]:
                    helpi=False
                    break
            if helpi==True and y>ymax:
                ymax=y
                imax=i
                jmax=j
    y=str(ymax)+"="+str(imax)+"*"+str(jmax)
    return y

#005: Smallest multiple
def project005():
    j=1
    while True:
        #print j
        bool_x=True
        for i in range(1,21,1):
            #print i
            if j%i!=0:
                bool_x=False
                break
        if bool_x==True:
            break
        else:
            j+=1
    return j

#006: Sum square difference
def project006():
    sumofsquares=0
    squareofsum=0
    for i in range(1,101,1):
        sumofsquares+=i**2
        squareofsum+=i
    return (squareofsum**2)-sumofsquares

#007: 10001st prime
def project007(g):
    g1=g
    i=1
    primfactors=[]
    g_bool=False
    pnbr=0
    while True:
        if g_bool==True:
            break
        while True:
            i+=1
            if i==g:
                if g==g1:
                    #print g,"ist primzahl"
                    g_bool=True
                    pnbr=1
                else:
                    #print g,"ist groesster primfaktor"
                    primfactors.append(g)
                    g_bool=True
                break
            if g%i==0:
                g=g/i
                primfactors.append(i)
                i=1
                break
    if len(primfactors)==0:
        return 1
    else:
        return 0


def project007b():
    prmnbr=0
    i=2
    while True:
        prmnbr+=project007(i)
        if prmnbr==10001:
            break
        i+=1
    return i

#008: Largest product in a series
def project008():
    onekarray="" \
            "73167176531330624919225119674426574742355349194934" \
            "96983520312774506326239578318016984801869478851843" \
            "85861560789112949495459501737958331952853208805511" \
            "12540698747158523863050715693290963295227443043557" \
            "66896648950445244523161731856403098711121722383113" \
            "62229893423380308135336276614282806444486645238749" \
            "30358907296290491560440772390713810515859307960866" \
            "70172427121883998797908792274921901699720888093776" \
            "65727333001053367881220235421809751254540594752243" \
            "52584907711670556013604839586446706324415722155397" \
            "53697817977846174064955149290862569321978468622482" \
            "83972241375657056057490261407972968652414535100474" \
            "82166370484403199890008895243450658541227588666881" \
            "16427171479924442928230863465674813919123162824586" \
            "17866458359124566529476545682848912883142607690042" \
            "24219022671055626321111109370544217506941658960408" \
            "07198403850962455444362981230987879927244284909188" \
            "84580156166097919133875499200524063689912560717606" \
            "05886116467109405077541002256983155200055935729725" \
            "71636269561882670428252483600823257530420752963450" \

    maxreiheprodukt=0
    for i in range(len(onekarray)-12):
        reiheprodukt=1
        for j in range(0,13,1):
            reiheprodukt*=int(onekarray[i+j])
        if reiheprodukt>maxreiheprodukt:
            maxreiheprodukt=reiheprodukt
    return maxreiheprodukt

#009: Special Pythagorean triplet
import math
def project009():
    #a<b<c and a+b+c=1000; amax=333; bmax=499
    for a in range(1,334,1):
        for b in range(a+1,500,1):
            c=1000-a-b
            v_bool=c==math.sqrt(a**2+b**2)
            if v_bool==True:
                return a*b*c

#010: Summation of primes
def project010():
    n=2000001
    #create a list of primes < n
    #credit to Robert William Hanks for providing such a
    # fast way for returning primes in a list
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    primelist=[2] + [i for i in xrange(3,n,2) if sieve[i]]
    #return sum of all primes < n
    primesum=0
    for i in range(len(primelist)):
        primesum+=primelist[i]
    return primesum

#Print Loesungen

print project001()
"""
print project002()
print project003()
print project004()
print project005() #Achtung ausfuehrung dauert ewig!!!
print project006()
print project007b() #Achtung ausfuehrung dauert ewig(ca 1min30s)!!!
print project008()
print project009()
print project010()
"""