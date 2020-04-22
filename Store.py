import json
class Product:
    def __init__(self, title, price):
        if int(price) > 1000:
            raise ProductPriceException("Слишком дорого!")
        elif int(price) < 1:
            raise ProductPriceException("Даром - не пойдет!")
        self.title = title
        self.price = int(price)

class ProductPriceException(Exception):
    pass



class Store:
    def __init__(self, title="Магазин на диване"):
        self.title = title
        self.storage = {}

    def add_product(self, product, number_of_products=1):

        if product in self.storage:
            self.storage[product] += int(number_of_products)
        else:
            self.storage[product] = int(number_of_products)

    def _product_details(self, product):
        message_template = "Количество товара %s: %s штук, стоимость: %s. Суммарная стоимость: %s "

        product_count = self.storage[product]
        product_title = product.title
        product_price = product.price
        product_total_price = product_price * product_count

        rendered_message = message_template % (product_title, product_count, product_price, product_total_price)

        return rendered_message

    def showcase(self, product=None):
        if product:
            print(self._product_details(product))
        else:
            for product in self.storage.keys():
                print(self._product_details(product))


class Manager:

    store = None

    @staticmethod
    def create_add_to_store_products():
        """
        Метод, который создает магазин (вызывает метод create_store для создания.)
        Спрашивает не желаете ли создать продукт. И если ответ положительный - создает продукт (create_product).
        с помощью while и какого-то условия можно повторять процесс создания продукта, до тех пор,
        пока пользователь не решит что продукты создавать больше не нужно. И не ответит на вопрос о желании
        создать продукт отрицательно.
        """
        # message = input("Хотите ли вы создать магазин? Y/N:")
        if Manager.store == None:
            message = input("Хотите ли вы создать магазин? Y/N:")
            if message == "Y":
                Manager.store = Manager.create_store()
            elif message == "N":

                return


        create_next_product = True
        while create_next_product:



            message2 = input("Хотите создать товар? Y/N:")

            if message2 == 'N':
                Manager.dump_data_to_file()
                create_next_product = False
            elif message2 == 'Y':
                product = Manager.create_product()
                product_number = int(input("Введите количество товара:"))
                Manager.store.add_product(product, product_number)









    @staticmethod
    def create_product():
        """
        Метод который запускает процесс создания продукта, и просит ввести данные с клавиатуры.
        Возвращает продукт.
        """
        title = input('Введите название товара: ')
        price = input('Введите цену товара: ')
        return Product(title=title, price=price)

    @staticmethod
    def create_store():
        """
        Метод который создает магазин и помезает его в аттрибут класса store. (Manager.store) Если магазин
        уже создан и добавлен, то метод возвращает текущий магазани, а не пересоздает новый.
        """
        if Manager.store is None:
            store_title = input('Введите название магазина: ')
            Manager.store = Store(title=store_title)
        return Manager.store


    @staticmethod
    def dump_data_to_file():
        file = open("store.txt","w")
        store_title = Manager.store.title
        file_dump={"store_title" : store_title, "storage" : []}
        for k in Manager.store.storage.keys():
            product_title = k.title
            product_price = k.price
            product_count = Manager.store.storage[k]
            file_dump["storage"].append((product_title,product_price,product_count))
        j=json.dump(file_dump, file)
        file.close()
        print(f"Магазин {store_title} записан в файл 'store.txt'")




    @staticmethod
    def load_data_from_file():

        store_data=open("store.txt","r")
        l=json.load(store_data)
        Manager.store = Store(title = l["store_title"])
        for record in l["storage"]:
            product=Product(title=record[0],price=record[1])
            Manager.store.add_product(product=product, number_of_products=record[2])
        store_data.close()

Manager.create_add_to_store_products()
