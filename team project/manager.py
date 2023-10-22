import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

start_time = ''
end_time = ''


def manager():
    global start_time
    global end_time
    start = input("Please enter a start_time using Y-m-d H:M:S style")
    end = input("Please enter a ending_time using Y-m-d H:M:S style")
    start_time = parse_time(start)
    end_time = parse_time(end)
    print(start_time)
    print(end_time)

    return start_time, end_time


def all_vehicle_status():
    con = sqlite3.connect("User_Vehicle.db")
    cur = con.cursor()

    # two pie charts including two different types

    # cur.execute(
    #     "select vehicle_status,count(vehicle_id) "
    #     "from vehicle where vehicle_type = 0 "
    #     "group by vehicle_status"
    #     "order by vehicle_status")
    # status_num = cur.fetchall()
    # print(status_num)

    # pie_1
    # running bike
    # running_bike = "SELECT * FROM vehicle where vehicle_type = 0 and vehicle_status = 1"
    # cur.execute(running_bike)
    # run_bike = cur.fetchall()
    # run_bike_num = len(run_bike)
    # # print(run_bike_num)
    #
    # # static bike
    # static_bike = "SELECT * FROM vehicle where vehicle_type = 0 and vehicle_status = 0"
    # cur.execute(static_bike)
    # # sta_bike_num = cur.fetchone()[0]
    # sta_bike = cur.fetchall()
    # sta_bike_num = len(sta_bike)
    # # print(sta_bike_num)
    #
    # # sta_bike [][]
    # # [vehicle_id, vehicle_type,battery]
    # # [vehicle_id, vehicle_type,battery]
    #
    # # bike need repaired
    # repaired_bike = "SELECT * FROM vehicle where vehicle_type = 0 and vehicle_status = 2"
    # cur.execute(repaired_bike)
    # repair_bike = cur.fetchall()
    # repair_bike_num = len(repair_bike)
    # # print(repair_bike_num)

    sql = f'select vehicle_type, vehicle_status, count(v.vehicle_id) ' \
          f'from Vehicles v join Orders O on v.vehicle_id = O.vehicle_id ' \
          f'where vehicle_start_time >= {start_time} and vehicle_end_time <= {end_time} ' \
          f'group by vehicle_type, vehicle_status'

    cur.execute(sql)
    res = cur.fetchall()
    print(res)

    run_bike_num, sta_bike_num, repair_bike_num = 0, 0, 0
    run_scooter_num, sta_scooter_num, repair_scooter_num = 0, 0, 0

    for row in res:
        vehicle_type = row[0]
        vehicle_status = row[1]
        total = row[2]

        if vehicle_type == 'bike':
            if vehicle_status == 0:
                sta_bike_num = total
            elif vehicle_status == 1:
                run_bike_num = total
            else:
                repair_bike_num = total
        else:
            if vehicle_status == 0:
                sta_scooter_num = total
            elif vehicle_status == 1:
                run_scooter_num = total
            else:
                repair_scooter_num = total

    sum1 = sta_bike_num + run_bike_num + repair_bike_num
    sum2 = sta_scooter_num + run_scooter_num + repair_scooter_num

    if sum1 != 0:
        labels = ['running', 'static', 'repaired']
        colors = ['green', 'yellow', 'red']
        values = [run_bike_num, sta_bike_num, repair_bike_num]
        plt.title("The Status of Bike")
        explode = [0.3, 0, 0]
        plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', explode=explode)
        plt.show()

    # pie_2
    # 运行的滑板车
    # running_scooter = 'SELECT * FROM vehicle where vehicle_type = 1 and vehicle_status = 1'
    # cur.execute(running_scooter)
    # run_scooter = cur.fetchall()
    # run_scooter_num = len(run_scooter)
    #
    # # 静止的滑板车
    # static_scooter = 'SELECT * FROM vehicle where vehicle_type = 1 and vehicle_status = 0'
    # cur.execute(static_scooter)
    # sta_scooter = cur.fetchall()
    # sta_scooter_num = len(sta_scooter)
    #
    # # 待维修的滑板车
    # repaired_scooter = 'SELECT * FROM vehicle where vehicle_type = 1 and vehicle_status = 2'
    # cur.execute(repaired_scooter)
    # repair_scooter = cur.fetchall()
    # repair_scooter_num = len(repair_scooter)

    if sum2 != 0:
        values = [run_scooter_num, sta_scooter_num, repair_scooter_num]
        # print(run_scooter_num, sta_scooter_num, repair_scooter_num)
        labels = ['running', 'static', 'repaired']
        colors = ['green', 'yellow', 'red']
        plt.title("The Status of Scooter")
        plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%')
        plt.show()

    cur.close()
    con.close()


def usage_in_selected_time():
    con = sqlite3.connect("User_Vehicle.db")
    cur = con.cursor()

    # 生成一个柱状图或折线图
    # 横坐标是类型， 纵坐标是数量
    # xAxis is Type, yAxis is amount of using

    running_bike = "SELECT * from Vehicles v join Orders O on v.vehicle_id = O.vehicle_id where vehicle_type = 'bike' and vehicle_start_time > {} and vehicle_end_time < {}".format(
        start_time, end_time)
    cur.execute(running_bike)
    run_bike = cur.fetchall()
    run_bike_num = len(run_bike)
    print(run_bike_num)

    running_scooter = "SELECT * from Vehicles v join Orders O on v.vehicle_id = O.vehicle_id where vehicle_type = 'scooter' and vehicle_start_time > {} and vehicle_end_time < {}".format(
        start_time, end_time)
    cur.execute(running_scooter)
    run_scooter = cur.fetchall()
    run_scooter_num = len(run_scooter)
    print(run_bike_num)

    index = ["bike", "scooter"]
    values = [run_bike_num, run_scooter_num]
    plt.title("The Amount of vehicle in using")
    plt.legend(index, loc=2)
    plt.xlabel('Type of vehicle', color='black')
    plt.ylabel('Amount of using vehicle', color='black')

    plt.bar(index, values)
    plt.show()

    cur.close()
    con.close()


def total_and_avg_hour():
    # 生成一个柱状图
    # 骑行总时长和平均时长
    con = sqlite3.connect("User_Vehicle.db")
    cur = con.cursor()
    # start_time = input("please input ")
    print('select:', start_time, end_time)

    sql = f'select vehicle_type, avg(vehicle_end_time - vehicle_start_time), sum(vehicle_end_time - vehicle_start_time) ' \
          f'from Orders O join Vehicles v on v.vehicle_id = O.vehicle_id ' \
          f'where vehicle_start_time >= {start_time} and vehicle_end_time <= {end_time} ' \
          f'group by vehicle_type'
    print(sql)
    cur.execute(sql)
    res = cur.fetchall()
    bike_avg_time = 1
    bike_sum_time = 1
    scooter_avg_time = 1
    scooter_sum_time = 1
    for row in res:
        if row[0] == 'bike':
            bike_avg_time = row[1]
            bike_sum_time = row[2]
        elif row[0] == 'scooter':
            scooter_avg_time = row[1]
            scooter_sum_time = row[2]

    # res = cur.fetchall()[0]
    # avg_time, sum_time = res
    print(res)

    # print(avg_time, ' ', sum_time)

    # cur.execute('SELECT vehical_start_time FROM Orders')
    # start = cur.fetchall()
    # print(start)
    #
    # cur.execute('SELECT vehical_end_time FROM Orders')
    # end = cur.fetchall()
    # print(end)
    #
    # cur.execute('SELECT vehical_start_time, vehical_end_time FROM Orders')
    # time_all = cur.fetchall()
    # print(time_all)
    #
    # sum_time = 0
    # for i in start:
    #     for j in end:
    #         if start_time < start[i] and end_time > end[j]:
    #             sum_time = (end[j] - start[i]) + sum_time
    #             count = count + 1
    #
    #         elif start_time > start[i] and end_time > end[j]:
    #             sum_time = (end[j] - start_time) + sum_time
    #             count = count + 1
    #
    #         elif start_time < start[i] and end_time < end[j]:
    #             sum_time = (end_time - start[i]) + sum_time
    #             count = count + 1
    #
    # mean_time = sum_time / count

    index = ["total_time", "average_time"]
    values = [bike_sum_time, bike_avg_time]
    plt.title("The total time and average time of bike")
    plt.legend(index, loc=2)
    plt.ylabel('Time', color='black')
    plt.bar(index, values, color='y')
    plt.show()

    index = ["total_time", "average_time"]
    values = [scooter_sum_time, scooter_avg_time]
    plt.title("The total time and average time of scooter")
    plt.legend(index, loc=2)
    plt.ylabel('Time', color='black')
    plt.bar(index, values, color='y')
    plt.show()


    cur.close()
    con.close()


def parse_time(str_time):
    return int(datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S').timestamp())
    pass


def main():
    manager()
    all_vehicle_status()
    usage_in_selected_time()
    total_and_avg_hour()

# if __name__ == '__main__':
#     main()
