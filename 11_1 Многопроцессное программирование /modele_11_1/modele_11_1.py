from datetime import datetime
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, encoding= "utf-8") as  file:
        while True:
            line = file.readline().strip()
            if not line:
                break
            all_data.append(line)

filenames = [f'./file {number}.txt' for number in range(1, 5)]
# time_start = datetime.now()
# for i in filenames:
#     read_info(i)
# and_time = datetime.now()
# result_time = and_time - time_start
# print(result_time,"(линейный)")

if __name__ == '__main__':
    time_start = datetime.now()
    with Pool() as p:
        r = p.map(read_info, filenames)

    and_time = datetime.now()
    result_time = and_time - time_start
    print(result_time,'(многопроцессный)')

