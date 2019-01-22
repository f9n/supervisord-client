from .xmlrpc import XmlRpc
from .processes import Processes


class Node:
    def __init__(self, name, host, port, username="", password=""):
        self.name = name
        self.xmlrpc_api = XmlRpc(host, port, username, password)
        self.processes = Processes()

    # Supervisor status and supervisor control
    @property
    def api_version(self):
        # self.xmlrpc_server.connection.supervisor.getAPIVersion()
        pass

    @property
    def version(self):
        # self.xmlrpc_server.connection.supervisor.getSupervisorVersion()
        pass

    @property
    def identification(self):
        # self.xmlrpc_server.connection.supervisor.getIdentification()
        pass

    @property
    def state(self):
        # self.xmlrpc_server.connection.supervisor.getState()
        pass

    @property
    def pid(self):
        # self.xmlrpc_server.connection.supervisor.getPID()
        pass

    def read_log(self, offset, length):
        # self.xmlrpc_server.connection.supervisor.readLog(offset, length)
        pass

    def clear_log(self):
        # self.xmlrpc_server.connection.supervisor.clearLog()
        pass

    def shutdown(self):
        # self.xmlrpc_server.connection.supervisor.shutdown()
        pass

    def restart(self):
        # self.xmlrpc_server.connection.supervisor.restart()
        pass

    def reload_config(self):
        pass

    def serialize(self):
        return {
            "name": self.name,
            "processes": self.processes.serialize(),
            "connection": self.xmlrpc_api.serialize(),
        }

    def __str__(self):
        return "node:{}".format(self.name)
