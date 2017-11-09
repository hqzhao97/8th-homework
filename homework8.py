import pylab as pl 
import time
from math import *

starttime=time.time()

def run():
	c_x.append(x0)
	c_y.append(y0)
	c_vx.append(vx0)
	c_vy.append(vy0)
	c_t.append(0)
	n=0
	for i in range (100000):
		c_x.append(c_x[i]+c_vx[i]*timestep)
		c_y.append(c_y[i]+c_vy[i]*timestep)
		c_vx.append(c_vx[i])
		c_vy.append(c_vy[i])
		c_t.append((i+1)*timestep)

		if c_x[-1]>1.0 or c_x[-1]<-1.0:
			c_vx[-1]=-c_vx[-1]
		if c_y[-1]>1.0 or c_y[-1]<-1.0:
			c_vy[-1]=-c_vy[-1]
		if (c_x[-1]-circle_cx)**2+(c_y[-1]-circle_cy)**2<=circle_r**2 and n>5:
			vt=c_vx[-1]*(c_x[-1]-circle_cx)/circle_r+c_vy[-1]*(c_y[-1]-circle_cy)/circle_r
			vtx=vt*(c_x[-1]-circle_cx)/circle_r
			vty=vt*(c_y[-1]-circle_cy)/circle_r
			vnx=c_vx[-1]-vtx
			vny=c_vy[-1]-vty
			vtx=-vtx
			vty=-vty
			c_vx[-1]=vtx+vnx
			c_vy[-1]=vty+vny
			n=0
		n=n+1
	return 0

c_x=[]
c_y=[]
c_vx=[]
c_vy=[]
c_t=[]


timestep=0.001
x0=0.8
y0=0.0
vx0=1.34
vy0=1.0
circle_cx=0.1
circle_cy=0.1
circle_r=0.5

circle_a=0.5
circle_b=0.5

if circle_a==circle_b:
	circle_r=circle_a

	run()
	pl.figure(figsize=(20,20))
	pl.scatter(x0,y0,color='blue')
	pl.scatter(c_x,c_y,s=1,color='red')
	pl.xlim(-1.2,1.2)
	pl.ylim(-1.2,1,2)

	pl.plot([1,-1,-1,1,1],[1,1,-1,-1,1],color='black')

	circle_x=[]
	circle_y=[]
	for i in range (510):
		circle_x.append(circle_r*math.cos(i*math.pi/250)+circle_cx)
		circle_y.append(circle_r*math.sin(i*math.pi/250)+circle_cy)
	pl.plot(circle_x,circle_y,color='black')
	pl.legend()

	pl.show()