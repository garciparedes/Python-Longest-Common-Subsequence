
#!/usr/bin/env python

'''
Author: Sergio Garcia Prado
        www.garciparedes.me
'''

def max(a, b):
    return a if (a > b) else b


def lcs(X, Y, m, n):
    L = [[0 for col in range(n+1)] for row in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if (X[i-1] ==Y[j-1]):
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    #return L[m][n]
    index = L[m][n]
    lcs = list(" " * index)
    i = m
    j = n
    while(i > 0 and j > 0):
       if (X[i-1] == Y[j-1]):
           lcs[index-1] = X[i-1]
           i -= 1
           j -= 1
           index -= 1
       elif (L[i-1][j] > L[i][j-1]):
           i -= 1
       else:
           j -= 1

    return "".join(lcs)



def main():
    X = "ACCGGTGGACAATTCA";
    Y = "GGAAAGAGATATGCAC";

    m = len(X);
    n = len(Y);
    print "\n"

    print X
    print ""
    print Y
    print "\n"

    l = lcs( X, Y, m, n )

    print"LCS is %s and it length is %s" % (l, len(l) )
    print ""

if __name__ == "__main__":
    main()