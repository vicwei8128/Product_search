import cv2
import numpy as np
from matplotlib import pyplot as plt
import csv

import pandas as pd

# from matplotlib import pyplot as plt
df = pd.read_csv("data.csv")
# plt.plot(data.x, data.y, 'o') #將a、b所繪製的圖表更改顯示方式
# #plt.legend(["b","c"]) #標示ab、ac的圖示
# plt.show() #執行

data = open('data.csv', 'r', newline='', encoding="utf-8-sig")
reader = csv.DictReader(data)
# final_list = list(reader)
#product
# for row in reader:
#     print(row)
pxy_mat = [[row['product'], row['x'], row['y']] for row in reader]
print('xy', pxy_mat)

gc = cv2.imread('./image/plan.jpg', 1)

i = str(input('請輸入要找的商品'))
j = ['商品', '肥皂']
if i in j:
    m = [150, 150]
    print(type(m))
    cv2.circle(gc, tuple(m), 10, (255, 255, 0), -1)
    cv2.imshow('draw', gc)
else:
    print('沒有此商品')
    # cv2.imshow('plan', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
