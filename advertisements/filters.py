from django.db import models
from django_filters import rest_framework as filters, DateFromToRangeFilter
from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = DateFromToRangeFilter()
    creator = filters.NumberFilter()
    status = filters.ChoiceFilter(choices=AdvertisementStatusChoices.choices)

    class Meta:
        model = Advertisement
        fields = []
