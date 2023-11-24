from passlib.hash import pbkdf2_sha256
WEEKLY_PATH = "C:/Users/timmy/PycharmProjects/AttendanceVK2/pages/data/weekly.csv"
DAILY_PATH = "C:/Users/timmy/PycharmProjects/AttendanceVK2/pages/data/daily.csv"
PIN_PATH = "C:/Users/timmy/PycharmProjects/AttendanceVK2/pages/data/pins.json"
LOGGED_IN_PATH = "C:/Users/timmy/PycharmProjects/AttendanceVK2/pages/data/logged_in.pickle"
LAST_UPDATE_PATH = "C:/Users/timmy/PycharmProjects/AttendanceVK2/pages/data/last_updated.pickle"
LOG_PATH = "C:/Users/timmy/PycharmProjects/AttendanceVK2/pages/data/log.txt"
REALTIME_UPDATE_PATH = "C:/Users/timmy/PycharmProjects/AttendanceVK2/pages/data/realtime.pickle"
ADMIN_PW = pbkdf2_sha256.hash("hello")
SECRET_PATH = "C:/Users/timmy/PycharmProjects/AttendanceVK2/pages/data/client_secrets.json"
