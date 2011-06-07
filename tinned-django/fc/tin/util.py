# -*- coding: utf-8 -*-
import re
from fabric.operations import local

def usernames_unixgroup():
    group_file = local('cat /etc/group', capture=True)
    # Ищем строку в /etc/groups вида "groupname:x:1006:usr1,usr2,usr3",
    # чтобы создавать учётки для перечисленных в ней пользователей
    matches = re.search(GROUP_FOR_PARSE+':x:\d+:(?P<users>[\w,]+)', group_file)
    user_list = (matches.group(1)).split(',')
    return user_list