# CouplingConstraint object

The CouplingConstraint object.

## Access

```
        import visualization
        session.odbData[name].kinematicCouplings[i]
        session.odbData[name].distributingCouplings[i]
        session.odbData[name].shellSolidCouplings[i]
      
```

## constraintData(...)



This method returns node numbers of the surface being controlled by the control point.



### Required arguments

None.

### Optional arguments

None.

### Return value

Tuple-of-Ints Dictionary specifying the node numbers on the controlled surface.

### Exceptions

None.



## Members

The CouplingConstraint object has the following members:

- *name*

  A String specifying the coupling name. This attribute is read-only.

- *type*

  A String specifying the type of coupling. This attribute is read-only.