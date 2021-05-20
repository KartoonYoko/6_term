#!/usr/bin/env python
# --*-- coding: utf-8 --*--
import os
import stat
import time


def parse_file_info(file):
    """
    parse files information "drwxr-xr-x 2 root wheel 1024 Nov 17 1993 lib" result like follower
                            "drwxr-xr-x", "2", "root", "wheel", "1024 Nov 17 1993", "lib"
    """
    item = [f for f in file.split(' ') if f != '']
    mode, num, owner, group, size, date, filename = (
        item[0], item[1], item[2], item[3], item[4], ' '.join(item[5:8]), ' '.join(item[8:]))
    return (mode, num, owner, group, size, date, filename)


def fileProperty(filepath):
    """
    :param filepath: путь к каталогу
    return information from given file, like this "-rw-r--r-- 1 User Group 312 Aug 1 2014 filename"
    """
    st = os.stat(filepath)
    fileMessage = []

    def _getFileMode():
        modes = [
            stat.S_IRUSR, stat.S_IWUSR, stat.S_IXUSR,
            stat.S_IRGRP, stat.S_IWGRP, stat.S_IXGRP,
            stat.S_IROTH, stat.S_IWOTH, stat.S_IXOTH,
        ]
        mode = st.st_mode
        fullmode = ''
        fullmode += os.path.isdir(filepath) and 'd' or '-'

        for i in range(9):
            fullmode += bool(mode & modes[i]) and 'rwxrwxrwx'[i] or '-'
        return fullmode

    def _getFilesNumber():
        return str(st.st_nlink)

    def _getUser():
        return str(st.st_uid)

    def _getGroup():
        return str(st.st_gid)

    def _getSize():
        return str(st.st_size)

    def _getLastTime():
        return time.strftime('%b %d %H:%M', time.gmtime(st.st_mtime))
    for func in ('_getFileMode()', '_getFilesNumber()', '_getUser()', '_getGroup()', '_getSize()', '_getLastTime()'):
        fileMessage.append(eval(func))
    fileMessage.append(os.path.basename(filepath))

    return ' '.join(fileMessage)

