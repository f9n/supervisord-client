from datetime import datetime, timedelta

from .xmlrpc import XmlRpc
from .utils import handle_exceptions


class Process:
    def __init__(self, dictionary):
        """
        dictionary = {
            'name': 'clock1',
            'group': 'clock1',
            'unique_name': 'clock1:clock1',
            'description': 'pid 8, uptime 0:13:48',
            'pid': 8,
            'start': 1544613566,
            'stop': 0,
            'now': 1544614394,
            'exitstatus': 0,
            'statename': 'RUNNING',
            'state': 20,
            'spawnerr': '',
            'logfile': '/opt/cesi-dev/logs/clock1.out.log', 
            'stderr_logfile': '/opt/cesi-dev/logs/clock1.err.log', 
            'stdout_logfile': '/opt/cesi-dev/logs/clock1.out.log',
        }
        """
        self.xmlrpc_api = XmlRpc.getInstance()

        self.dictionary = dictionary

        self.name = self.dictionary["name"]
        self.group = self.dictionary["group"]
        self.unique_name = "{group}:{name}".format(group=self.group, name=self.name)

        self.description = self.dictionary["description"]
        self.pid = self.dictionary["pid"]
        self.starttime = self.dictionary["start"]
        self.stoptime = self.dictionary["stop"]
        self.now = self.dictionary["now"]
        self.state = self.dictionary["state"]
        self.statename = self.dictionary["statename"]
        self.spawnerr = self.dictionary["spawnerr"]
        self.exitstatus = self.dictionary["exitstatus"]
        self.stdout_logfile = self.dictionary["stdout_logfile"]
        self.stderr_logfile = self.dictionary["stderr_logfile"]

        if self.state == 20:
            # description = 'pid 11039, uptime 0:00:03'
            __uptime_string = self.description.split(",")[1].strip()
            self.uptime = __uptime_string.split(" ")[1].strip()
        else:
            self.uptime = 0

        self.dictionary.update({"uptime": self.uptime})

    @handle_exceptions
    def start(self):
        self.xmlrpc_api.connection.supervisor.startProcess(self.unique_name)
        return True, ""

    @handle_exceptions
    def stop(self):
        self.xmlrpc_api.connection.supervisor.stopProcess(self.unique_name)
        return True, ""

    def restart(self):
        if self.state == 20:
            status, msg = self.stop()
            if not status:
                return status, msg

        return self.start()

    def stdout_log_with_read_method(self, offset, length):
        # readProcessStdoutLog(name, offset, length)
        pass

    def stdout_log_with_tail_method(self, offset, length):
        # tailProcessStdoutLog(name, offset, length)
        pass

    def stderr_log_with_read_method(self, offset, length):
        # readProcessStderrLog(name, offset, length)
        pass

    def stderr_log_with_tail_method(self, offset, length):
        # tailProcessStderrLog(name, offset, length)
        pass

    def clear_logs(self):
        # clearProcessLogs(name)
        pass

    def singal(self, signal_name):
        # signalProcess(name, signal)
        pass

    def serialize(self):
        return self.dictionary

