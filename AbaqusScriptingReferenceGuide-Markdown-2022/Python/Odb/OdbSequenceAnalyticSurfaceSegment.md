# OdbSequenceAnalyticSurfaceSegment object

A sequence of [AnalyticSurfaceSegment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticsurfacesegmentpyc.htm?ContextScope=all) describing an analytic surface profile.

## Access

```
import odbAccess
session.odbs[name].parts[name].analyticSurface.segments
session.odbs[name].rootAssembly.instances[name].analyticSurface\
.segments
session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i]\
.instance.analyticSurface.segments
```

## AnalyticSurfaceProfile()



This method creates a OdbSequenceAnalyticSurfaceSegment object.



### Path

odbAccess.AnalyticSurfaceProfile

### Arguments

None.

### Return value

An OdbSequenceAnalyticSurfaceSegment object.

### Exceptions

None.



## Start(...)



This method adds a [AnalyticSurfaceSegment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticsurfacesegmentpyc.htm?ContextScope=all) describing the first segment of the surface profile.



### Required arguments

- *origin*

  A sequence of Floats specifying the coordinates of start point.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Line(...)



This method adds a [AnalyticSurfaceSegment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticsurfacesegmentpyc.htm?ContextScope=all) describing the line segment of the surface profile.



### Required arguments

- *endPoint*

  A sequence of Floats specifying the coordinates of end point.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Circle(...)



This method adds a [AnalyticSurfaceSegment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticsurfacesegmentpyc.htm?ContextScope=all) describing a circular segment of the surface profile.



### Required arguments

- *center*

  A sequence of Floats specifying the coordinates of center of the circular segment.

- *endPoint*

  A sequence of Floats specifying the coordinates of end point of the circular segment.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Parabola(...)



This method adds a [AnalyticSurfaceSegment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticsurfacesegmentpyc.htm?ContextScope=all) describing a parabolic segment of the surface profile.



### Required arguments

- *middlePoint*

  A sequence of Floats specifying the coordinates of middle point of the parabolic segment.

- *endPoint*

  A sequence of Floats specifying the coordinates of end point of the parabolic segment.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The OdbSequenceAnalyticSurfaceSegment object has no members.