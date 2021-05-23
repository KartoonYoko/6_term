import sqlite3
from sqlite3 import Error
import os
from init_db import FTPdb


class DatabaseFTP(FTPdb):
    # execute_query - ordinary
    # execute_read_query - returning query

    def __init__(self, catalog, file_name="FTP_server_bd"):
        """
        :param catalog: name of catalog which files in
        :param file_name: name of file which stores database
        """
        super(DatabaseFTP, self).__init__(catalog, file_name)

    def get_user(self, name):
        """
        :param name: name of user
        :return List: [password, group]
        """
        if self.is_exist_user(name):
            query = """
            SELECT * FROM %s
            WHERE name = ?
            """ % self.users_table
            t = (name,)
            res = self.execute_read_query(query, t)
            passw = self.execute_read_query("""
            SELECT name
            FROM %s
            WHERE id = ?
            """ % self.groups_table, (res[0][3],))
            return [res[0][2], passw[0][0]]

    def set_user(self, name, passw, group=None):
        """
        """
        group_name = group if group else self.COMMON_GROUP
        if self.is_exist_group(group_name):
            query = """
                    SELECT id 
                    FROM %s
                    WHERE name = '%s'
                    """ % (self.groups_table, group_name)
            group_id = self.execute_read_query(query)[0][0]
            query = """
            INSERT INTO
            %s 
            VALUES (NULL, ?, ?, ?)
            """ % self.users_table
            t = (name, passw, group_id)
            self.execute_query(query, t)

    def get_group_of_user(self, name):
        """
        get group of user
        :param String name: name of user
        :return String: name of group
        """
        if self.is_exist_user(name):
            query = """
                    SELECT * FROM %s
                    WHERE name = ?
                    """ % self.users_table
            t = (name,)
            res = self.execute_read_query(query, t)
            query = """
                            SELECT name FROM %s
                            WHERE id = %d
                            """ % (self.groups_table, res[0][3])
            group = self.execute_read_query(query)[0][0]
            return group

    def set_group_to_user(self, name, group):
        """
        :param name: name of User
        :param group: name of Group
        """
        query = """
                        SELECT id FROM %s
                        WHERE name = ?
                        """ % self.groups_table
        t = (group,)
        group_id = self.execute_read_query(query, t)

        # make group if ones absent
        if not group_id:
            query = query = """
                        INSERT INTO
                        %s (NULL, ?)
                        VALUES
                        """ % self.groups_table
            t = (group,)
            self.execute_read_query(query, t)
        group_id = group_id[0][0]
        query = """
        UPDATE %s
        SET group_id = %d
        WHERE name = ?
        """ % (self.users_table, group_id)
        t = (name,)
        self.execute_read_query(query, t)

    def get_all_users(self):
        """
        :return String: all users
        """
        query = """
        SELECT * 
        FROM %s
        """ % self.users_table
        users = self.execute_read_query(query)
        res = 'Username\t|\tGroup\n'

        for key in users:
            res += key[1] + ":\t\t"  # name
            query = """
            SELECT name 
            FROM %s
            WHERE id = %d
            """ % (self.groups_table, key[3])   # group
            group = self.execute_read_query(query)[0][0]
            res += group + "\n"
        return res

    def get_file_rules(self, group, file):
        """
        :param String group: name of group
        :param String file: absolute path to file
        :return String: 'rwx'
        """
        if self.is_exist_group(group) and self.is_exist_file(file):
            group_id = self.get_group_id(group)
            file_id = self.get_file_id(file)
            query = """
                    SELECT rule
                    FROM %s
                    WHERE group_id = %d and file_id = %d
                    """ % (self.groups_files_table, group_id, file_id)
            res = self.execute_read_query(query)
            if res:
                if res[0]:
                    return res[0][0]

    def get_list_groups(self):
        res = ''
        query = """
                SELECT *
                FROM %s
                """ % self.groups_table
        groups = self.execute_read_query(query)
        for key in groups:
            res += key[1] + "\n"
        return res

    def get_files_list(self):
        query = """
                SELECT *
                FROM %s
                """ % self.files_table
        files = self.execute_read_query(query)
        res = ''
        for key in files:
            res += self.get_file_rules(self.COMMON_GROUP, key[1])[0] + '\t'
            res += key[1]
            res += '\n'
        return res


if __name__ == "__main__":
    ul = DatabaseFTP("storage", "FTP_server_bd.db")
    ul.set_user("tolik", "123qwe")
    ul.set_group_to_user("tolik", "common")
    print(ul.get_user("tolik"))
    print(ul.get_group_of_user("tolik"))
    print(ul.get_all_users())
    print(ul.get_list_groups())
    print(ul.get_files_list())
    print(ul.is_exist_group('common'))
    print(ul.get_file_rules('common', 'C:\\Users\\crash\\OneDrive\\Рабочий стол\\Домашка\\6_term\\The network\\ccccc\\server\\storage\\README'))

