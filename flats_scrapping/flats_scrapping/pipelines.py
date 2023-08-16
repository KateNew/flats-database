# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from config import DATABASE_SETTINGS

import psycopg2

class PostgresPipeline:
    def __init__(self):

        self.connection = psycopg2.connect(**DATABASE_SETTINGS)
        self.cursor = self.connection.cursor()
        self.cursor.execute("DROP TABLE flats")
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS flats(
            id bigint PRIMARY KEY, 
            name text,
            image text
        )
        """)

    def process_item(self, item, spider):
        insert_query = "INSERT INTO flats (id,name, image) VALUES (%s,%s, %s)"
        data = (item["id"],item['name'], item['image'])  # Replace with your item fields
        self.cursor.execute(insert_query, data)
        self.connection.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()
