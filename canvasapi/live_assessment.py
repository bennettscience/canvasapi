from canvasapi.canvas_object import CanvasObject
from canvasapi.exceptions import CanvasException
from canvasapi.paginated_list import PaginatedList

class LiveAssessment(CanvasObject):
    def __str__(self, course_id):
        return "{} ({})".format(self.title, self.id)

    def __get_next(self):
        """
        Get the next page of results.

        The LiveAssessment endpoint doesn't use <Link> headers for pagination,
        so this method handles pagination from the original response before
        returning the response to the user.

        :rtype: dict
        """
        pass
    
    def get_results(self, **kwargs):
        """
        Get results for this LiveAssessment

        :calls: `GET /api/v1/courses/:course_id/live_assessments/:assessment_id/results \
        <https://canvas.instructure.com/doc/api/live_assessments.html#method.live_assessments/results.index>`_

        :rtype: :class: `canvasapi.paginated_list.PaginatedList` of
            :class: `canvasapi.live_assessment.LiveAssessmentResult`
        """
        # Make the initial call
        # Handle any pagination
        # return a list

        # return PaginatedList(
        #     LiveAssessmentResult,
        #     self._requester,
        #     "GET",
        #     "courses/{}/live_assessments/{}/results".format(self.course_id, self.id)
        # )
        pass


class LiveAssessmentResult(CanvasObject):
    def __str__(self):
        return "{} ({})".format(self.id, self.passed)
