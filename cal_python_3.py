import pylab as pl
a,b,n = 0,pl.pi/2,100
fn = lambda x : pl.sin(3*x)*pl.sin(3*x)*pl.cos(3*x)
xs,h = pl.linspace(a,b,n+1,retstep = True)
ys = pl.sin(3*xs)*pl.sin(3*xs)*pl.cos(3*xs)
rsum , lsum , usum , tsum = 0,0,0,0
y1 = ys[0]
for y2 in ys[1:]:
	rsum+=y1
	if y1<y2:
		lsum+=y1
		rsum+=y2
	else:
		lsum+=y2
		rsum+=y1
	tsum+=y1+y2
	y1=y2
isum = h*sum([ys[0],4*sum(ys[1:-1:2]),2*sum(ys[2:-1:2]),ys[-1]])/3
print(isum)	