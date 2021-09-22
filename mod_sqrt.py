def quadratic_residue(a:int,p:int):
	if pow(a,(p - 1) // 2,p) == 1:
		return 1
	return -1

def calc(_h:int,p:int,b:int,cnt:int):
	s = 1
	h = pow(_h,-1,p)
	for i in (cnt - 2,-1,-1):
		e = pow(2,i,p)
		if pow(b,e,p) == p - 1:
			s *= h
			s %= p
			b *= pow(h,2)
			b %= p
		h = pow(h,2,p)
	return s

def mod_sqrt (a:int,p:int):
	if quadratic_residue(a,p) == -1:
		print("No answer")
		exit()
	g = 0
	for i in range(2,10000000):
		if (quadratic_residue(i,p) + p) == p - 1:
			g = i
			break
	t = p - 1
	cnt = 0
	while t & 1 == 0:
		cnt += 1
		t >>= 1
	h = pow(g,t,p)
	b = pow(a,t,p)
	#print(pow(a,(t + 1) //2,p))
	#print(calc(h,p,b,cnt))
	return (pow(a,(t + 1) // 2,p) * calc(h,p,b,cnt)) % p

