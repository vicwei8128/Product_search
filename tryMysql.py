import pymysql
import cv2

connection = pymysql.connect(host='localhost',
                             database='create_carrefour_table',
                             user='root',
                             password='5985593')

mycursor = connection.cursor()


# insert_commit = "INSERT INTO city VALUES(%s, %s)"
# data = ('103', 'hisnchu')
# mycursor.execute(insert_commit, data)
# connection.commit()
# sql_1 = "SELECT * FROM EMP"
# mycursor.execute(sql_1)


def get_staff_info_one():
    while True:
        name = input("請輸入商品類別:")
        if name == "": break
        sql_2 = "SELECT X , Y FROM carrefour_4 WHERE 類別 ='" + name + "'"
        mycursor.execute(sql_2)
        # print(sql_2)
        staff_data = mycursor.fetchone()
        if (staff_data == None):
            print("查無此商品".format(name))
            continue

        for x in staff_data:
            print(x, type(x))

        ans = [x for x in staff_data]
        print(ans)

        if name in sql_2:
            gc = cv2.imread('./image/plan.jpg', 1)
            cv2.circle(gc, tuple(ans), 5, (0, 10, 255), -1)
            cv2.imshow('draw', gc)
        else:
            print('沒有此商品')
            # cv2.imshow('plan', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        return staff_data


# myresult = mycursor.fetchall()

get_staff_info_one()
#
# for x in myresult:
#     print(x)

