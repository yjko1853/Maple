
from input_data import *
import numpy as np
from sklearn.model_selection import train_test_split
from knn import Knn
# x = np.array([0,1,2,3,4])
# y = x * 2 + 1
file = load_xls('./data/maple.xlsx')
start_date = get_single_column(file, 'sheet1', 'B2', 'B35')
forsythia_flowering = get_single_column(file, 'sheet6', 'D2', 'D35')
for i in range(len(start_date)):
    # TODO:날짜 파싱
    start_date[i] = (int(start_date[i].strftime("%Y%m%d")[4:6])-10)*31 + int(start_date[i].strftime("%Y%m%d")[6:])
    forsythia_flowering[i] = (int(forsythia_flowering[i].strftime("%Y%m%d")[4:6])-3)*31 + int(forsythia_flowering[i].strftime("%Y%m%d")[6:])
    # start_date[i] = float(start_date[i].strftime("%Y%m%d")[6:])
min_temper = get_single_column(file, 'sheet2', 'D14', 'D408')
max_temper = get_single_column(file, 'sheet2', 'E14', 'E408')
rain_weight = get_single_column(file, 'sheet3', 'B2', 'B35')
# rain_time = get_single_column(file, 'sheet3', 'C2', 'C35')
for i in range(393, -1, -1):
    if 0 <= i % 12 < 5 or 10 <= i % 12:
        del (min_temper[i])
        del (max_temper[i])
        # del (rain_weight[i])
np.array(min_temper[i]).astype(float)
np.array(max_temper[i]).astype(float)
x = []
for i in range(33):
    v = []
    for j in range(5):
        v.append(min_temper[i*5+j])
    for j in range(5):
        v.append(max_temper[i*5+j])
    v.append(rain_weight[i])
    v.append(forsythia_flowering[i])
    x.append(v)

x = np.array(x)
y = np.array(start_date)

# x = x / x.max()
# y = y / y.max()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.17, shuffle=True)
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, shuffle=True, random_state=1004)
# print('x_test : ', x_test)
# print('y_test : ', y_test)
# print('x_train : ', x_train)
# print('y_train : ', y_train)

train_size = len(y_train)
test_size = len(y_test)
print(train_size, test_size)

k1 = Knn(x_train, x_test, y_train, y_test)
k = 2
acc = 0
print(y)
for i in range(test_size):
    result = k1.neighbor(k, k1.distance(i))
    print(i, "th data result ", result, ", label ", y_test[i], sep='', end=' ')

    # print(result, "  label ", end=' ')
    # print(y_test[i], end=' ')
    #if result == y_test[i]:
    #    count = count + 1

    # acc += abs(result - y_test[i])
    acc += 1 - abs(result - y_test[i])/result
    print(", Accuracy : %.2f" % ((1-abs(result-y_test[i])/result)*100), "%", sep='')
print("\nTotal Accuracy : %.4f" % (acc/test_size*100), "%", sep='')
