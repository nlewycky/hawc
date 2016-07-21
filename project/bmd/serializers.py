from copy import deepcopy
from jsonschema import validate, ValidationError
from rest_framework import serializers


from . import models


class LogicFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LogicField
        fields = (
            'id',
            'name',
            'description',
            'failure_bin',
            'threshold',
            'continuous_on',
            'dichotomous_on',
            'cancer_dichotomous_on',
        )


class SelectedModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SelectedModel
        fields = ('id', 'model', 'notes')


class BMDModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BMDModel
        fields = (
            'id', 'model_id', 'bmr_id',
            'name', 'overrides', 'date_executed',
            'execution_error', 'output', 'outfile',
            'created', 'last_updated',
        )


class BMDSessionSerializer(serializers.ModelSerializer):
    allModelOptions = serializers.JSONField(source='get_model_options', read_only=True)
    allBmrOptions = serializers.JSONField(source='get_bmr_options', read_only=True)
    selected_model = SelectedModelSerializer(source='get_selected_model', read_only=True)
    models = BMDModelSerializer(many=True)
    logic = LogicFieldSerializer(source='get_logic', many=True)

    class Meta:
        model = models.BMDSession
        fields = (
            'id', 'bmrs', 'models', 'dose_units',
            'allModelOptions', 'allBmrOptions',
            'selected_model', 'logic',
        )


class BMDSessionUpdateSerializer(serializers.Serializer):
    bmrs = serializers.JSONField()
    modelSettings = serializers.JSONField()

    bmr_schema = schema = {
        'type': 'array',
        'items': {
            'type': 'object',
            'properties': {
                'type': {'type': 'string'},
                'value': {'type': 'number'},
                'confidence_level': {'type': 'number'},
            },
            'required': ['type', 'value', 'confidence_level']
        },
        'minItems': 1,
    }

    model_schema = {
        'type': 'array',
        'items': {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'overrides': {'type': 'object'},
                'defaults': {'type': 'object'},
            },
            'required': ['name', 'overrides', 'defaults']
        },
        'minItems': 1,
    }

    def validate_bmrs(self, value):
        try:
            validate(value, self.bmr_schema)
        except ValidationError as err:
            raise serializers.ValidationError(err.message)
        return value

    def validate_modelSettings(self, value):
        try:
            validate(value, self.model_schema)
        except ValidationError as err:
            raise serializers.ValidationError(err.message)
        return value

    def save(self):
        self.instance.bmrs = self.validated_data['bmrs']
        self.instance.date_executed = None
        self.instance.save()

        self.instance.models.all().delete()
        objects = []
        for i, bmr in enumerate(self.validated_data['bmrs']):
            bmr_overrides = self.instance.get_bmr_overrides(
                self.instance.get_session(), i)
            for j, settings in enumerate(self.validated_data['modelSettings']):
                overrides = deepcopy(settings['overrides'])
                overrides.update(bmr_overrides)
                obj = models.BMDModel(
                    session=self.instance,
                    bmr_id=i,
                    model_id=j,
                    name=settings['name'],
                    overrides=overrides,
                )
                objects.append(obj)
        models.BMDModel.objects.bulk_create(objects)


class SelectedModelUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SelectedModel
        fields = (
            'id', 'model', 'notes'
        )

    def save(self):
        session = self.instance

        instance = session.get_selected_model()
        if not instance:
            instance = models.SelectedModel(endpoint_id=session.endpoint_id)

        instance.model = self.validated_data['model']
        instance.notes = self.validated_data['notes']
        instance.save()
