from __future__ import absolute_import

from rest_framework import viewsets
from rest_framework.response import Response

from api.permissions import AssessmentLevelPermissions, get_permitted_assessment

from . import models, serializers


class MetaResult(viewsets.ReadOnlyModelViewSet):
    permission_classes = (AssessmentLevelPermissions, )
    model = models.MetaResult
    serializer_class = serializers.MetaResultSerializer
    queryset = models.MetaResult.objects.all()

    def list(self, request):
        # override list to only return meta-results for a single assessment
        assessment = get_permitted_assessment(request)
        by_assessment = self.model.objects.filter(protocol__study__assessment=assessment)
        page = self.paginate_queryset(by_assessment)
        serializer = self.get_pagination_serializer(page)
        return Response(serializer.data)


class AssessedOutcome(viewsets.ReadOnlyModelViewSet):
    permission_classes = (AssessmentLevelPermissions, )
    model = models.AssessedOutcome
    serializer_class = serializers.AssessedOutcomeSerializer
    queryset = models.AssessedOutcome.objects.all()

    def list(self, request):
        # override list to only return assessed-outcomes for a single assessment
        assessment = get_permitted_assessment(request)
        by_assessment = self.model.objects.filter(assessment=assessment)
        page = self.paginate_queryset(by_assessment)
        serializer = self.get_pagination_serializer(page)
        return Response(serializer.data)