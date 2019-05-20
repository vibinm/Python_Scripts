"""class variable / methods"""


class Connections:
    connection_counter = 0  # class variable
    max_connection = 5

    def __init__(self, connection_id):
        self.connection_id = connection_id
        Connections.connection_counter += 1
        Connections.check_4_limit()

    @classmethod
    def check_4_limit(cls):
        if cls.connection_counter > cls.max_connection:
            raise ConnectionError('reached maximum allowed current connections....')


if __name__ == '__main__':
    list_of_connections = list()

    try:
        for item in range(1, 8):
            c = Connections(item)
            list_of_connections.append(c)
    except ConnectionError as err:
        print(err)

    for c_object in list_of_connections:
        print(c_object.connection_id, c_object.connection_counter, c_object.max_connection)