# LightOptions object

The LightOptions object stores settings that control how objects are lit when the *renderStyle* is set to SHADED. LightOptions objects are accessed in one of two ways:

- The default light options. These settings are used as defaults when you start a session and by the Defaults button on the Light Options dialog box.
- The light options associated with a particular viewport.

The LightOptions object has no constructor; Abaqus creates the *defaultLightOptions* member when a session is started. When a new viewport is created, the *lightOptions* member is copied from the current viewport.

## Access

```
session.defaultLightOptions
session.viewports[name].lightOptions
```

## setValues(...)



This method modifies the LightOptions object.



### Required arguments

None.

### Optional arguments

- *shading*

  A SymbolicConstant specifying the shading technique that should be used to fill facets for geometric bodies when *renderStyle* =SHADED. The lighting of facets for meshed geometry is not affected by this setting. Possible values are:GOURAUD, specifying that lighting values should be computed for each corner of a facet and interpolated to fill the remainder of the facet.PHONG, specifying that lighting values should be computed for each pixel of a facet.The default value is GOURAUD.When set to *shading* =GOURAUD, lighting values are computed for each corner of a facet and the lighting for the remainder of the facet is interpolated from the corner values. When *shading* =PHONG, lighting values are computed for each pixel of a facet.Note:The shading technique can only be set to PHONG when the *shadersAvailable* member of [GraphicsOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-graphicsoptionspyc.htm?ContextScope=all) is True.Printed output will only contain Phong shading if the output format is raster and the *accelerateOffScreen* member of [GraphicsOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-graphicsoptionspyc.htm?ContextScope=all) is ON.The *renderStyle* setting is part of [AssemblyDisplayOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblydisplayoptionspyc.htm?ContextScope=all), [PartDisplayOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partdisplayoptionspyc.htm?ContextScope=all), and various other options objects not listed here since they are generally used for meshed geometry.

- *viewpoint*

  A SymbolicConstant specifying how specular highlights should be calculated. Possible values are:INFINITE, specifying that a constant vector should be used for the direction from the camera to a vertex when computing specular highlights.LOCAL, specifying that the vector from the camera to each vertex should be calculated when computing specular highlights.The default value is INFINITE.When set to *viewpoint* =INFINITE, a constant vector is used for the direction from the camera (viewpoint) to a vertex. When *viewpoint* =LOCAL, the result is more realistic because the actual vector from the camera to each vertex is calculated. However, overall performance is decreased.

- *ambientColor*

  A String specifying the light applied evenly to the entire scene independent of any individual light. The initial value is 20% gray. A list of valid color strings is in the *colors* map in the *session* object.

- *materialShininess*

  A Float specifying the degree to which specular reflection is focused. The higher the *materialShininess* argument, the more focused the specular highlight. Possible values are 0.0 ≤≤ *polygonOffsetConstant* ≤≤ 128.0. The default value is 105.0.

### Return value

None.

### Exceptions

RangeError.



## Members

The LightOptions object has the following members:

- *shading*

  A SymbolicConstant specifying the shading technique that should be used to fill facets for geometric bodies when *renderStyle* =SHADED. The lighting of facets for meshed geometry is not affected by this setting. Possible values are:GOURAUD, specifying that lighting values should be computed for each corner of a facet and interpolated to fill the remainder of the facet.PHONG, specifying that lighting values should be computed for each pixel of a facet.The default value is GOURAUD.When set to *shading* =GOURAUD, lighting values are computed for each corner of a facet and the lighting for the remainder of the facet is interpolated from the corner values. When *shading* =PHONG, lighting values are computed for each pixel of a facet.Note:The shading technique can only be set to PHONG when the *shadersAvailable* member of [GraphicsOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-graphicsoptionspyc.htm?ContextScope=all) is True.Printed output will only contain Phong shading if the output format is raster and the *accelerateOffScreen* member of [GraphicsOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-graphicsoptionspyc.htm?ContextScope=all) is ON.The *renderStyle* setting is part of [AssemblyDisplayOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblydisplayoptionspyc.htm?ContextScope=all), [PartDisplayOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partdisplayoptionspyc.htm?ContextScope=all), and various other options objects not listed here since they are generally used for meshed geometry.

- *viewpoint*

  A SymbolicConstant specifying how specular highlights should be calculated. Possible values are:INFINITE, specifying that a constant vector should be used for the direction from the camera to a vertex when computing specular highlights.LOCAL, specifying that the vector from the camera to each vertex should be calculated when computing specular highlights.The default value is INFINITE.When set to *viewpoint* =INFINITE, a constant vector is used for the direction from the camera (viewpoint) to a vertex. When *viewpoint* =LOCAL, the result is more realistic because the actual vector from the camera to each vertex is calculated. However, overall performance is decreased.

- *materialShininess*

  A Float specifying the degree to which specular reflection is focused. The higher the *materialShininess* argument, the more focused the specular highlight. Possible values are 0.0 ≤≤ *polygonOffsetConstant* ≤≤ 128.0. The default value is 105.0.

- *lights*

  A [LightArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-lightpyc.htm?ContextScope=all) object of length 8.

- *ambientColor*

  A String specifying the light applied evenly to the entire scene independent of any individual light. The initial value is 20% gray. A list of valid color strings is in the *colors* map in the *session* object.