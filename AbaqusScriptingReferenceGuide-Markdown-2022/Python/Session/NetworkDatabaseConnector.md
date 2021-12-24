# NetworkDatabaseConnector object

The NetworkDatabaseConnector object allows you to access an output database on a remote system.

## Access

```
session.networkDatabaseConnectors[name]
```

## NetworkDatabaseConnector(...)



This method creates a NetworkDatabaseConnector object that you can use to access a remote output database. You can create a network database connector from any platform: Windows or Linux. However, the network database connector server must reside on a Linux platform; you cannot access an output database that resides on a remote Windows system. You can access only a remote output database; you cannot access a remote model database.



### Path

```
session.NetworkDatabaseConnector
```

### Required arguments

- *name*

  A String specifying the repository key.

- *hostName*

  A String specifying the name of the remote computer.

- *directory*

  A String specifying the directory on the remote computer.

### Optional arguments

- *remoteAbaqusDriverName*

  A String specifying the name of command to execute Abaqus/CAE on the remote computer.

- *remoteLoginMechanism*

  A SymbolicConstant specifying the remote shell command on the local system. Possible values are RSH and SSH. The default value is SSH.

- *sshPath*

  A String specifying the path to the`ssh` command on the local system. The default value is an empty string.

- *serverPort*

  An Int specifying the server port on the remote computer. If *serverPort* =0, the host and remote systems are allowed to establish their own port numbers. The default value is 0.

- *connectionPort*

  An Int specifying the connection port on the remote computer. The default value is 0.

- *serverTimeout*

  An Int specifying the timeout in seconds for the remote server. For example: 86400 corresponds to one day. The server exits if it does not receive any communication from the client during the time specified. The default value is 86400.

- *allowAutomaticStartup*

  A Boolean specifying whether to start the remote network database connector server. The default value is ON.

### Return value

A NetworkDatabaseConnector object.

### Exceptions

None.



## start(...)



This method starts the remote network database connector server on the remote host.



### Required arguments

None.

### Optional arguments

- *serverPort*

  An Int specifying the server port on the remote computer. If *serverPort* =0, the host and remote systems are allowed to establish their own port numbers. The default value is 0.

- *serverTimeout*

  An Int specifying the timeout in seconds for the remote server. For example: 86400 corresponds to one day. The server exits if it does not receive any communication from the client during the time specified. The default value is 86400.

### Return value

None.

### Exceptions

None.



## stop()



This method stops the remote network database connector server on the remote host.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## setValues(...)



This method modifies the NetworkDatabaseConnector object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [NetworkDatabaseConnector ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-networkdatabaseconnectorpyc.htm?ContextScope=all#simaker-networkdatabaseconnectornetworkdatabaseconnectorpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The NetworkDatabaseConnector object has members with the same names and descriptions as the arguments to the [NetworkDatabaseConnector ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-networkdatabaseconnectorpyc.htm?ContextScope=all#simaker-networkdatabaseconnectornetworkdatabaseconnectorpyc)method.

In addition, the NetworkDatabaseConnector object has the following member:

- *connected*

  A Boolean specifying if the connection between the client and the server is established.