import webbrowser 
import time
'''
自動開啟網頁，並填入google表單內容，開啟後確認輸入是否正確，按送出表單即可
簽到直接使用時間進行判斷，稍微檢查是否勾選正確即可。
'''

#指定你的chrome路徑
chromePath = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'  
email = 'titus.leo616@gmail.com'
name = '郭彥明'
student_id = '16'
note = '' #備註

# ---- 下面不需修改
time_stamp = {}
time_struct = {}
time_str = {}
sign_type_list = ['上午簽到', '上午簽退', '下午簽到', '下午簽退']
t_now, t0, t1, t2 = 'now', '11:30:00', '12:40:00', '14:00:00'

def get_time_info(t_now, t0, t1, t2):
    time_stamp[t_now] = int(time.time()) # current time stamp
    time_struct[t_now] = time.localtime(time_stamp[t_now]) # convert time_stamp to time struct
    time_str[t_now] = time.strftime("%Y-%m-%d %H:%M:%S", time_struct[t_now]) # convert time struct to time string

    time_str[t0] = time_str[t_now].split(' ')[0] + f' {t0}' # 判斷上午簽到結束時間
    time_struct[t0] = time.strptime(time_str[t0], "%Y-%m-%d %H:%M:%S")
    time_stamp[t0] = int(time.mktime(time_struct[t0]))

    time_str[t1] = time_str[t_now].split(' ')[0] + f' {t1}' # 判斷 上午簽退結束時間
    time_struct[t1] = time.strptime(time_str[t1], "%Y-%m-%d %H:%M:%S")
    time_stamp[t1] = int(time.mktime(time_struct[t1]))

    time_str[t2] = time_str[t_now].split(' ')[0] + f' {t2}' # 判斷下午簽到結束時間
    time_struct[t2] = time.strptime(time_str[t2], "%Y-%m-%d %H:%M:%S")
    time_stamp[t2] = int(time.mktime(time_struct[t2]))
    return time_stamp, time_struct, time_str

def get_sign_type(time_stamp):
    idx = 0
    t_tamp = time_stamp[t_now]
    for t in time_stamp.values():
        if t_tamp > t:
            idx +=1
    return sign_type_list[idx]

def main():
    time_stamp, time_struct, time_str = get_time_info(t_now,t0,t1,t2)
    today_date = time_str[t_now].split(' ')[0]
    sign_type = get_sign_type(time_stamp)
    url = 'https://docs.google.com/forms/d/e/1FAIpQLScyj-cxY3QSgqXyQn-UNd06nhDGSfdtJtUk0QFPL7Fvlx2Fgg/viewform?'\
                f'entry.947274367={student_id}&entry.1397597325={name}&entry.1895033237={note}'\
                f'&entry.750854324={today_date}&entry.1235639024={sign_type}&emailAddress={email}'

    #註冊Chrome 瀏覽器
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
    #指定Chrome開啟網頁
    webbrowser.get('chrome').open_new(url) 
    print('open...')
    time.sleep(1)
    print('Done')
main()