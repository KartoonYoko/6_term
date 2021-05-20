#!/usr/bin/env python
# --*-- coding: utf-8 --*--
import json
import os
COMMON_GROUP = "common"

class UsersList:
    def __init__(self, file_name="users.json"):
        self.file_name = file_name
        self.users = {}  # задаем структуру для хранения пользователей
        with open(self.file_name, "r") as read_file:
            try:
                self.users = json.load(read_file)
                self.update_file()
            except Exception as err:
                with open(self.file_name, "w") as write_file:
                    json.dump(self.users, write_file)

    def get_user(self, name):
        self.users.get(name)

    def add_user(self, name, passw, group=COMMON_GROUP):
        """
        { name: [pass, group] }
        """
        if not ((name == "anonymous") and (passw == "anonymous")):
            self.users[name.lower()] = [passw, group]
        self.update_file()

    def update_file(self):
        with open(self.file_name, "w") as write_file:
            json.dump(self.users, write_file)

    def get_group(self, name):
        """
        get group of user
        :param String name:
        :return:
        """
        return self.users[name][1]

    def set_group(self, name, group):
        if self.users.get(name):
            self.users[name][1] = group
            self.update_file()

    def get_all_users(self):
        res = ''
        for key in self.users:
            res += key + ": " + self.users[key][1] + '\n'
        return res
