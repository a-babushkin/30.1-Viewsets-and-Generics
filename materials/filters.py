import django_filters

from materials.models import Course, Lesson


class CoursesFilter(django_filters.FilterSet):
    course = django_filters.NumberFilter(field_name="course__id", lookup_expr="exact")

    class Meta:
        model = Course
        fields = ["course"]

class LessonsFilter(django_filters.FilterSet):
    lesson = django_filters.NumberFilter(field_name="lesson__id", lookup_expr="exact")

    class Meta:
        model = Lesson
        fields = ["lesson"]
