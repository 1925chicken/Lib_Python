MAX,MOD = 200001,1000000007

fac,finv,inv = [0] * MAX,[0] * MAX,[0] * MAX
def COMinit():
    fac[0],fac[1] = 1,1
    finv[0],finv[1] = 1,1
    inv[1] = 1
    for i in range(2,MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

def COM(n,k):
    if(n < k):
        return 0
    if(n < 0 or k < 0):
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD