from canvasapi.canvas_object import CanvasObject
from canvasapi.exceptions import CanvasException


class LiveAssessment(CanvasObject):
    def __str__(self):
        return "{} ({})".format(self.title, self.id)
