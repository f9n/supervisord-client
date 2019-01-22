import xmlrpc.client


class XmlRpc(object):
    __instance = None

    def __init__(self, host, port, username, password):
        if XmlRpc.__instance != None:
            raise Exception(
                "This class is a singleton! You already created an xmlrpc object."
            )

        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connection = XmlRpc.get_connection(host, port, username, password)
        XmlRpc.__instance = self

    @staticmethod
    def getInstance():
        if XmlRpc.__instance == None:
            raise Exception(
                "This class is a singleton! First, you must create an xmlrpc object."
            )

        return XmlRpc.__instance

    @staticmethod
    def get_connection(host, port, username, password):
        if username == "" and password == "":
            address = "http://{0}:{1}/RPC2".format(host, port)
        else:
            address = "http://{0}:{1}@{2}:{3}/RPC2".format(
                username, password, host, port
            )

        return xmlrpc.client.ServerProxy(uri=address)

    @property
    def is_connected(self):
        try:
            self.connection.system.listMethods()
            print("Yes, node connected.")
            return True
        except Exception as err:
            print(err)
            return False

    def serialize(self):
        return {
            "host": self.host,
            "port": self.port,
            "username": self.username,
            "password": self.password,
            "connected": self.is_connected,
        }

    def __str__(self):
        return "xmlrpc: {}:{}".format(self.host, self.port)
