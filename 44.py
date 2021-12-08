import pyautogui as pg
import time
pg.click('4.png')
pg.click()
pg.locateCenterOnScreen('4.png')
#tx=pg.locateCenterOnScreen('4.png')
#print(tx)

# 获取鼠标位置
def get_mouse_positon():
 time.sleep(2) # 准备时间
print('开始获取鼠标位置')
try:
 for i in range(2):
 
  x, y = pg.position()
  positionStr = '鼠标坐标点（X,Y）为：{},{}'.format(str(x).rjust(4), str(y).rjust(4))
  pix = pg.screenshot().getpixel((x, y)) # 获取鼠标所在屏幕点的RGB颜色
  positionStr += ' RGB:(' + str(pix[0]).rjust(3) + ',' + str(pix[1]).rjust(3) + ',' + str(pix[2]).rjust(
3) + ')'
  print(positionStr)
  time.sleep(0.2) # 停顿时间
  h=str(x).rjust(4)
  j=str(y).rjust(4)
  #print(j)
except:
 print('获取鼠标位置失败')
# if __name__ == "__main__":
   #return h, j

t=get_mouse_positon()
print(h)
if(int(h)==1790):print('x')
 


