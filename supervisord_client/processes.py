from .xmlrpc import XmlRpc
from .process import Process


class Processes:
    def __init__(self):
        self.xmlrpc_api = XmlRpc.getInstance()

    def get(self):
        try:
            __processes = []
            all_process_info = self.xmlrpc_api.connection.supervisor.getAllProcessInfo()
            for _p in all_process_info:
                _process_object = Process(_p)
                __processes.append(_process_object)

            return __processes
        except Exception as e:
            print(e)
            return []

    def get_process(self, process_name):
        try:
            _p = self.xmlrpc_api.connection.supervisor.getProcessInfo(process_name)
            return Process(_p)
        except Exception as err:
            print(err)
            return None

    def get_by_group_name(self, group_name):
        return [p for p in self.get() if p.group == group_name]

    def start(self):
        # startAllProcesses
        pass

    def start_group(self, group_name):
        # startProcessGroup(name)
        pass

    def stop(self):
        # stopAllProcesses
        pass

    def stop_group(self, group_name):
        # stopProcessGroup(name)
        pass

    def signal(self, signal_name):
        # signalAllProcesses
        pass

    def signal_group(self, group_name, signal_name):
        # signalProcessGroup(name, signal)
        pass

    def clear_logs(self):
        # clearAllProcessLogs
        pass

    def add_group(self, name):
        # addProcessGroup(name)
        pass

    def remove_group(self, name):
        # removeProcessGroup(name)
        pass

    def send_remote_comm_event(self, type, data):
        # sendRemoteCommEvent(type, data)
        pass

    def send_process_stdin(self, name, chars):
        # sendProcessStdin(name, chars)
        pass

    def serialize(self):
        return [p.serialize() for p in self.get()]
