from .Annotation import Annotation
from abaqusConstants import *
import typing

class Arrow(Annotation):

    """The Arrow object stores the visual settings and location of an arrow annotation. 
    The Arrow object is derived from the Annotation object. 

    Access
    ------
        - import annotationToolset
        - mdb.annotations[name]
        - session.odbs[name].userData.annotations[name]
        - session.viewports[name].annotationsToPlot[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    def __init__(self, name: str, startPoint: tuple[float] = (), endPoint: tuple[float] = (), 
                 startAnchor: typing.Union[SymbolicConstant, float] = BOTTOM_LEFT, 
                 endAnchor: typing.Union[SymbolicConstant, float] = BOTTOM_LEFT, 
                 startHeadStyle: SymbolicConstant = NONE, endHeadStyle: SymbolicConstant = FILLED_ARROW, 
                 startGap: float = 0, endGap: float = 0, color: str = '', 
                 lineStyle: SymbolicConstant = SOLID, lineThickness: SymbolicConstant = VERY_THIN):
        """This method creates an Arrow object.

        Path
        ----
            - mdb.Arrow
            - session.odbs[*name*].userData.Arrow

        Parameters
        ----------
        name
            A String specifying the annotation repository key. 
        startPoint
            A pair of Floats specifying the start point *X*- and *Y*-offsets in millimeters from 
            *startAnchor*. The default value is (0, 0). 
        endPoint
            A pair of Floats specifying the end point *X*- and *Y*-offsets in millimeters from 
            *endAnchor*. The default value is (0, 0). 
        startAnchor
            A SymbolicConstant or a sequence of Floats specifying a point. A sequence of two Floats 
            specifies the *X*- and *Y*-coordinates as percentages of the viewport width and height. 
            A sequence of three Floats specifies the *X*-, *Y*-, and *Z*-coordinates of a point in 
            the model coordinate system. A SymbolicConstant indicates a relative position. Possible 
            values 
            are:BOTTOM_LEFTBOTTOM_CENTERBOTTOM_RIGHTCENTER_LEFTCENTERCENTER_RIGHTTOP_LEFTTOP_CENTERTOP_RIGHTThe 
            default value is BOTTOM_LEFT. 
        endAnchor
            A SymbolicConstant or a sequence of Floats specifying a point. A sequence of two Floats 
            specifies the *X*- and *Y*-coordinates as percentages of the viewport width and height. 
            A Sequence of three Floats specifies the *X*-, *Y*-, and *Z*-coordinates of a point in 
            the model coordinate system. A SymbolicConstant indicates a relative position. Possible 
            values 
            are:BOTTOM_LEFTBOTTOM_CENTERBOTTOM_RIGHTCENTER_LEFTCENTERCENTER_RIGHTTOP_LEFTTOP_CENTERTOP_RIGHTThe 
            default value is BOTTOM_LEFT. 
        startHeadStyle
            A SymbolicConstant specifying the style of the start head. Possible values 
            are:ARROWFILLED_ARROWHOLLOW_CIRCLEFILLED_CIRCLEHOLLOW_DIAMONDFILLED_DIAMONDHOLLOW_SQUAREFILLED_SQUARENONEThe 
            default value is NONE. 
        endHeadStyle
            A SymbolicConstant specifying the style of the end head. Possible values 
            are:ARROWFILLED_ARROWHOLLOW_ 
            CIRCLEFILLED_CIRCLEHOLLOW_DIAMONDFILLED_DIAMONDHOLLOW_SQUAREFILLED_SQUARENONEThe default 
            value is FILLED_ARROW. 
        startGap
            A Float specifying the distance in millimeters between the arrow start point and the 
            arrow start head. The default value is 0.0. 
        endGap
            A Float specifying the distance in millimeters between the arrow end point and the arrow 
            end head. The default value is 0.0. 
        color
            A String specifying the color of the arrow. Possible string values are any valid color. 
            The default value is "White". 
        lineStyle
            A SymbolicConstant specifying the line style of the arrow. Possible values are SOLID, 
            DASHED, DOTTED, and DOT_DASH. The default value is SOLID. 
        lineThickness
            A SymbolicConstant specifying the line thickness of the arrow. Possible values are 
            VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN. 

        Returns
        -------
            An Arrow object. 

        Exceptions
        ----------
            InvalidNameError. 
            !img 
        """
        super().__init__()
        pass

    def translateStartPoint(self, x: float = None, y: float = None):
        """This method translates the start point of the Arrow object on the viewport plane.

        Parameters
        ----------
        x
            A Float specifying the *X* translation amount in millimeters. 
        y
            A Float specifying the*Y* translation amount in millimeters. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
            !img 
        """
        pass

    def translateEndPoint(self, x: float = None, y: float = None):
        """This method translates the end point of the Arrow object on the viewport plane.

        Parameters
        ----------
        x
            A Float specifying the *X* translation amount in millimeters. 
        y
            A Float specifying the*Y* translation amount in millimeters. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
            !img 
        """
        pass

    def setValues(self, startPoint: tuple[float] = (), endPoint: tuple[float] = (), 
                  startAnchor: typing.Union[SymbolicConstant, float] = BOTTOM_LEFT, 
                  endAnchor: typing.Union[SymbolicConstant, float] = BOTTOM_LEFT, 
                  startHeadStyle: SymbolicConstant = NONE, endHeadStyle: SymbolicConstant = FILLED_ARROW, 
                  startGap: float = 0, endGap: float = 0, color: str = '', 
                  lineStyle: SymbolicConstant = SOLID, lineThickness: SymbolicConstant = VERY_THIN):
        """This method modifies the Arrow object.

        Parameters
        ----------
        startPoint
            A pair of Floats specifying the start point *X*- and *Y*-offsets in millimeters from 
            *startAnchor*. The default value is (0, 0). 
        endPoint
            A pair of Floats specifying the end point *X*- and *Y*-offsets in millimeters from 
            *endAnchor*. The default value is (0, 0). 
        startAnchor
            A SymbolicConstant or a sequence of Floats specifying a point. A sequence of two Floats 
            specifies the *X*- and *Y*-coordinates as percentages of the viewport width and height. 
            A sequence of three Floats specifies the *X*-, *Y*-, and *Z*-coordinates of a point in 
            the model coordinate system. A SymbolicConstant indicates a relative position. Possible 
            values 
            are:BOTTOM_LEFTBOTTOM_CENTERBOTTOM_RIGHTCENTER_LEFTCENTERCENTER_RIGHTTOP_LEFTTOP_CENTERTOP_RIGHTThe 
            default value is BOTTOM_LEFT. 
        endAnchor
            A SymbolicConstant or a sequence of Floats specifying a point. A sequence of two Floats 
            specifies the *X*- and *Y*-coordinates as percentages of the viewport width and height. 
            A Sequence of three Floats specifies the *X*-, *Y*-, and *Z*-coordinates of a point in 
            the model coordinate system. A SymbolicConstant indicates a relative position. Possible 
            values 
            are:BOTTOM_LEFTBOTTOM_CENTERBOTTOM_RIGHTCENTER_LEFTCENTERCENTER_RIGHTTOP_LEFTTOP_CENTERTOP_RIGHTThe 
            default value is BOTTOM_LEFT. 
        startHeadStyle
            A SymbolicConstant specifying the style of the start head. Possible values 
            are:ARROWFILLED_ARROWHOLLOW_CIRCLEFILLED_CIRCLEHOLLOW_DIAMONDFILLED_DIAMONDHOLLOW_SQUAREFILLED_SQUARENONEThe 
            default value is NONE. 
        endHeadStyle
            A SymbolicConstant specifying the style of the end head. Possible values 
            are:ARROWFILLED_ARROWHOLLOW_ 
            CIRCLEFILLED_CIRCLEHOLLOW_DIAMONDFILLED_DIAMONDHOLLOW_SQUAREFILLED_SQUARENONEThe default 
            value is FILLED_ARROW. 
        startGap
            A Float specifying the distance in millimeters between the arrow start point and the 
            arrow start head. The default value is 0.0. 
        endGap
            A Float specifying the distance in millimeters between the arrow end point and the arrow 
            end head. The default value is 0.0. 
        color
            A String specifying the color of the arrow. Possible string values are any valid color. 
            The default value is "White". 
        lineStyle
            A SymbolicConstant specifying the line style of the arrow. Possible values are SOLID, 
            DASHED, DOTTED, and DOT_DASH. The default value is SOLID. 
        lineThickness
            A SymbolicConstant specifying the line thickness of the arrow. Possible values are 
            VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
            !img 
        """
        pass

