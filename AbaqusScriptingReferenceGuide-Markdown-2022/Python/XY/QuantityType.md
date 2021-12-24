# QuantityType object

The QuantityType object is used to store attributes defining the physical dimension and label of the quantity type to be associated with an [XYData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xydatapyc.htm?ContextScope=all) or an [AxisData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-axisdatapyc.htm?ContextScope=all) object.

QuantityType objects are automatically created when creating [XYData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xydatapyc.htm?ContextScope=all) objects from the odb.

QuantityType objects can be created using the methods described below.

## Access

```
import visualization
session.charts[name].axes1[i].axisData.curves[i].data\
.axis1QuantityType
session.charts[name].axes1[i].axisData.curves[i].data\
.axis2QuantityType
session.charts[name].axes1[i].axisData.quantityType
session.charts[name].axes2[i].axisData.curves[i].data\
.axis1QuantityType
session.charts[name].axes2[i].axisData.curves[i].data\
.axis2QuantityType
session.charts[name].axes2[i].axisData.quantityType
session.charts[name].curves[name].data.axis1QuantityType
session.charts[name].curves[name].data.axis2QuantityType
session.curves[name].data.axis1QuantityType
session.curves[name].data.axis2QuantityType
session.defaultChartOptions.defaultAxis1Options.axisData.curves[i]\
.data.axis1QuantityType
session.defaultChartOptions.defaultAxis1Options.axisData.curves[i]\
.data.axis2QuantityType
session.defaultChartOptions.defaultAxis1Options.axisData.quantityType
session.defaultChartOptions.defaultAxis2Options.axisData.curves[i]\
.data.axis1QuantityType
session.defaultChartOptions.defaultAxis2Options.axisData.curves[i]\
.data.axis2QuantityType
session.defaultChartOptions.defaultAxis2Options.axisData.quantityType
import odbAccess
session.odbs[name].userData.axis1QuantityType
session.odbs[name].userData.axis2QuantityType
import visualization
import xyPlot
session.odbs[name].userData.xyDataObjects[name].axis1QuantityType
session.odbs[name].userData.xyDataObjects[name].axis2QuantityType
session.xyDataObjects[name].axis1QuantityType
session.xyDataObjects[name].axis2QuantityType
session.xyPlots[name].charts[name].axes1[i].axisData.curves[i].data\
.axis1QuantityType
session.xyPlots[name].charts[name].axes1[i].axisData.curves[i].data\
.axis2QuantityType
session.xyPlots[name].charts[name].axes1[i].axisData.quantityType
session.xyPlots[name].charts[name].axes2[i].axisData.curves[i].data\
.axis1QuantityType
session.xyPlots[name].charts[name].axes2[i].axisData.curves[i].data\
.axis2QuantityType
session.xyPlots[name].charts[name].axes2[i].axisData.quantityType
session.xyPlots[name].charts[name].curves[name].data.axis1QuantityType
session.xyPlots[name].charts[name].curves[name].data.axis2QuantityType
session.xyPlots[name].curves[name].data.axis1QuantityType
session.xyPlots[name].curves[name].data.axis2QuantityType
```

## QuantityType(...)



This method creates a QuantityType object.



### Path

session.QuantityType

xyPlot.QuantityType

### Required arguments

None.

### Optional arguments

- *label*

  A String specifying the label for this quantity type.

- *type*

  A SymbolicConstant specifying the physical dimension of the axis. Possible values are:

  - NONE.
  - ACCELERATION.
  - ACOUSTIC_INTENSITY.
  - ANGLE.
  - ANGULAR_MOMENTUM.
  - ARC_LENGTH.
  - AREA.
  - AREA_VELOCITY_SQUARED, specifying "Velocity squared per area".
  - BIMOMENT.
  - CURVATURE.
  - CORIOLIS_LOAD.
  - DAMAGE.
  - DAMAGE_CRITERION.
  - DENSITY.
  - DENSITY_ROTATIONAL_ACCELERATION, specifying "Density * Angular acceleration".
  - DISPLACEMENT.
  - ECURRENT_AREA_TIME, specifying "Time integrated electric current per area".
  - ELECTRIC_CHARGE.
  - ELECTRIC_CURRENT.
  - ELECTRIC_CURRENT_AREA, specifying "Electric current per unit area".
  - ELECTRIC_POTENTIAL.
  - ENERGY.
  - ENERGY_DENSITY.
  - ENERGY_RELEASE_RATE.
  - EPOTENTIAL_GRADIENT, specifying "Electric potential gradient".
  - FREQUENCY.
  - FORCE.
  - FORCE_VOLUME, specifying "Force per volume".
  - HEAT_FLUX.
  - HEAT_FLUX_AREA, specifying "Heat flux per area".
  - HEAT_FLUX_RATE.
  - HEAT_FLUX_VOLUME, specifying "Heat flux per volume".
  - LENGTH.
  - LINEAR_PRESSURE.
  - LUMIN, specifying "Luminous intensity".
  - MASS.
  - MASS_FLOW_AREA, specifying "Mass flow per area".
  - MASS_FLOW_AREA_RATE, specifying "Mass flow rate per area".
  - MASS_FLOW_RATE.
  - MODE_NUMBER.
  - MOMENT.
  - NUMBER.
  - PATH.
  - PHASE.
  - POSITION.
  - PRESSURE.
  - PRESSURE_GRADIENT.
  - RATE.
  - ROTARY_INERTIA.
  - ROTATIONAL_ACCELERATION.
  - ROTATIONAL_VELOCITY.
  - STATUS.
  - STRAIN.
  - STRAIN_RATE.
  - STRESS.
  - STRESS_INTENS_FACTOR, specifying "Stress intensity factor".
  - SUBSTANCE, specifying "Amount of substance".
  - TEMPERATURE.
  - THICKNESS.
  - TIME.
  - TIME_INCREMENT.
  - TIME_HEAT_FLUX, specifying "Time integrated heat flux".
  - TIME_HEAT_FLUX_AREA, specifying "Time integrated heat flux per area".
  - TIME_VOLUME, specifying "Time integrated volume".
  - TIME_VOLUME_FLUX, specifying "Time integrated volume flux per area".
  - TWIST.
  - VELOCITY.
  - VELOCITY_SQUARED.
  - VOLUME.
  - VOLUME_FLUX.
  - VOLUME_FLUX_AREA, specifying "Volume flux per area".
  - VOLUME_FRACTION.

  The default value is NONE

### Return value

A QuantityType object.

### Exceptions

None.



## setValues(...)



This method modifies the QuantityType object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [QuantityType ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-quantitytypepyc.htm?ContextScope=all#simaker-quantitytypequantitytypepyc)method.

### Return value

None.

### Exceptions

None.



## Members

The QuantityType object has members with the same names and descriptions as the arguments to the [setValues ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-quantitytypepyc.htm?ContextScope=all#simaker-quantitytypesetvaluespyc)method.