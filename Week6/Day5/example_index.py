import psycopg2
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'jes'
DATABASE = 'menu'


class MenuItem:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def save(self):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor = connection.cursor()

        query = f"INSERT INTO menuitem (name,price) VALUES ('"+str(self.name)+ "','"+str(self.price)+"');"

        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()

item = MenuItem('wrap', 50)
item.save()

    # @classmethod
    def delete(self):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor = connection.cursor()

        delete_query = f'DELETE FROM menuitem WHERE item = {self.name}'
        cursor.execute(delete_query)
        connection.commit()
        cursor.close()
        connection.close()

item = MenuItem('Burger')
item.delete()

    # @classmethod
    def update (self, new_price):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor = connection.cursor()
        self.price = new_price
        update_query = f"UPDATE menuitem set price = {self.price} where item = {self.name}"

        cursor.execute(update_query)
        connection.commit()
        cursor.close()
        connection.close()

    @classmethod
    def all(cls):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor = connection.cursor()
        all_query = "SELECT * FROM menu"
        cursor.execute(all_query)
