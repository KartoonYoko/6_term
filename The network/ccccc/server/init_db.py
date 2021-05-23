import sqlite3
from sqlite3 import Error
import os
from log_func import *


class FTPdb:
    def __init__(self, catalog, file_name="FTP_server_bd"):
        """
        :param String catalog: name of catalog where stores all files
        :param String file_name: path to db file
        create 4 tables (users, groups, files, groups_files_table),
        add common group for all users,
        add all files in catalog to table "files",
        add rules to all files for common group
        """
        self.file_name = file_name
        # Tables names
        self.users_table = "users"
        self.groups_table = "groups"
        self.files_table = "files"
        self.groups_files_table = "groups_files_table"

        self.connection = None
        self.path = os.path.abspath(self.file_name)
        self.execute_query('pragma encoding=UTF16')

        create_users_table = """
        CREATE TABLE IF NOT EXISTS %s (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL UNIQUE,
          password TEXT NOT NULL,
          group_id INTEGER NOT NULL
        );
        """ % self.users_table
        create_groups_table = """
        CREATE TABLE IF NOT EXISTS %s (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
        """ % self.groups_table
        create_files_table = """
        CREATE TABLE IF NOT EXISTS %s (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
        """ % self.files_table
        create_groups_files_table = """
        CREATE TABLE IF NOT EXISTS %s (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_id INTEGER,
            file_id INTEGER,
            rule TEXT,
            
            CONSTRAINT unq_ids UNIQUE (group_id, file_id)
        );
        """ % self.groups_files_table   # TODO Unique group and file ids
        self.execute_query(create_users_table)
        self.execute_query(create_groups_table)
        self.execute_query(create_files_table)
        self.execute_query(create_groups_files_table)

        # add common group for all new users
        self.COMMON_GROUP = "common"
        add_common_group = """
        INSERT INTO
        groups (name)
        VALUES ('common')
        """
        self.execute_query(add_common_group)

        #
        for dirpath, dirnames, filenames in os.walk(catalog):
            # перебрать файлы
            for filename in filenames:
                # filename = os.path.abspath(filename)
                filename = os.path.abspath(os.path.join(dirpath, filename))
                self.set_file(filename)
                # TODO add rules to each file for common group
                self.set_rules_to_file_for_group(self.COMMON_GROUP, filename, 'r--')

    def create_connection(self):
        try:
            self.connection = sqlite3.connect(self.path)
            # log("init FTP db", "Connection to SQLite DB successful")
        except Error as e:
            log("init FTP db", f"The error '{e}' occurred")

    def execute_query(self, query, t=None):
        self.create_connection()
        cursor = self.connection.cursor()
        try:
            if t:
                cursor.execute(query, t)
            else:
                cursor.execute(query)
            self.connection.commit()
            # log("init FTP db", "Query executed successfully")
        except Error as e:
            log("init FTP db", f"The error '{e}' occurred")

        self.connection.close()

    def execute_query_without_except(self, query, t=None):
        self.create_connection()
        cursor = self.connection.cursor()
        if t:
            cursor.execute(query, t)
        else:
            cursor.execute(query)
        self.connection.commit()

        self.connection.close()

    def execute_read_query(self, query, t=None):
        self.create_connection()
        cursor = self.connection.cursor()
        result = None
        try:
            if t:
                cursor.execute(query, t)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            log("init FTP db", f"The error '{e}' occurred")

        self.connection.close()

    def is_exist_group(self, group):
        query = """
        SELECT *
        FROM %s
        WHERE name = ?
        """ % self.groups_table
        t = (group,)
        if self.execute_read_query(query, t):
            return True
        else:
            return False

    def is_exist_file(self, file):
        file = self.path_change(file)
        query = """
        SELECT *
        FROM %s
        WHERE name = ?
        """ % self.files_table
        t = (file,)
        buf = self.execute_read_query(query, t)
        if buf:
            return True
        else:
            return False

    def is_exist_user(self, name):
        query = """
           SELECT *
           FROM %s
           WHERE name = ?
           """ % self.users_table
        t = (name,)
        if self.execute_read_query(query, t):
            return True
        else:
            return False

    def get_group_id(self, group):
        query = """
                SELECT id
                FROM %s
                WHERE name = ?
                """ % self.groups_table
        t = (group, )
        res = self.execute_read_query(query, t)
        if all(res[0]):
            return res[0][0]

    def get_file_id(self, file):
        file = self.path_change(file)
        query = """
                SELECT id
                FROM %s
                WHERE name = ?
                """ % self.files_table
        t = (file, )
        res = self.execute_read_query(query, t)
        if res:
            if res[0]:
                return res[0][0]

    def set_file(self, file):
        file = self.path_change(file)
        query = """
                INSERT INTO
                %s (id, name)
                VALUES (NULL, ?)
                """ % self.files_table
        t = (file,)
        self.execute_query(query, t)

    def set_rules_to_file_for_group(self, group, file, rules):
        """
        :param String group: name of group
        :param String file: abs path of file
        :param String rules: rwx
        """
        file = self.path_change(file)
        if self.is_exist_group(group) and self.is_exist_file(file):
            group_id = self.get_group_id(group)
            file_id = self.get_file_id(file)
            query = """
                    INSERT INTO
                        %s (id, group_id, file_id, rule)
                    VALUES (NULL, %d, %d, ?)
                    """ % (self.groups_files_table, group_id, file_id)
            t = (rules,)
            try:
                self.execute_query_without_except(query, t)
            except Error as e:
                self.connection.close()
                if e.args[0].find('UNIQUE constraint failed') != -1:
                    query = """
                            UPDATE %s
                            SET
                                rule = ?
                            WHERE group_id = %d and file_id = %d 
                            """ % (self.groups_files_table, group_id, file_id)
                    t = (rules,)
                    self.execute_query(query, t)

    def path_change(self, path):
        """
        change path to store it equally in database
        """
        file = os.path.abspath(path)
        file = file.replace("\\", "/")
        return file

