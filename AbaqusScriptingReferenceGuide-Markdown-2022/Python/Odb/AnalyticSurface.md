# AnalyticSurface object

The AnalyticSurface object is a geometric surface that can be described with straight and/or curved line segments.

## Access

```
import odbAccess
session.odbs[name].parts[name].analyticSurface
session.odbs[name].rootAssembly.instances[name].analyticSurface
session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i]\
.instance.analyticSurface
```

## Members

The AnalyticSurface object has the following members:

- *name*

  A String specifying the name of the analytic surface.

- *type*

  A SymbolicConstant specifying the type of AnalyticSurface object. Possible values are SEGMENTS, CYLINDER, and REVOLUTION.

- *filletRadius*

  A Float specifying radius of curvature to smooth discontinuities between adjoining segments. The default value is 0.0.

- *segments*

  An [OdbSequenceAnalyticSurfaceSegment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsequenceanalyticsurfacesegmentpyc.htm?ContextScope=all) object specifying the profile associated with the surface.

- *localCoordData*

  A tuple of tuples of Floats specifying the global coordinates of points representing the local coordinate system, if used.