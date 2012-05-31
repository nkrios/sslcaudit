''' ----------------------------------------------------------------------
SSLCAUDIT - a tool for automating security audit of SSL clients
Released under terms of GPLv3, see COPYING.TXT
Copyright (C) 2012 Alexandre Bezroutchko abb@gremwell.com
---------------------------------------------------------------------- '''

class ControllerEvent(object):
    '''
    Base class.
    '''
    pass

class ClientConnectionAuditEvent(ControllerEvent):
    '''
    This is a base class for events produced while auditing individual client connections.
    '''
    def __init__(self, conn, profile):
        self.conn = conn
        self.profile = profile

    def __eq__(self, other):
        return (self.__class__ == other.__class__) and (self.__dict__ == other.__dict__)


class ClientConnectionAuditResult(ClientConnectionAuditEvent):
    '''
    This class contains audit results returned by handle() method of subclasses of BaseServerHandler. It
    contains the results of the audit of a single connection.
    '''

    def __init__(self, conn, profile, result):
        ClientConnectionAuditEvent.__init__(self, conn, profile)
        self.result = result

    def __str__(self):
        return ' CCAR(%s, %s)' % (self.profile, self.result)

class ClientAuditStartEvent(ControllerEvent):
    '''
    This event is generated by ClientHandler on very first connection.
    It carries the list of test profiles scheduled for this client.
    '''
    def __init__(self, client_id, profiles):
        self.client_id = client_id
        self.profiles = profiles


class ClientAuditEndResult(ControllerEvent):
    '''
    This event is generated by ClientHandler after very last connection, after ClientAuditEndEvent.
    It contains results produced by handle() methods of all client connection auditors, for a single client.
    '''

    def __init__(self, client_id):
        self.client_id = client_id
        self.results = []

    def add(self, res):
        self.results.append(res)
