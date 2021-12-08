import pyautogui as pg
import time
l=1
pg.click(1000,20)

#x,y=pg.locateCenterOnScreen('c.png')
#print(x)

#print tx[6:10]
def xx():
  
   for x,y,z,n in pg.locateAllOnScreen('10.png'):
     
     print(x)
     
     time.sleep(1)
     if x==1645:
       print('f')
       pg.click('10.png')
       pg.click('10.png')
       time.sleep(40)
       pg.press('s')
       time.sleep(1)
       for i in range(20):
         time.sleep(1)
         pg.press('c')
         pg.press('v')
       pg.press('s')
       time.sleep(1)
       pg.press('s')
       time.sleep(1)
 
       for i in range(40):
         time.sleep(1)
         pg.press('c')
         pg.press('v')
       pg.press('s')
       time.sleep(1)
       pg.press('s')
       time.sleep(1)
       for i in range(20):
         time.sleep(1)
         pg.press('c')
         pg.press('v')
       
      
   for q,w,e,r in pg.locateAllOnScreen('55.png'):
     
     print(q)
     time.sleep(1)
     if q==1193:
       print('h')
       pg.press('d')
       time.sleep(2)
       pg.press('d')
       time.sleep(2)
       pg.press('d')
       time.sleep(2)
       pg.press('g')
       time.sleep(3)
       pg.press('f')
       time.sleep(3)
       pg.press('f')
       
    


#pinrt(hx)
while True:
    xx()
