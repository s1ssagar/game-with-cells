n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
if n % 2 == 0 and m % 2 == 0:
    print ((n/2)*(m/2))
if n % 2 == 0 and m % 2 == 1:
    print (((n/2) * ((m-1)/2)) + (n/2))
if n % 2 == 1 and m % 2 == 0:
    print (((m/2) * ((n-1)/2)) + (m/2))
if n % 2 == 1 and m % 2 == 1:
    print (((n+1)/2) * ((m+1)/2))