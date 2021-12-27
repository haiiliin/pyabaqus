from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup

# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2021 replay file
# Internal Version: 2020_03_06-22.50.37 167380
# Run by Hailin on Wed Oct 13 16:22:48 2021
#

executeOnCaeStartup()

# TODO CALCULATION METHOD
CALCULATION_METHOD = 'STANDARD'  # OR EXPLICIT

# TODO GEOMETRY
SOIL_LENGTH = 0.025
SOIL_WIDTH = 0.025
SOIL_HEIGHT = 0.025
SOLID_LENGTH = 0.05
SOLID_WIDTH = 0.05
SOLID_HEIGHT = 0.05

# TODO MATERIAL
SOIL_ELASTIC_MODULUS = 4e4
SOIL_POISSON_RATIO = 0.0
SOIL_DENSITY = None
SOLID_ELASTIC_MODULUS = 2e8
SOLID_POISSON_RATIO = 0.0
SOLID_DENSITY = None

# TODO MESH
SOIL_MESH_METHOD = 'NUMBER'  # OR 'SIZE'
SOIL_SEEDS_NUMBER = 2
SOIL_SEEDS_SIZE = 0.01
SOLID_MESH_METHOD = 'NUMBER'
SOLID_SEEDS_NUMBER = 2
SOLID_SEEDS_SIZE = 0.01

# TODO STEP
# INITIAL STRESS
INITIAL_STRESS_TIME_PERIOD = 1.0
INITIAL_STRESS_DESCRIPTION = ''
# GENERAL STATIC STEP
INITIAL_STRESS_INCREMENTATION_TYPE = 'FIXED'
INITIAL_STRESS_MAXIMAL_INCREMENTS = 100
INITIAL_STRESS_INITIAL_INCREMENT_SIZE = 1.0
INITIAL_STRESS_MINIMAL_INCREMENT_SIZE = 1e-5
INITIAL_STRESS_MAXIMAL_INCREMENT_SIZE = 1.0
INITIAL_STRESS_FIXED_INCREMENT_SIZE = 0.2
# EXPLICIT DYNAMIC STEP
INITIAL_STRESS_MAXIMAL_TIME_INCREMENT = 'UNLIMITED'
INITIAL_STRESS_INCREMENT_SIZE = 'ELEMENT_BY_ELEMENT_INCREMENTATION'
INITIAL_STRESS_SCALING_FACTOR = 1.0
INITIAL_STRESS_LINEAR_BULK_VISCOSITY = 0.06
INITIAL_STRESS_QUAD_BULK_VISCOSITY = 1.2

# SHEAR
SHEAR_TIME_PERIOD = 1.0
SHEAR_DESCRIPTION = ''
# GENERAL STATIC STEP
SHEAR_INCREMENTATION_TYPE = 'FIXED'
SHEAR_MAXIMAL_INCREMENTS = 100
SHEAR_INITIAL_INCREMENT_SIZE = 1.0
SHEAR_MINIMAL_INCREMENT_SIZE = 1e-5
SHEAR_MAXIMAL_INCREMENT_SIZE = 1.0
SHEAR_FIXED_INCREMENT_SIZE = 0.2
# EXPLICIT DYNAMIC STEP
SHEAR_MAXIMAL_TIME_INCREMENT = 'UNLIMITED'
SHEAR_INCREMENT_SIZE = 'ELEMENT_BY_ELEMENT_INCREMENTATION'
SHEAR_SCALING_FACTOR = 1.0
SHEAR_LINEAR_BULK_VISCOSITY = 0.06
SHEAR_QUAD_BULK_VISCOSITY = 1.2

# TODO LOAD
RP_DISPLACEMENT = [0.006, 0.0, 0.0, 0.0, 0.0, 0.0]
RP_VELOCITY = [0.006, 0.0, 0.0, 0.0, 0.0, 0.0]
VERTICAL_PRESSURE = 310.0
PREDEFINED_STRESS = [-310.0, -310.0, -310.0, 0.0, 0.0, 0.0]

# TODO CONTACT
# NORMAL CONTACT
normal_contactStiffness = DEFAULT
normal_pressureOverclosure = HARD
normal_allowSeparation = ON
normal_maxStiffness = None
normal_table = ()
normal_constraintEnforcementMethod = DEFAULT
normal_overclosureFactor = 0.0
normal_overclosureMeasure = 0.0
normal_contactStiffnessScaleFactor = 1.0
normal_initialStiffnessScaleFactor = 1.0
normal_clearanceAtZeroContactPressure = 0.0
normal_stiffnessBehavior = LINEAR
normal_stiffnessRatio = 0.01
normal_upperQuadraticFactor = 0.03
normal_lowerQuadraticRatio = 0.3333
# TANGENTIAL CONTACT
tangential_formulation = USER_DEFINED
tangential_directionality = ISOTROPIC
tangential_slipRateDependency = OFF
tangential_pressureDependency = OFF
tangential_temperatureDependency = OFF
tangential_dependencies = 0
tangential_exponentialDecayDefinition = COEFFICIENTS
tangential_table = ((0.0,), (250.0,), (5.19,), (0.89,), (0.147,), (0.424,), (31.2,), (7.57,), (2.06,), (0.46,), (0.5771,), (0.00115,))
tangential_shearStressLimit = None
tangential_maximumElasticSlip = FRACTION
tangential_fraction = 0.0
tangential_absoluteDistance = 0.0
tangential_elasticSlipStiffness = None
tangential_nStateDependentVars = 28
tangential_useProperties = ON

# TODO USER-DEFINED SUBROUTINE
SUBROUTINE = 'FRIC'
SUBROUTINE_PATH = 'FRIC_exponential_CV.for'
N_STATE_DEPENDENT_VARS = 28
FRICTION_PARAMETERS = ((0.0,), (250.0,), (5.19,), (0.89,), (0.147,), (0.424,), (31.2,), (7.57,), (2.06,), (0.46,), (0.5771,), (0.00115,))

# TODO OUTPUT
STANDARD_FREQUENCY = 1
EXPLICIT_NUM_INTERVALS = 50  # FIXME NOT DEFINED
FIELD_OUTPUT_VARIABLES = ['S', 'E', 'LE', 'U', 'RF', 'RT', 'RM', 'P', 'CSTRESS', 'CDISP', 'CFORCE', 'CNAREA', 'CSTATUS']
# FIELD_OUTPUT_VARIABLES = ['S', 'E', 'LE', 'U', 'V', 'A', 'RF', 'P', 'CSTRESS', 'CFORCE', 'FSLIPR', 'FSLIP', 'PPRESS']
HISTORY_OUTPUT_VARIABLES = ['U1', 'RF1']

# TODO WORK DIRECTORY
WORK_DIRECTORY = r'C:\Users\user\OneDrive\Documents\GitHub\PyAbaqusBase\tests'
os.chdir(WORK_DIRECTORY)

# TODO CREATE PARTS
# Soil part
sketch_soil = mdb.models['Model-1'].ConstrainedSketch(name='SKETCH-SOIL', sheetSize=0.1)
sketch_soil.rectangle(point1=(0.0, 0.0), point2=(SOIL_LENGTH, SOIL_WIDTH))
mdb.models['Model-1'].Part(name='PART-SOIL', dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['PART-SOIL'].BaseSolidExtrude(sketch=sketch_soil, depth=SOIL_HEIGHT)
del mdb.models['Model-1'].sketches['SKETCH-SOIL']
# Solid part
sketch_solid = mdb.models['Model-1'].ConstrainedSketch(name='SKETCH-SOLID', sheetSize=0.1)
sketch_solid.rectangle(point1=(0.0, 0.0), point2=(SOLID_LENGTH, SOLID_WIDTH))
mdb.models['Model-1'].Part(name='PART-SOLID', dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['PART-SOLID'].BaseSolidExtrude(sketch=sketch_solid, depth=SOLID_HEIGHT)
del mdb.models['Model-1'].sketches['SKETCH-SOLID']

# TODO ASSEMBLY INSTANCE
assembly = mdb.models['Model-1'].rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
assembly.Instance(name='INSTANCE-SOIL', part=mdb.models['Model-1'].parts['PART-SOIL'], dependent=ON)
assembly.Instance(name='INSTANCE-SOLID', part=mdb.models['Model-1'].parts['PART-SOLID'], dependent=ON)
assembly.translate(instanceList=('INSTANCE-SOIL',), vector=((SOLID_LENGTH - SOIL_LENGTH) / 2,
                                                            (SOLID_WIDTH - SOIL_WIDTH) / 2,
                                                            SOLID_HEIGHT))

# TODO SETS
# Sets of the soil
part_soil = mdb.models['Model-1'].parts['PART-SOIL']
part_soil.Surface(side1Faces=part_soil.faces.findAt(((SOIL_LENGTH / 2, SOIL_WIDTH / 2, 0),), ), name='SURFACE-SOIL-Z0')
part_soil.Surface(side1Faces=part_soil.faces.findAt(((SOIL_LENGTH / 2, SOIL_WIDTH / 2, SOIL_HEIGHT),), ),
                  name='SURFACE-SOIL-Z1')

part_soil.Set(cells=part_soil.cells.findAt(((SOIL_LENGTH / 2, SOIL_WIDTH / 2, SOIL_HEIGHT / 2),), ), name='SET-SOIL')

part_soil.Set(faces=part_soil.faces.findAt(((0, SOIL_WIDTH / 2, SOIL_HEIGHT / 2),), ), name='SET-SOIL-X0')
part_soil.Set(faces=part_soil.faces.findAt(((SOIL_LENGTH / 2, 0, SOIL_HEIGHT / 2),), ), name='SET-SOIL-Y0')
part_soil.Set(faces=part_soil.faces.findAt(((SOIL_LENGTH / 2, SOIL_WIDTH / 2, 0),), ), name='SET-SOIL-Z0')

part_soil.Set(faces=part_soil.faces.findAt(((SOIL_LENGTH, SOIL_WIDTH / 2, SOIL_HEIGHT / 2),), ), name='SET-SOIL-X1')
part_soil.Set(faces=part_soil.faces.findAt(((SOIL_LENGTH / 2, SOIL_WIDTH, SOIL_HEIGHT / 2),), ), name='SET-SOIL-Y1')
part_soil.Set(faces=part_soil.faces.findAt(((SOIL_LENGTH / 2, SOIL_WIDTH / 2, SOIL_HEIGHT),), ), name='SET-SOIL-Z1')

# Sets of the solid
part_solid = mdb.models['Model-1'].parts['PART-SOLID']
part_solid.Surface(side1Faces=part_solid.faces.findAt(((SOLID_LENGTH / 2, SOLID_WIDTH / 2, 0),), ),
                   name='SURFACE-SOLID-Z0')
part_solid.Surface(side1Faces=part_solid.faces.findAt(((SOLID_LENGTH / 2, SOLID_WIDTH / 2, SOLID_HEIGHT),), ),
                   name='SURFACE-SOLID-Z1')

part_solid.Set(cells=part_solid.cells.findAt(((SOLID_LENGTH / 2, SOLID_WIDTH / 2, SOLID_HEIGHT / 2),), ),
               name='SET-SOLID')

part_solid.Set(faces=part_solid.faces.findAt(((0, SOLID_WIDTH / 2, SOLID_HEIGHT / 2),), ), name='SET-SOLID-X0')
part_solid.Set(faces=part_solid.faces.findAt(((SOLID_LENGTH / 2, 0, SOLID_HEIGHT / 2),), ), name='SET-SOLID-Y0')
part_solid.Set(faces=part_solid.faces.findAt(((SOLID_LENGTH / 2, SOLID_WIDTH / 2, 0),), ), name='SET-SOLID-Z0')

part_solid.Set(faces=part_solid.faces.findAt(((SOLID_LENGTH, SOLID_WIDTH / 2, SOLID_HEIGHT / 2),), ),
               name='SET-SOLID-X1')
part_solid.Set(faces=part_solid.faces.findAt(((SOLID_LENGTH / 2, SOLID_WIDTH, SOLID_HEIGHT / 2),), ),
               name='SET-SOLID-Y1')
part_solid.Set(faces=part_solid.faces.findAt(((SOLID_LENGTH / 2, SOLID_WIDTH / 2, SOLID_HEIGHT),), ),
               name='SET-SOLID-Z1')

# TODO MATERIAL
# Materials
mdb.models['Model-1'].Material(name='MATERIAL-SOIL')
mdb.models['Model-1'].materials['MATERIAL-SOIL'].Elastic(table=((SOIL_ELASTIC_MODULUS, SOIL_POISSON_RATIO),))
if SOIL_DENSITY is not None:
    mdb.models['Model-1'].materials['MATERIAL-SOIL'].Density(table=((SOIL_DENSITY,),))
mdb.models['Model-1'].Material(name='MATERIAL-SOLID')
mdb.models['Model-1'].materials['MATERIAL-SOLID'].Elastic(table=((SOLID_ELASTIC_MODULUS, SOLID_POISSON_RATIO),))
if SOLID_DENSITY is not None:
    mdb.models['Model-1'].materials['MATERIAL-SOLID'].Density(table=((SOLID_DENSITY,),))

# Sections
mdb.models['Model-1'].HomogeneousSolidSection(name='SECTION-SOIL', material='MATERIAL-SOIL', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(name='SECTION-SOLID', material='MATERIAL-SOLID', thickness=None)

# Sections assignment
part_soil = mdb.models['Model-1'].parts['PART-SOIL']
part_soil.SectionAssignment(region=part_soil.sets['SET-SOIL'], sectionName='SECTION-SOIL', offset=0.0,
                            offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
part_solid = mdb.models['Model-1'].parts['PART-SOLID']
part_solid.SectionAssignment(region=part_solid.sets['SET-SOLID'], sectionName='SECTION-SOLID', offset=0.0,
                             offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)

# TODO STEP
if CALCULATION_METHOD == 'STANDARD':
    mdb.models['Model-1'].StaticStep(name='INITIAL-STRESS', previous='Initial',
                                     maxNumInc=INITIAL_STRESS_MAXIMAL_INCREMENTS,
                                     initialInc=INITIAL_STRESS_INITIAL_INCREMENT_SIZE,
                                     minInc=INITIAL_STRESS_MINIMAL_INCREMENT_SIZE,
                                     maxInc=INITIAL_STRESS_MAXIMAL_INCREMENT_SIZE,
                                     matrixSolver=DIRECT, matrixStorage=UNSYMMETRIC)
    mdb.models['Model-1'].StaticStep(name='SHEAR', previous='INITIAL-STRESS',
                                     maxNumInc=SHEAR_MAXIMAL_INCREMENTS,
                                     initialInc=SHEAR_INITIAL_INCREMENT_SIZE,
                                     minInc=SHEAR_MINIMAL_INCREMENT_SIZE,
                                     maxInc=SHEAR_MAXIMAL_INCREMENT_SIZE,
                                     matrixSolver=DIRECT, matrixStorage=UNSYMMETRIC)
else:
    if INITIAL_STRESS_INCREMENTATION_TYPE == 'AUTOMATIC':
        if INITIAL_STRESS_MAXIMAL_TIME_INCREMENT == 'UNLIMITED':
            mdb.models['Model-1'].ExplicitDynamicsStep(name='INITIAL-STRESS', previous='Initial',
                                                       timePeriod=INITIAL_STRESS_TIME_PERIOD,
                                                       linearBulkViscosity=INITIAL_STRESS_LINEAR_BULK_VISCOSITY,
                                                       quadBulkViscosity=INITIAL_STRESS_QUAD_BULK_VISCOSITY,
                                                       improvedDtMethod=ON,
                                                       timeIncrementationMethod=AUTOMATIC_GLOBAL)
        else:
            mdb.models['Model-1'].ExplicitDynamicsStep(name='INITIAL-STRESS', previous='Initial',
                                                       timePeriod=INITIAL_STRESS_TIME_PERIOD,
                                                       linearBulkViscosity=INITIAL_STRESS_LINEAR_BULK_VISCOSITY,
                                                       quadBulkViscosity=INITIAL_STRESS_QUAD_BULK_VISCOSITY,
                                                       improvedDtMethod=ON,
                                                       maxIncrement=INITIAL_STRESS_MAXIMAL_TIME_INCREMENT,
                                                       timeIncrementationMethod=AUTOMATIC_GLOBAL)
    else:
        if INITIAL_STRESS_INCREMENT_SIZE == 'ELEMENT_BY_ELEMENT_INCREMENTATION':
            mdb.models['Model-1'].ExplicitDynamicsStep(name='INITIAL-STRESS', previous='Initial',
                                                       timePeriod=INITIAL_STRESS_TIME_PERIOD,
                                                       linearBulkViscosity=INITIAL_STRESS_LINEAR_BULK_VISCOSITY,
                                                       quadBulkViscosity=INITIAL_STRESS_QUAD_BULK_VISCOSITY,
                                                       improvedDtMethod=ON,
                                                       timeIncrementationMethod=FIXED_EBE)
        else:
            mdb.models['Model-1'].ExplicitDynamicsStep(name='INITIAL-STRESS', previous='Initial',
                                                       timePeriod=INITIAL_STRESS_TIME_PERIOD,
                                                       linearBulkViscosity=INITIAL_STRESS_LINEAR_BULK_VISCOSITY,
                                                       quadBulkViscosity=INITIAL_STRESS_QUAD_BULK_VISCOSITY,
                                                       improvedDtMethod=ON,
                                                       timeIncrementationMethod=FIXED_USER_DEFINED_INC,
                                                       userDefinedInc=INITIAL_STRESS_INCREMENT_SIZE)
    if SHEAR_INCREMENTATION_TYPE == 'AUTOMATIC':
        if SHEAR_MAXIMAL_TIME_INCREMENT == 'UNLIMITED':
            mdb.models['Model-1'].ExplicitDynamicsStep(name='SHEAR', previous='INITIAL-STRESS',
                                                       timePeriod=SHEAR_TIME_PERIOD,
                                                       linearBulkViscosity=SHEAR_LINEAR_BULK_VISCOSITY,
                                                       quadBulkViscosity=SHEAR_QUAD_BULK_VISCOSITY, improvedDtMethod=ON,
                                                       timeIncrementationMethod=AUTOMATIC_GLOBAL)
        else:
            mdb.models['Model-1'].ExplicitDynamicsStep(name='SHEAR', previous='INITIAL-STRESS',
                                                       timePeriod=SHEAR_TIME_PERIOD,
                                                       linearBulkViscosity=SHEAR_LINEAR_BULK_VISCOSITY,
                                                       quadBulkViscosity=SHEAR_QUAD_BULK_VISCOSITY, improvedDtMethod=ON,
                                                       maxIncrement=SHEAR_MAXIMAL_TIME_INCREMENT,
                                                       timeIncrementationMethod=AUTOMATIC_GLOBAL)
    else:
        if SHEAR_INCREMENT_SIZE == 'ELEMENT_BY_ELEMENT_INCREMENTATION':
            mdb.models['Model-1'].ExplicitDynamicsStep(name='SHEAR', previous='INITIAL-STRESS',
                                                       timePeriod=SHEAR_TIME_PERIOD,
                                                       linearBulkViscosity=SHEAR_LINEAR_BULK_VISCOSITY,
                                                       quadBulkViscosity=SHEAR_QUAD_BULK_VISCOSITY, improvedDtMethod=ON,
                                                       timeIncrementationMethod=FIXED_EBE)
        else:
            mdb.models['Model-1'].ExplicitDynamicsStep(name='SHEAR', previous='INITIAL-STRESS',
                                                       timePeriod=SHEAR_TIME_PERIOD,
                                                       linearBulkViscosity=SHEAR_LINEAR_BULK_VISCOSITY,
                                                       quadBulkViscosity=SHEAR_QUAD_BULK_VISCOSITY, improvedDtMethod=ON,
                                                       timeIncrementationMethod=FIXED_USER_DEFINED_INC,
                                                       userDefinedInc=SHEAR_INCREMENT_SIZE)

# TODO CONTACT
# Contact property
mdb.models['Model-1'].ContactProperty('IntProp-1')
"""mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(pressureOverclosure=HARD, allowSeparation=ON,
                                                                        constraintEnforcementMethod=DEFAULT)
mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
    formulation=USER_DEFINED, nStateDependentVars=N_STATE_DEPENDENT_VARS,
    useProperties=ON, table=FRICTION_PARAMETERS)"""

if normal_pressureOverclosure == HARD:
    mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(
        pressureOverclosure=HARD,
        allowSeparation=normal_allowSeparation,
        constraintEnforcementMethod=normal_constraintEnforcementMethod)

elif normal_pressureOverclosure == EXPONENTIAL:
    mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(
        pressureOverclosure=EXPONENTIAL,
        table=normal_table,
        maxStiffness=normal_maxStiffness,
        constraintEnforcementMethod=normal_constraintEnforcementMethod)

elif normal_pressureOverclosure == LINEAR:
    mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(
        pressureOverclosure=LINEAR,
        contactStiffness=normal_contactStiffness,
        constraintEnforcementMethod=normal_constraintEnforcementMethod)

elif normal_pressureOverclosure == TABULAR:
    mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(
        pressureOverclosure=TABULAR,
        table=normal_table,
        constraintEnforcementMethod=normal_constraintEnforcementMethod)

else:  # SCALE_FACTOR
    mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(
        pressureOverclosure=SCALE_FACTOR,
        contactStiffnessScaleFactor=normal_contactStiffnessScaleFactor,
        initialStiffnessScaleFactor=normal_initialStiffnessScaleFactor,
        overclosureFactor=normal_overclosureFactor,
        overclosureMeasure=normal_overclosureMeasure,
        constraintEnforcementMethod=normal_constraintEnforcementMethod)

if tangential_formulation == FRICTIONLESS:
    mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
        formulation=FRICTIONLESS)

elif tangential_formulation == PENALTY:
    mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
        formulation=PENALTY,
        directionality=tangential_directionality,
        slipRateDependency=tangential_slipRateDependency,
        pressureDependency=tangential_pressureDependency,
        temperatureDependency=tangential_temperatureDependency,
        dependencies=tangential_dependencies,
        table=tangential_table,
        shearStressLimit=tangential_shearStressLimit,
        maximumElasticSlip=tangential_maximumElasticSlip,
        fraction=tangential_fraction,
        absoluteDistance=tangential_absoluteDistance,
        elasticSlipStiffness=tangential_elasticSlipStiffness)

elif tangential_formulation == EXPONENTIAL_DECAY:
    mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
        formulation=EXPONENTIAL_DECAY,
        exponentialDecayDefinition=tangential_exponentialDecayDefinition,
        table=tangential_table,
        maximumElasticSlip=tangential_maximumElasticSlip,
        fraction=tangential_fraction,
        absoluteDistance=tangential_absoluteDistance,
        elasticSlipStiffness=tangential_elasticSlipStiffness)

elif tangential_formulation == ROUGH:
    mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
        formulation=ROUGH)

elif tangential_formulation == LAGRANGE:
    mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
        formulation=LAGRANGE, directionality=tangential_directionality,
        slipRateDependency=tangential_slipRateDependency,
        pressureDependency=tangential_pressureDependency,
        temperatureDependency=tangential_temperatureDependency,
        dependencies=tangential_dependencies,
        table=tangential_table,
        shearStressLimit=tangential_shearStressLimit)
else:  # USER_DEFINED
    mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
        formulation=USER_DEFINED,
        nStateDependentVars=tangential_nStateDependentVars,
        useProperties=tangential_useProperties,
        table=tangential_table)


# Contact assignment
assembly = mdb.models['Model-1'].rootAssembly
region_solid = assembly.instances['INSTANCE-SOLID'].surfaces['SURFACE-SOLID-Z1']
region_soil = assembly.instances['INSTANCE-SOIL'].surfaces['SURFACE-SOIL-Z0']
if CALCULATION_METHOD == 'STANDARD':
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Int-1', createStepName='Initial', master=region_solid,
                                                     slave=region_soil, sliding=FINITE, thickness=ON,
                                                     interactionProperty='IntProp-1', adjustMethod=NONE,
                                                     initialClearance=OMIT, datumAxis=None, clearanceRegion=None)
else:  # EXPLICIT
    mdb.models['Model-1'].SurfaceToSurfaceContactExp(name='Int-1', createStepName='Initial', master=region_solid,
                                                     slave=region_soil, sliding=FINITE, initialClearance=OMIT,
                                                     interactionProperty='IntProp-1', datumAxis=None,
                                                     clearanceRegion=None,
                                                     mechanicalConstraint=KINEMATIC)

# TODO LOAD
# Vertical pressure
region_pressure = mdb.models['Model-1'].rootAssembly.instances['INSTANCE-SOIL'].surfaces['SURFACE-SOIL-Z1']
mdb.models['Model-1'].Pressure(name='SOIL-VERTICAL-PRESSURE', createStepName='INITIAL-STRESS', region=region_pressure,
                               distributionType=UNIFORM, field='', magnitude=VERTICAL_PRESSURE, amplitude=UNSET)
# Predefined stress
region_predefined_stress = mdb.models['Model-1'].rootAssembly.instances['INSTANCE-SOIL'].sets['SET-SOIL']
mdb.models['Model-1'].Stress(name='SOIL-PREDEFINED-STRESS', region=region_predefined_stress, distributionType=UNIFORM,
                             sigma11=PREDEFINED_STRESS[0], sigma22=PREDEFINED_STRESS[1], sigma33=PREDEFINED_STRESS[2],
                             sigma12=PREDEFINED_STRESS[3], sigma13=PREDEFINED_STRESS[4], sigma23=PREDEFINED_STRESS[5])

# Confining pressure
# Reference point
mdb.models['Model-1'].parts['PART-SOLID'].ReferencePoint(point=(0.0, 0.0, 0.0))
RP = mdb.models['Model-1'].parts['PART-SOLID'].referencePoints[11]
mdb.models['Model-1'].parts['PART-SOLID'].Set(referencePoints=(RP,), name='SET-RP')

# Rigid body
region1 = mdb.models['Model-1'].rootAssembly.instances['INSTANCE-SOLID'].sets['SET-RP']
region2 = mdb.models['Model-1'].rootAssembly.instances['INSTANCE-SOLID'].sets['SET-SOLID']
mdb.models['Model-1'].RigidBody(name='CONSTRAINT-SOLID', refPointRegion=region1, bodyRegion=region2)

# BC-RP INITIAL: FIXED; SHEAR: U1 = 0.006
region_RP = mdb.models['Model-1'].rootAssembly.instances['INSTANCE-SOLID'].sets['SET-RP']
if CALCULATION_METHOD == 'STANDARD':
    mdb.models['Model-1'].DisplacementBC(name='BC-RP', createStepName='Initial',
                                         region=region_RP, u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET,
                                         amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
    mdb.models['Model-1'].boundaryConditions['BC-RP'].setValuesInStep(
        stepName='SHEAR', u1=RP_DISPLACEMENT[0], u2=RP_DISPLACEMENT[1], u3=RP_DISPLACEMENT[2],
        ur1=RP_DISPLACEMENT[3], ur2=RP_DISPLACEMENT[4], ur3=RP_DISPLACEMENT[5])
else:
    mdb.models['Model-1'].VelocityBC(name='BC-RP', createStepName='Initial',
                                     region=region_RP, v1=SET, v2=SET, v3=SET, vr1=SET, vr2=SET, vr3=SET,
                                     amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
    mdb.models['Model-1'].boundaryConditions['BC-RP'].setValuesInStep(
        stepName='SHEAR', v1=RP_VELOCITY[0], v2=RP_VELOCITY[1], v3=RP_VELOCITY[2],
        vr1=RP_VELOCITY[3], vr2=RP_VELOCITY[4], vr3=RP_VELOCITY[5])

# BC-SOIL-X0 INITIAL: U1 = 0
assembly = mdb.models['Model-1'].rootAssembly
region_X0 = assembly.instances['INSTANCE-SOIL'].sets['SET-SOIL-X0']
if CALCULATION_METHOD == 'STANDARD':
    mdb.models['Model-1'].DisplacementBC(name='BC-SOIL-X0', createStepName='Initial',
                                         region=region_X0, u1=0.0, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET,
                                         amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='',
                                         localCsys=None)
else:
    mdb.models['Model-1'].VelocityBC(name='BC-SOIL-X0', createStepName='Initial',
                                     region=region_X0, v1=0.0, v2=UNSET, v3=UNSET, vr1=UNSET, vr2=UNSET, vr3=UNSET,
                                     amplitude=UNSET, distributionType=UNIFORM, fieldName='',
                                     localCsys=None)

# BC-SOIL-X1 INITIAL: U1 = 0
region_X1 = assembly.instances['INSTANCE-SOIL'].sets['SET-SOIL-X1']
if CALCULATION_METHOD == 'STANDARD':
    mdb.models['Model-1'].DisplacementBC(name='BC-SOIL-X1', createStepName='Initial',
                                         region=region_X1, u1=0.0, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET,
                                         amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='',
                                         localCsys=None)
else:
    mdb.models['Model-1'].VelocityBC(name='BC-SOIL-X1', createStepName='Initial',
                                     region=region_X1, v1=0.0, v2=UNSET, v3=UNSET, vr1=UNSET, vr2=UNSET, vr3=UNSET,
                                     amplitude=UNSET, distributionType=UNIFORM, fieldName='',
                                     localCsys=None)

# BC-SOIL-Y0 INITIAL: U2 = 0
region_Y0 = assembly.instances['INSTANCE-SOIL'].sets['SET-SOIL-Y0']
if CALCULATION_METHOD == 'STANDARD':
    mdb.models['Model-1'].DisplacementBC(name='BC-SOIL-Y0', createStepName='Initial',
                                         region=region_Y0, u1=UNSET, u2=0.0, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET,
                                         amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='',
                                         localCsys=None)
else:
    mdb.models['Model-1'].VelocityBC(name='BC-SOIL-Y0', createStepName='Initial',
                                     region=region_Y0, v1=UNSET, v2=0.0, v3=UNSET, vr1=UNSET, vr2=UNSET, vr3=UNSET,
                                     amplitude=UNSET, distributionType=UNIFORM, fieldName='',
                                     localCsys=None)

# BC-SOIL-Y1 INITIAL: U2 = 0
region_Y1 = assembly.instances['INSTANCE-SOIL'].sets['SET-SOIL-Y1']
if CALCULATION_METHOD == 'STANDARD':
    mdb.models['Model-1'].DisplacementBC(name='BC-SOIL-Y1', createStepName='Initial',
                                         region=region_Y1, u1=UNSET, u2=0.0, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET,
                                         amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='',
                                         localCsys=None)
else:
    mdb.models['Model-1'].VelocityBC(name='BC-SOIL-Y1', createStepName='Initial',
                                     region=region_Y1, v1=UNSET, v2=0.0, v3=UNSET, vr1=UNSET, vr2=UNSET, vr3=UNSET,
                                     amplitude=UNSET, distributionType=UNIFORM, fieldName='',
                                     localCsys=None)

# TODO MESH
# Element type
# Mesh soil
elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, kinematicSplit=AVERAGE_STRAIN,
                          secondOrderAccuracy=OFF, hourglassControl=ENHANCED, distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)

p = mdb.models['Model-1'].parts['PART-SOIL']
cells = p.cells.findAt(((SOIL_LENGTH / 2, SOIL_WIDTH / 2, SOIL_HEIGHT / 2),), )
p.setElementType(regions=(cells,), elemTypes=(elemType1, elemType2, elemType3))

if SOIL_MESH_METHOD == 'SIZE':
    p.seedPart(size=SOIL_SEEDS_SIZE, deviationFactor=0.1, minSizeFactor=0.1)
else:
    p.seedEdgeByNumber(edges=p.edges, number=SOIL_SEEDS_NUMBER, constraint=FINER)

mdb.models['Model-1'].parts['PART-SOIL'].generateMesh()

# Mesh solid
if CALCULATION_METHOD == 'STANDARD':
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, kinematicSplit=AVERAGE_STRAIN,
                              secondOrderAccuracy=OFF, hourglassControl=ENHANCED, distortionControl=DEFAULT)
else:
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, kinematicSplit=AVERAGE_STRAIN,
                              secondOrderAccuracy=OFF, hourglassControl=RELAX_STIFFNESS, distortionControl=DEFAULT)

elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['PART-SOLID']
cells = p.cells.findAt(((SOLID_LENGTH / 2, SOLID_WIDTH / 2, SOLID_HEIGHT / 2),), )
p.setElementType(regions=(cells,), elemTypes=(elemType1, elemType2, elemType3))

if SOLID_MESH_METHOD == 'SIZE':
    p.seedPart(size=SOLID_SEEDS_SIZE, deviationFactor=0.1, minSizeFactor=0.1)
else:
    p.seedEdgeByNumber(edges=p.edges, number=SOLID_SEEDS_NUMBER, constraint=FINER)

mdb.models['Model-1'].parts['PART-SOLID'].generateMesh()

# TODO FIELD OUTPUT REQUEST FIXME Modify the input file to add SDV variable of the contact
if CALCULATION_METHOD == 'STANDARD':
    mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(
        variables=tuple(FIELD_OUTPUT_VARIABLES),
        frequency=STANDARD_FREQUENCY)
else:  # EXPLICIT
    mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(
        variables=tuple(FIELD_OUTPUT_VARIABLES),
        numIntervals=EXPLICIT_NUM_INTERVALS)
    pass

# TODO HISTORY OUTPUT REQUEST
regionDef = mdb.models['Model-1'].rootAssembly.allInstances['INSTANCE-SOLID'].sets['SET-RP']
mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-1', createStepName='SHEAR',
                                           variables=tuple(HISTORY_OUTPUT_VARIABLES), region=regionDef,
                                           sectionPoints=DEFAULT, rebar=EXCLUDE)

# TODO JOB
mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS,
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
        explicitPrecision=DOUBLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF,
        userSubroutine=SUBROUTINE_PATH,
        scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1,
        numGPUs=0)

# TODO MODIFY INPUT FILE: ADD SDV OUTPUT VARIABLES
if CALCULATION_METHOD == 'STANDARD':
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(101, """
    *Contact Output
    CDISP, CFORCE, CNAREA, CSTATUS, CSTRESS, SDV""")
    mdb.models['Model-1'].keywordBlock.replace(115, """
    *Contact Output
    CDISP, CFORCE, CNAREA, CSTATUS, CSTRESS, SDV""")
else:  # EXPLICIT
    pass

# TODO WRITE INPUT FILE
mdb.jobs['Job-1'].writeInput()

# TODO SAVE CAE MODEL TO FILE
mdb.saveAs(pathName='dst.cae')

# TODO SUBMIT JOB
# mdb.jobs['Job-1'].submit(consistencyChecking=OFF)

# OPEN OUTPUT DATABASE FILE
# mdb.jobs['Job-1'].waitForCompletion()
# odb = session.openOdb(name=os.path.join(WORK_DIRECTORY, 'Job-1.odb'))
# session.viewports['Viewport: 1'].setValues(displayedObject=odb)
