import django_filters

from users.models import Payment


class PaymentFilter(django_filters.FilterSet):
    payment_date = django_filters.DateFromToRangeFilter(field_name="payment_date")
    course = django_filters.NumberFilter(field_name="course__id", lookup_expr="exact")
    lesson = django_filters.NumberFilter(field_name="lesson__id", lookup_expr="exact")
    payment_method = django_filters.ChoiceFilter(
        choices=(("cash", "Наличные"), ("transfer", "Перевод"))
    )

    class Meta:
        model = Payment
        fields = ["course", "lesson", "payment_method"]
