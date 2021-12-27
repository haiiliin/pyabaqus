from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup

# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2021 replay file
# Internal Version: 2020_03_06-22.50.37 167380
# Run by Hailin on Wed Oct 27 16:22:48 2021
#

executeOnCaeStartup()

# TODO CALCULATION METHOD
CALCULATION_METHOD = 'STANDARD'  # OR EXPLICIT

# TODO GEOMETRY
# SOIL_LENGTH = 0.025
# SOIL_WIDTH = 0.025
# SOIL_HEIGHT = 0.025
# SOLID_LENGTH = 0.05
# SOLID_WIDTH = 0.05
# SOLID_HEIGHT = 0.05
NAIL_RADIUS = 0.05
NAIL_LENGTH = 1.2
SOIL_LENGTH = 1.0
SOIL_WIDTH = 0.3
SOIL_HEIGHT = 0.8
SOIL_NAIL_OFFSET_HEIGHT = SOIL_HEIGHT / 2

# TODO MATERIAL
SOIL_ELASTIC_MODULUS = 4e4
SOIL_POISSON_RATIO = 0.3
SOIL_DENSITY = None
SOIL_MOHR_COULOMB_FRICTION_ANGLE = 30
SOIL_MOHR_COULOMB_DILATION_ANGLE = 3
SOIL_MOHR_COULOMB_COHESION_YIELD_STRESS = 5
SOIL_MOHR_COULOMB_ABS_PLASTIC_STRAIN = 0
NAIL_ELASTIC_MODULUS = 3.2e7
MAIL_POISSON_RATIO = 0.2
NAIL_DENSITY = None

# TODO MESH FIXME
SOIL_MESH_METHOD = 'SIZE'  # OR 'SIZE'
SOIL_SEEDS_GENERAL_NUMBER = 12
SOIL_SEEDS_DENSE_NUMBER = 6
SOIL_SEEDS_GENERAL_SIZE = 0.025
SOIL_SEEDS_DENSE_SIZE = 0.01

NAIL_MESH_METHOD = 'SIZE'
NAIL_SEEDS_GENERAL_NUMBER = 12
NAIL_SEEDS_DENSE_NUMBER = 12
NAIL_SEEDS_GENERAL_SIZE = 0.025
NAIL_SEEDS_DENSE_SIZE = 0.01

# TODO STEP FIXME
# INITIAL STRESS
INITIAL_STRESS_TIME_PERIOD = 1.0
INITIAL_STRESS_DESCRIPTION = ''
# GENERAL STATIC STEP
INITIAL_STRESS_INCREMENTATION_TYPE = 'FIXED'
INITIAL_STRESS_MAXIMAL_INCREMENTS = 100
INITIAL_STRESS_INITIAL_INCREMENT_SIZE = 0.01
INITIAL_STRESS_MINIMAL_INCREMENT_SIZE = 1e-5
INITIAL_STRESS_MAXIMAL_INCREMENT_SIZE = 0.1
INITIAL_STRESS_FIXED_INCREMENT_SIZE = 0.2
# EXPLICIT DYNAMIC STEP
INITIAL_STRESS_MAXIMAL_TIME_INCREMENT = 'UNLIMITED'
INITIAL_STRESS_INCREMENT_SIZE = 'ELEMENT_BY_ELEMENT_INCREMENTATION'
INITIAL_STRESS_SCALING_FACTOR = 1.0
INITIAL_STRESS_LINEAR_BULK_VISCOSITY = 0.06
INITIAL_STRESS_QUAD_BULK_VISCOSITY = 1.2

# SHEAR -> PULLOUT
PULLOUT_TIME_PERIOD = 1.0
PULLOUT_DESCRIPTION = ''
# GENERAL STATIC STEP
PULLOUT_INCREMENTATION_TYPE = 'FIXED'
PULLOUT_MAXIMAL_INCREMENTS = 100
PULLOUT_INITIAL_INCREMENT_SIZE = 1e-6
PULLOUT_MINIMAL_INCREMENT_SIZE = 1e-9
PULLOUT_MAXIMAL_INCREMENT_SIZE = 0.01
PULLOUT_FIXED_INCREMENT_SIZE = 0.2
# EXPLICIT DYNAMIC STEP
PULLOUT_MAXIMAL_TIME_INCREMENT = 'UNLIMITED'
PULLOUT_INCREMENT_SIZE = 'ELEMENT_BY_ELEMENT_INCREMENTATION'
PULLOUT_SCALING_FACTOR = 1.0
PULLOUT_LINEAR_BULK_VISCOSITY = 0.06
PULLOUT_QUAD_BULK_VISCOSITY = 1.2

# TODO LOAD FIXME
RP_DISPLACEMENT = [0.0, 0.0, 0.008, 0.0, 0.0, 0.0]
RP_VELOCITY = [0.0, 0.0, 0.008, 0.0, 0.0, 0.0]
VERTICAL_PRESSURE = 300.0
PREDEFINED_STRESS = [-300.0, -300.0, -300.0, 0.0, 0.0, 0.0]

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
# N_STATE_DEPENDENT_VARS = 28
# ((0.0,), (250.0,), (5.19,), (0.89,), (0.147,), (0.424,), (31.2,), (0.1,), (0.1,), (0.1,), (0.7,), (0.00115,))
# FRICTION_PARAMETERS = ((0.0,), (250.0,), (5.19,), (0.89,), (0.147,), (0.424,), (31.2,), (0.1,), (0.1,), (0.1,), (0.7,), (0.00115,))

# TODO OUTPUT FIXME
STANDARD_FREQUENCY = 1
EXPLICIT_NUM_INTERVALS = 50
FIELD_OUTPUT_VARIABLES = ['S', 'E', 'LE', 'U', 'RF', 'RT', 'RM', 'P', 'CSTRESS', 'CDISP', 'CFORCE', 'CNAREA', 'CSTATUS']
# FIELD_OUTPUT_VARIABLES = ['S', 'E', 'LE', 'U', 'V', 'A', 'RF', 'P', 'CSTRESS', 'CFORCE', 'FSLIPR', 'FSLIP', 'PPRESS']
HISTORY_OUTPUT_VARIABLES = ['U1', 'RF1']

# TODO WORK DIRECTORY
WORK_DIRECTORY = r'C:\Users\user\OneDrive\Documents\GitHub\CH-Model\CH_model_Python\SSI\Abaqus\DirectShear\abageotests\abapullout\pullout_abaqus'
os.chdir(WORK_DIRECTORY)

# TODO CREATE PARTS
mdb.models['Model-1'].ConstrainedSketch(name='SKETCH-NAIL', sheetSize=NAIL_LENGTH)
mdb.models['Model-1'].sketches['SKETCH-NAIL'].ArcByCenterEnds(center=(0.0, 0.0), direction=CLOCKWISE,
                                                              point1=(-NAIL_RADIUS, 0.0), point2=(NAIL_RADIUS, 0.0))
mdb.models['Model-1'].sketches['SKETCH-NAIL'].Line(point1=(NAIL_RADIUS, 0.0), point2=(-NAIL_RADIUS, 0.0))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='PART-NAIL', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['PART-NAIL'].BaseSolidExtrude(depth=NAIL_LENGTH,
                                                          sketch=mdb.models['Model-1'].sketches['SKETCH-NAIL'])
del mdb.models['Model-1'].sketches['SKETCH-NAIL']
mdb.models['Model-1'].ConstrainedSketch(name='SKETCH-SOIL', sheetSize=1.0)
mdb.models['Model-1'].sketches['SKETCH-SOIL'].Line(point1=(-NAIL_RADIUS, 0.0),
                                                   point2=(-NAIL_RADIUS * 2, 0.0))
mdb.models['Model-1'].sketches['SKETCH-SOIL'].Line(point1=(-NAIL_RADIUS * 2, 0.0),
                                                   point2=(-SOIL_HEIGHT + SOIL_NAIL_OFFSET_HEIGHT, 0.0))
mdb.models['Model-1'].sketches['SKETCH-SOIL'].Line(point1=(-SOIL_HEIGHT + SOIL_NAIL_OFFSET_HEIGHT, 0.0),
                                                   point2=(-SOIL_HEIGHT + SOIL_NAIL_OFFSET_HEIGHT, NAIL_RADIUS * 2))
mdb.models['Model-1'].sketches['SKETCH-SOIL'].Line(point1=(-SOIL_HEIGHT + SOIL_NAIL_OFFSET_HEIGHT, NAIL_RADIUS * 2),
                                                   point2=(-SOIL_HEIGHT + SOIL_NAIL_OFFSET_HEIGHT, SOIL_WIDTH))
mdb.models['Model-1'].sketches['SKETCH-SOIL'].Line(point1=(-SOIL_HEIGHT + SOIL_NAIL_OFFSET_HEIGHT, SOIL_WIDTH),
                                                   point2=(-NAIL_RADIUS * 2, SOIL_WIDTH))
mdb.models['Model-1'].sketches['SKETCH-SOIL'].Line(point1=(-NAIL_RADIUS * 2, SOIL_WIDTH),
                                                   point2=(NAIL_RADIUS * 2, SOIL_WIDTH))
mdb.models['Model-1'].sketches['SKETCH-SOIL'].Line(point1=(NAIL_RADIUS * 2, SOIL_WIDTH),
                                                   point2=(SOIL_NAIL_OFFSET_HEIGHT, SOIL_WIDTH))
mdb.models['Model-1'].sketches['SKETCH-SOIL'].Line(point1=(SOIL_NAIL_OFFSET_HEIGHT, SOIL_WIDTH),
                                                   point2=(SOIL_NAIL_OFFSET_HEIGHT, NAIL_RADIUS * 2))
mdb.models['Model-1'].sketches['SKETCH-SOIL'].Line(point1=(SOIL_NAIL_OFFSET_HEIGHT, NAIL_RADIUS * 2),
                                                   point2=(SOIL_NAIL_OFFSET_HEIGHT, 0.0))
mdb.models['Model-1'].sketches['SKETCH-SOIL'].Line(point1=(SOIL_NAIL_OFFSET_HEIGHT, 0.0),
                                                   point2=(NAIL_RADIUS * 2, 0.0))
mdb.models['Model-1'].sketches['SKETCH-SOIL'].Line(point1=(NAIL_RADIUS * 2, 0.0),
                                                   point2=(NAIL_RADIUS, 0.0))
mdb.models['Model-1'].sketches['SKETCH-SOIL'].ArcByCenterEnds(center=(0.0, 0.0), direction=CLOCKWISE,
                                                              point1=(-NAIL_RADIUS, 0.0), point2=(NAIL_RADIUS, 0.0))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='PART-SOIL', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['PART-SOIL'].BaseSolidExtrude(depth=1.0,
                                                          sketch=mdb.models['Model-1'].sketches['SKETCH-SOIL'])
del mdb.models['Model-1'].sketches['SKETCH-SOIL']

# TODO SETS
# SOIL
part_soil = mdb.models['Model-1'].parts['PART-SOIL']
part_soil.Surface(
    side1Faces=part_soil.faces.findAt(
        ((0, NAIL_RADIUS, SOIL_LENGTH / 2),),
    ), name='SURFACE-SOIL-INTERFACE')

part_soil.Surface(
    side1Faces=part_soil.faces.findAt(
        ((-SOIL_HEIGHT + SOIL_NAIL_OFFSET_HEIGHT, SOIL_WIDTH / 2, SOIL_LENGTH / 2), ),
    ), name='SURFACE-SOIL-PRESSURE')

part_soil.Set(
    cells=part_soil.cells.findAt(
        ((0, SOIL_WIDTH / 2, SOIL_LENGTH / 2), ),
    ), name='SET-SOIL')

part_soil.Set(
    faces=part_soil.faces.findAt(
        ((0, SOIL_WIDTH / 2, 0), ),
        ((0, SOIL_WIDTH / 2, SOIL_LENGTH), )
    ), name='SET-SOIL-LR')

part_soil.Set(
    faces=part_soil.faces.findAt(
        ((-SOIL_HEIGHT + SOIL_NAIL_OFFSET_HEIGHT, SOIL_WIDTH / 2, SOIL_LENGTH / 2), ),
    ), name='SET-SOIL-TOP')

part_soil.Set(
    faces=part_soil.faces.findAt(
        ((SOIL_NAIL_OFFSET_HEIGHT, SOIL_WIDTH / 2, SOIL_LENGTH / 2), ),
    ), name='SET-SOIL-BOT')

part_soil.Set(
    faces=part_soil.faces.findAt(
        ((-(SOIL_HEIGHT - SOIL_NAIL_OFFSET_HEIGHT) / 2 - NAIL_RADIUS, 0, SOIL_LENGTH / 2), ),
        ((SOIL_NAIL_OFFSET_HEIGHT / 2 + NAIL_RADIUS, 0, SOIL_LENGTH / 2), ),
    ), name='SET-SOIL-FRT')

part_soil.Set(
    faces=part_soil.faces.findAt(
        ((0, SOIL_WIDTH, SOIL_LENGTH / 2), ),
    ), name='SET-SOIL-BCK')
# NAIL
part_nail = mdb.models['Model-1'].parts['PART-NAIL']
part_nail.Surface(
    side1Faces=part_nail.faces.findAt(
        ((0, NAIL_RADIUS, NAIL_LENGTH / 2), ),
    ), name='SURFACE-NAIL-INTERFACE')
part_nail.Set(
    cells=part_nail.cells.findAt(
        ((0, 0, NAIL_LENGTH / 2), ),
    ), name='SET-NAIL')

# TODO ASSEMBLY INSTANCE
assembly = mdb.models['Model-1'].rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
assembly.Instance(name='INSTANCE-SOIL', part=mdb.models['Model-1'].parts['PART-SOIL'], dependent=ON)
assembly.Instance(name='INSTANCE-NAIL', part=mdb.models['Model-1'].parts['PART-NAIL'], dependent=ON)
assembly.translate(instanceList=('INSTANCE-NAIL',), vector=(0, 0, -0.15))

# TODO CREATE MATERIAL
# SOIL
mdb.models['Model-1'].Material(name='MATERIAL-SOIL')
mdb.models['Model-1'].materials['MATERIAL-SOIL'].Elastic(table=((SOIL_ELASTIC_MODULUS, SOIL_POISSON_RATIO),))
mdb.models['Model-1'].materials['MATERIAL-SOIL'].MohrCoulombPlasticity(
    table=((SOIL_MOHR_COULOMB_FRICTION_ANGLE, SOIL_MOHR_COULOMB_DILATION_ANGLE),))
mdb.models['Model-1'].materials['MATERIAL-SOIL'].mohrCoulombPlasticity.MohrCoulombHardening(
    table=((SOIL_MOHR_COULOMB_COHESION_YIELD_STRESS,
            SOIL_MOHR_COULOMB_ABS_PLASTIC_STRAIN),))
mdb.models['Model-1'].materials['MATERIAL-SOIL'].mohrCoulombPlasticity.TensionCutOff(dependencies=0,
                                                                                     table=((0.0, 0.0),),
                                                                                     temperatureDependency=OFF)
if SOIL_DENSITY is not None:
    mdb.models['Model-1'].materials['MATERIAL-SOIL'].Density(table=((SOIL_DENSITY,),))
# NAIL
mdb.models['Model-1'].Material(name='MATERIAL-NAIL')
mdb.models['Model-1'].materials['MATERIAL-NAIL'].Elastic(table=((NAIL_ELASTIC_MODULUS, MAIL_POISSON_RATIO),))
if NAIL_DENSITY is not None:
    mdb.models['Model-1'].materials['MATERIAL-NAIL'].Density(table=((NAIL_DENSITY,),))

# Sections
mdb.models['Model-1'].HomogeneousSolidSection(name='SECTION-SOIL', material='MATERIAL-SOIL', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(name='SECTION-NAIL', material='MATERIAL-NAIL', thickness=None)

# Sections assignment
part_soil = mdb.models['Model-1'].parts['PART-SOIL']
part_soil.SectionAssignment(region=part_soil.sets['SET-SOIL'], sectionName='SECTION-SOIL', offset=0.0,
                            offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
part_nail = mdb.models['Model-1'].parts['PART-NAIL']
part_nail.SectionAssignment(region=part_nail.sets['SET-NAIL'], sectionName='SECTION-NAIL', offset=0.0,
                            offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)

# TODO STEP
if CALCULATION_METHOD == 'STANDARD':
    mdb.models['Model-1'].StaticStep(name='INITIAL-STRESS', previous='Initial',
                                     maxNumInc=INITIAL_STRESS_MAXIMAL_INCREMENTS,
                                     initialInc=INITIAL_STRESS_INITIAL_INCREMENT_SIZE,
                                     minInc=INITIAL_STRESS_MINIMAL_INCREMENT_SIZE,
                                     maxInc=INITIAL_STRESS_MAXIMAL_INCREMENT_SIZE,
                                     matrixSolver=DIRECT, matrixStorage=UNSYMMETRIC)
    mdb.models['Model-1'].StaticStep(name='PULLOUT', previous='INITIAL-STRESS',
                                     maxNumInc=PULLOUT_MAXIMAL_INCREMENTS,
                                     initialInc=PULLOUT_INITIAL_INCREMENT_SIZE,
                                     minInc=PULLOUT_MINIMAL_INCREMENT_SIZE,
                                     maxInc=PULLOUT_MAXIMAL_INCREMENT_SIZE,
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
    if PULLOUT_INCREMENTATION_TYPE == 'AUTOMATIC':
        if PULLOUT_MAXIMAL_TIME_INCREMENT == 'UNLIMITED':
            mdb.models['Model-1'].ExplicitDynamicsStep(name='PULLOUT', previous='INITIAL-STRESS',
                                                       timePeriod=PULLOUT_TIME_PERIOD,
                                                       linearBulkViscosity=PULLOUT_LINEAR_BULK_VISCOSITY,
                                                       quadBulkViscosity=PULLOUT_QUAD_BULK_VISCOSITY,
                                                       improvedDtMethod=ON,
                                                       timeIncrementationMethod=AUTOMATIC_GLOBAL)
        else:
            mdb.models['Model-1'].ExplicitDynamicsStep(name='PULLOUT', previous='INITIAL-STRESS',
                                                       timePeriod=PULLOUT_TIME_PERIOD,
                                                       linearBulkViscosity=PULLOUT_LINEAR_BULK_VISCOSITY,
                                                       quadBulkViscosity=PULLOUT_QUAD_BULK_VISCOSITY,
                                                       improvedDtMethod=ON,
                                                       maxIncrement=PULLOUT_MAXIMAL_TIME_INCREMENT,
                                                       timeIncrementationMethod=AUTOMATIC_GLOBAL)
    else:
        if PULLOUT_INCREMENT_SIZE == 'ELEMENT_BY_ELEMENT_INCREMENTATION':
            mdb.models['Model-1'].ExplicitDynamicsStep(name='PULLOUT', previous='INITIAL-STRESS',
                                                       timePeriod=PULLOUT_TIME_PERIOD,
                                                       linearBulkViscosity=PULLOUT_LINEAR_BULK_VISCOSITY,
                                                       quadBulkViscosity=PULLOUT_QUAD_BULK_VISCOSITY,
                                                       improvedDtMethod=ON,
                                                       timeIncrementationMethod=FIXED_EBE)
        else:
            mdb.models['Model-1'].ExplicitDynamicsStep(name='PULLOUT', previous='INITIAL-STRESS',
                                                       timePeriod=PULLOUT_TIME_PERIOD,
                                                       linearBulkViscosity=PULLOUT_LINEAR_BULK_VISCOSITY,
                                                       quadBulkViscosity=PULLOUT_QUAD_BULK_VISCOSITY,
                                                       improvedDtMethod=ON,
                                                       timeIncrementationMethod=FIXED_USER_DEFINED_INC,
                                                       userDefinedInc=PULLOUT_INCREMENT_SIZE)

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
region_nail = assembly.instances['INSTANCE-NAIL'].surfaces['SURFACE-NAIL-INTERFACE']
region_soil = assembly.instances['INSTANCE-SOIL'].surfaces['SURFACE-SOIL-INTERFACE']
if CALCULATION_METHOD == 'STANDARD':
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Int-1', createStepName='Initial', master=region_nail,
                                                     slave=region_soil, sliding=FINITE, thickness=ON,
                                                     interactionProperty='IntProp-1', adjustMethod=NONE,
                                                     initialClearance=OMIT, datumAxis=None, clearanceRegion=None)
else:  # EXPLICIT
    mdb.models['Model-1'].SurfaceToSurfaceContactExp(name='Int-1', createStepName='Initial', master=region_nail,
                                                     slave=region_soil, sliding=FINITE, initialClearance=OMIT,
                                                     interactionProperty='IntProp-1', datumAxis=None,
                                                     clearanceRegion=None,
                                                     mechanicalConstraint=KINEMATIC)

# TODO LOAD
# Vertical pressure
region_pressure = mdb.models['Model-1'].rootAssembly.instances['INSTANCE-SOIL'].surfaces['SURFACE-SOIL-PRESSURE']
mdb.models['Model-1'].Pressure(name='SOIL-VERTICAL-PRESSURE', createStepName='INITIAL-STRESS', region=region_pressure,
                               distributionType=UNIFORM, field='', magnitude=VERTICAL_PRESSURE, amplitude=UNSET)
# Predefined stress
region_predefined_stress = mdb.models['Model-1'].rootAssembly.instances['INSTANCE-SOIL'].sets['SET-SOIL']
mdb.models['Model-1'].Stress(name='SOIL-PREDEFINED-STRESS', region=region_predefined_stress, distributionType=UNIFORM,
                             sigma11=PREDEFINED_STRESS[0], sigma22=PREDEFINED_STRESS[1], sigma33=PREDEFINED_STRESS[2],
                             sigma12=PREDEFINED_STRESS[3], sigma13=PREDEFINED_STRESS[4], sigma23=PREDEFINED_STRESS[5])

# Confining pressure
# Reference point
mdb.models['Model-1'].parts['PART-NAIL'].ReferencePoint(point=(0.0, 0.0, NAIL_LENGTH))
RP = mdb.models['Model-1'].parts['PART-NAIL'].referencePoints[4]
mdb.models['Model-1'].parts['PART-NAIL'].Set(referencePoints=(RP,), name='SET-RP')

# Rigid body
region1 = mdb.models['Model-1'].rootAssembly.instances['INSTANCE-NAIL'].sets['SET-RP']
region2 = mdb.models['Model-1'].rootAssembly.instances['INSTANCE-NAIL'].sets['SET-NAIL']
mdb.models['Model-1'].RigidBody(name='CONSTRAINT-RIGID-NAIL', refPointRegion=region1, bodyRegion=region2)

# BC-RP INITIAL: FIXED; PULLOUT: U1 = 0.008
region_RP = mdb.models['Model-1'].rootAssembly.instances['INSTANCE-NAIL'].sets['SET-RP']
if CALCULATION_METHOD == 'STANDARD':
    mdb.models['Model-1'].DisplacementBC(name='BC-RP', createStepName='Initial',
                                         region=region_RP, u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET,
                                         amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
    mdb.models['Model-1'].boundaryConditions['BC-RP'].setValuesInStep(
        stepName='PULLOUT', u1=RP_DISPLACEMENT[0], u2=RP_DISPLACEMENT[1], u3=RP_DISPLACEMENT[2],
        ur1=RP_DISPLACEMENT[3], ur2=RP_DISPLACEMENT[4], ur3=RP_DISPLACEMENT[5])
else:
    mdb.models['Model-1'].VelocityBC(name='BC-RP', createStepName='Initial',
                                     region=region_RP, v1=SET, v2=SET, v3=SET, vr1=SET, vr2=SET, vr3=SET,
                                     amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
    mdb.models['Model-1'].boundaryConditions['BC-RP'].setValuesInStep(
        stepName='PULLOUT', v1=RP_VELOCITY[0], v2=RP_VELOCITY[1], v3=RP_VELOCITY[2],
        vr1=RP_VELOCITY[3], vr2=RP_VELOCITY[4], vr3=RP_VELOCITY[5])

# Boundary conditions
region_bot = assembly.instances['INSTANCE-SOIL'].sets['SET-SOIL-BOT']
mdb.models['Model-1'].DisplacementBC(name='BC-SOIL-BOT', createStepName='Initial',
                                     region=region_bot, u1=0.0, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET,
                                     amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='',
                                     localCsys=None)

"""region_top = assembly.instances['INSTANCE-SOIL'].sets['SET-SOIL-TOP']
mdb.models['Model-1'].DisplacementBC(name='BC-SOIL-TOP', createStepName='Initial',
                                     region=region_top, u1=UNSET, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=0.0, ur3=0.0,
                                     amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='',
                                     localCsys=None)"""

region_bck = assembly.instances['INSTANCE-SOIL'].sets['SET-SOIL-BCK']
mdb.models['Model-1'].DisplacementBC(name='BC-SOIL-BCK', createStepName='Initial',
                                     region=region_bck, u1=UNSET, u2=0.0, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET,
                                     amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='',
                                     localCsys=None)

region_lr = assembly.instances['INSTANCE-SOIL'].sets['SET-SOIL-LR']
mdb.models['Model-1'].DisplacementBC(name='BC-SOIL-LR', createStepName='Initial',
                                     region=region_lr, u1=UNSET, u2=UNSET, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET,
                                     amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='',
                                     localCsys=None)

region_frt = assembly.instances['INSTANCE-SOIL'].sets['SET-SOIL-FRT']
mdb.models['Model-1'].YsymmBC(createStepName='Initial', localCsys=None, name='BC-FRT',
                              region=region_frt)

# TODO MESH
# Element type
# Mesh soil
elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, kinematicSplit=AVERAGE_STRAIN,
                          secondOrderAccuracy=OFF, hourglassControl=ENHANCED, distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)

p = mdb.models['Model-1'].parts['PART-SOIL']
region_soil = mdb.models['Model-1'].rootAssembly.instances['INSTANCE-SOIL'].sets['SET-SOIL']
p.setElementType(regions=region_soil, elemTypes=(elemType1, elemType2, elemType3))

if SOIL_MESH_METHOD == 'SIZE':
    p.seedPart(size=SOIL_SEEDS_GENERAL_SIZE, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['PART-SOIL']
    pickedEdges = p.edges.findAt(
        ((0, NAIL_RADIUS, 0),),
        ((0, NAIL_RADIUS, SOIL_LENGTH),),
        ((-NAIL_RADIUS*1.5, 0, 0),),
        ((-NAIL_RADIUS*1.5, 0, SOIL_LENGTH),),
        ((NAIL_RADIUS*1.5, 0, 0),),
        ((NAIL_RADIUS*1.5, 0, SOIL_LENGTH),),
    )
    p.seedEdgeBySize(edges=pickedEdges, size=SOIL_SEEDS_DENSE_SIZE, deviationFactor=0.1, minSizeFactor=0.1,
                     constraint=FINER)
else:
    p = mdb.models['Model-1'].parts['PART-SOIL']
    p.seedEdgeByNumber(edges=p.edges, number=SOIL_SEEDS_GENERAL_NUMBER, constraint=FINER)
    pickedEdges = p.edges.findAt(
        ((0, NAIL_RADIUS, 0),),
        ((0, NAIL_RADIUS, SOIL_LENGTH),),
        ((-NAIL_RADIUS*1.5, 0, 0),),
        ((-NAIL_RADIUS*1.5, 0, SOIL_LENGTH),),
        ((NAIL_RADIUS*1.5, 0, 0),),
        ((NAIL_RADIUS*1.5, 0, SOIL_LENGTH),),
    )
    p.seedEdgeByNumber(edges=pickedEdges, number=SOIL_SEEDS_DENSE_NUMBER, constraint=FINER)

mdb.models['Model-1'].parts['PART-SOIL'].generateMesh()

# Mesh nail
if CALCULATION_METHOD == 'STANDARD':
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, kinematicSplit=AVERAGE_STRAIN,
                              secondOrderAccuracy=OFF, hourglassControl=ENHANCED, distortionControl=DEFAULT)
else:
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, kinematicSplit=AVERAGE_STRAIN,
                              secondOrderAccuracy=OFF, hourglassControl=RELAX_STIFFNESS, distortionControl=DEFAULT)

elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['PART-NAIL']
region_nail = mdb.models['Model-1'].rootAssembly.instances['INSTANCE-NAIL'].sets['SET-NAIL']
p.setElementType(regions=region_nail, elemTypes=(elemType1, elemType2, elemType3))

if NAIL_MESH_METHOD == 'SIZE':
    p.seedPart(size=NAIL_SEEDS_GENERAL_SIZE, deviationFactor=0.1, minSizeFactor=0.1)
    pickedEdges = p.edges.findAt(
        ((0, NAIL_RADIUS, 0),),
        ((0, NAIL_RADIUS, NAIL_LENGTH),),
        ((0, 0, 0),),
        ((0, 0, NAIL_LENGTH),),
    )
    p.seedEdgeBySize(edges=pickedEdges, size=NAIL_SEEDS_DENSE_SIZE, deviationFactor=0.1, minSizeFactor=0.1,
                     constraint=FINER)
else:
    p.seedEdgeByNumber(edges=p.edges, number=NAIL_SEEDS_GENERAL_NUMBER, constraint=FINER)
    pickedEdges = p.edges.findAt(
        ((0, NAIL_RADIUS, 0),),
        ((0, NAIL_RADIUS, NAIL_LENGTH),),
        ((0, 0, 0),),
        ((0, 0, NAIL_LENGTH),),
    )
    p.seedEdgeByNumber(edges=pickedEdges, number=NAIL_SEEDS_DENSE_NUMBER, constraint=FINER)

mdb.models['Model-1'].parts['PART-NAIL'].generateMesh()

# TODO JOB
mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS,
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
        explicitPrecision=DOUBLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF,
        userSubroutine=SUBROUTINE_PATH,
        scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1,
        numGPUs=0)

# TODO WRITE INPUT FILE
mdb.jobs['Job-1'].writeInput()

# TODO SAVE CAE MODEL TO FILE
mdb.saveAs(pathName='pullout.cae')

# TODO SUBMIT JOB
# mdb.jobs['Job-1'].submit(consistencyChecking=OFF)

# OPEN OUTPUT DATABASE FILE
# mdb.jobs['Job-1'].waitForCompletion()
# odb = session.openOdb(name=os.path.join(WORK_DIRECTORY, 'Job-1.odb'))
# session.viewports['Viewport: 1'].setValues(displayedObject=odb)
