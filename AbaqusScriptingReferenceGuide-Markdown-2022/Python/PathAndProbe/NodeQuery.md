# NodeQuery object

The NodeQuery object specifies nodes and their coordinates in a path. The NodeQuery object has no constructor or methods. Abaqus creates the *nodeQuery* member when you import the visualization module.

## Access

```
import visualization
session.nodeQuery
```

## Members

The NodeQuery object has the following members:

- *nodeId*

  An Int specifying the ID of the most recently queried node. If the last query was unsuccessful, *nodeID*=−1.

- *nodePos*

  A tuple of Floats specifying the *X*-, *Y*-, and *Z*-coordinates of the most recently queried node.