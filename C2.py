import sys

class Time:
    def __init__(self, id, login_hour, login_minute, logout_hour, logout_minute):
        self.id = id
        self.login_hour = login_hour
        self.login_minute = login_minute
        self.logout_hour = logout_hour
        self.logout_minute = logout_minute
    def time_check(self):
        if self.logout_hour - login_hour == 1 and logout_minute >= login_minute:
            if logout_minute - login_minute < 0:
                hour = str(logout_hour - login_hour - 1).zfill(2)
                minute = str(60 - abs(logout_minute - login_minute)).zfill(2)
            else:
                hour = str(logout_hour - login_hour).zfill(2)
                minute = str(logout_minute - login_minute).zfill(2)
            return f"{id} {hour}:{minute}"
        elif abs(logout_hour - login_hour) > 1:
            if logout_minute - login_minute < 0:
                hour = str(logout_hour - login_hour - 1).zfill(2)
                minute = str(60 - abs(logout_minute - login_minute)).zfill(2)
            else:
                hour = str(logout_hour - login_hour).zfill(2)
                minute = str(logout_minute - login_minute).zfill(2)
            return f"{id} {hour}:{minute}"


while True:
    try:
        time_table = list(map(str, input().split(", ")))
        id = time_table[0]
        login_hour = int(time_table[1][0:2])
        login_minute = int(time_table[1][3:5])
        logout_hour = int(time_table[2][0:2])
        logout_minute = int(time_table[2][3:5])
        cl = Time(id, login_hour, login_minute, logout_hour, logout_minute)
        if cl.time_check() == None:
            pass
        else:
            print(cl.time_check())
    except:
        break