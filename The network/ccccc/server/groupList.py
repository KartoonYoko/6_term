#!/usr/bin/env python
# --*-- coding: utf-8 --*--
import json


class GroupList:
    # { nameOfGroup: {file 1: "rules", ..., file n: "rules"} }
    def __init__(self, file_name="groups.json"):
        self.file_name = file_name
        self.groups = {}  # задаем структуру для хранения
        with open(self.file_name, "r") as read_file:
            try:
                self.groups = json.load(read_file)
                self.update_file()
            except Exception as err:
                with open(self.file_name, "w") as write_file:
                    json.dump(self.groups, write_file)

    def get_group(self, name):
        self.groups.get(name)

    def get_list_groups(self):
        res = ''
        for key in self.groups:
            res += key + '\n'
        return res

    def get_group_file_rules(self, file, group):
        """
            get file rules for group
        :return:
        """
        buf = self.groups.get(group)
        if buf:
            return buf.get(file)

    def get_file_rules(self, file):
        res = ''
        for key in self.groups:
            buf = self.groups[key]
            if buf.get(file):
               res += key + ': ' + self.groups[key][file] + '\n'
        return res

    def add_rules_to_file(self, name, file, rules):
        """
        :param: String name - name of group
        :param: String file - abs path of file
        :param: String rules
        { name: {file 1: "rules", ..., file n: "rules"} }
        """
        if not self.groups.get(name):
            self.groups[name] = {}
        self.groups[name][file] = rules
        self.update_file()

    def update_file(self):
        with open(self.file_name, "w") as write_file:
            json.dump(self.groups, write_file)


if __name__ == "__main__":
    gr = GroupList()
    gr.add_rules_to_file("common", "file.txt", "rw-")      # mode test.jpg common rw-
    gr.add_rules_to_file("test.jpg", "file.txt", "---")
    print(gr.get_list_groups())
    print(gr.get_file_rules("file.txt"))

