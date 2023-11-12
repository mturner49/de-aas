from db.mongodb import Mongo


def main():
    host = 'localhost'
    port = 27017

    db = Mongo(host, port)

    db.create_database('test_database')


if __name__ == '__main__':
    main()