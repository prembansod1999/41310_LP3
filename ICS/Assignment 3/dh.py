from random import randint
if __name__ == '__main__':
	# A prime number P is taken
	P = 11
	# G is a primitve root for P
	G = 2
	print('The Value of P is :%d'%(P))
	print('The Value of G is :%d'%(G))
	# Alice private key a
	a = 8
	print('The Private Key a for Alice is :%d'%(a))
	# Alice generated key(public Key)
	x = int(pow(G,a,P))
	# Bob private key b
	b = 4
	print('The Private Key b for Bob is :%d'%(b))
	# Bob generated key(public Key)
	y = int(pow(G,b,P))
	# Secret key for Alice
	ka = int(pow(y,a,P))
	# Secret key for Bob
	kb = int(pow(x,b,P))
	print('Secret key for the Alice is : %d'%(ka))
	print('Secret Key for the Bob is : %d'%(kb))
