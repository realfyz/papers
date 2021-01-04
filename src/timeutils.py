

import timeago, time


def perform(historytime):
    k = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    return timeago.format(historytime, k, 'zh_CN')


