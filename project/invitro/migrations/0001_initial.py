# Generated by Django 2.2 on 2019-04-20 04:00

import animal.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assessment', '0001_initial'),
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IVCellType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=64)),
                ('strain', models.CharField(default='not applicable', max_length=64)),
                ('sex', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('mf', 'Male and female'), ('na', 'Not-applicable'), ('nr', 'Not-reported')], max_length=2)),
                ('cell_type', models.CharField(max_length=64)),
                ('culture_type', models.CharField(choices=[('nr', 'not reported'), ('im', 'Immortalized cell line'), ('pc', 'Primary culture'), ('tt', 'Transient transfected cell line'), ('st', 'Stably transfected cell line'), ('ts', 'Transient transfected into stably transfected cell line'), ('na', 'not applicable')], max_length=2)),
                ('tissue', models.CharField(max_length=64)),
                ('source', models.CharField(max_length=128, verbose_name='Source of cell cultures')),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ivcelltypes', to='study.Study')),
            ],
        ),
        migrations.CreateModel(
            name='IVChemical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('cas', models.CharField(blank=True, max_length=40, verbose_name='Chemical identifier (CAS)')),
                ('cas_inferred', models.BooleanField(default=False, help_text='Was the correct CAS inferred or incorrect in the original document?', verbose_name='CAS inferred?')),
                ('cas_notes', models.CharField(max_length=256, verbose_name='CAS determination notes')),
                ('source', models.CharField(max_length=128, verbose_name='Source of chemical')),
                ('purity', models.CharField(help_text='Ex: >99%, not-reported, etc.', max_length=32, verbose_name='Chemical purity')),
                ('purity_confirmed', models.BooleanField(default=False, verbose_name='Purity experimentally confirmed')),
                ('purity_confirmed_notes', models.TextField(blank=True)),
                ('dilution_storage_notes', models.TextField(help_text='Dilution, storage, and observations such as precipitation should be noted here.')),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ivchemicals', to='study.Study')),
            ],
        ),
        migrations.CreateModel(
            name='IVEndpoint',
            fields=[
                ('baseendpoint_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='assessment.BaseEndpoint')),
                ('assay_type', models.CharField(max_length=128)),
                ('short_description', models.CharField(help_text='Short (<128 character) description of effect & measurement', max_length=128)),
                ('effect', models.CharField(help_text='Effect, using common-vocabulary', max_length=128)),
                ('data_location', models.CharField(blank=True, help_text='Details on where the data are found in the literature (ex: Figure 1, Table 2, etc.)', max_length=128)),
                ('data_type', models.CharField(choices=[('C', 'Continuous'), ('D', 'Dichotomous'), ('NR', 'Not reported')], default='C', max_length=2, verbose_name='Dataset type')),
                ('variance_type', models.PositiveSmallIntegerField(choices=[(0, 'NA'), (1, 'SD'), (2, 'SE')], default=0)),
                ('response_units', models.CharField(blank=True, max_length=64, verbose_name='Response units')),
                ('values_estimated', models.BooleanField(default=False, help_text='Response values were estimated using a digital ruler or other methods')),
                ('observation_time', models.CharField(blank=True, max_length=32)),
                ('observation_time_units', models.PositiveSmallIntegerField(choices=[(0, 'not-reported'), (1, 'seconds'), (2, 'minutes'), (3, 'hours'), (4, 'days'), (5, 'weeks'), (6, 'months')], default=0)),
                ('NOEL', models.SmallIntegerField(default=-999, help_text='No observed effect level', verbose_name='NOEL')),
                ('LOEL', models.SmallIntegerField(default=-999, help_text='Lowest observed effect level', verbose_name='LOEL')),
                ('monotonicity', models.PositiveSmallIntegerField(choices=[(8, '--'), (0, 'N/A, single dose level study'), (1, 'N/A, no effects detected'), (2, 'visual appearance of monotonicity'), (3, 'monotonic and significant trend'), (4, 'visual appearance of non-monotonicity'), (6, 'no pattern/unclear')], default=8)),
                ('overall_pattern', models.PositiveSmallIntegerField(choices=[(0, 'not-available'), (1, 'increase'), (2, 'increase, then decrease'), (6, 'increase, then no change'), (3, 'decrease'), (4, 'decrease, then increase'), (7, 'decrease, then no change'), (5, 'no clear pattern'), (8, 'no change')], default=0)),
                ('statistical_test_notes', models.CharField(blank=True, help_text='Notes describing details on the statistical tests performed', max_length=256)),
                ('trend_test', models.PositiveSmallIntegerField(choices=[(0, 'not reported'), (1, 'not analyzed'), (2, 'not applicable'), (3, 'significant'), (4, 'not significant')], default=0)),
                ('trend_test_notes', models.CharField(blank=True, help_text='Notes describing details on the trend-test performed', max_length=256)),
                ('endpoint_notes', models.TextField(blank=True, help_text='Any additional notes regarding the endpoint itself')),
                ('result_notes', models.TextField(blank=True, help_text='Qualitative description of the results')),
                ('additional_fields', models.TextField(default='{}')),
            ],
            bases=('assessment.baseendpoint',),
        ),
        migrations.CreateModel(
            name='IVEndpointCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
            bases=(utils.models.AssessmentRootMixin, models.Model),
        ),
        migrations.CreateModel(
            name='IVExperiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('transfection', models.CharField(help_text='Details on transfection methodology and details on genes or other genetic material introduced into assay, or "not-applicable"', max_length=256)),
                ('cell_notes', models.TextField(blank=True, help_text='Description of type of cell-line used (ex: primary cell-line, immortalized cell-line, stably transfected cell-line, transient transfected cell-line, etc.)')),
                ('dosing_notes', models.TextField(blank=True, help_text='Notes describing dosing-protocol, including duration-details')),
                ('metabolic_activation', models.CharField(choices=[('+', 'with metabolic activation'), ('-', 'without metabolic activation'), ('na', 'not applicable'), ('nr', 'not reported')], default='nr', help_text='Was metabolic-activation used in system (ex: S9)?', max_length=2)),
                ('serum', models.CharField(help_text='Percent serum, serum-type, and/or description', max_length=128)),
                ('has_naive_control', models.BooleanField(default=False)),
                ('has_positive_control', models.BooleanField(default=False)),
                ('positive_control', models.CharField(blank=True, help_text='Positive control chemical or other notes', max_length=128)),
                ('has_negative_control', models.BooleanField(default=False)),
                ('negative_control', models.CharField(blank=True, help_text='Negative control chemical or other notes', max_length=128)),
                ('has_vehicle_control', models.BooleanField(default=False)),
                ('vehicle_control', models.CharField(blank=True, help_text='Vehicle control chemical or other notes', max_length=128)),
                ('control_notes', models.CharField(blank=True, help_text='Additional details related to controls', max_length=256)),
                ('cell_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ivexperiments', to='invitro.IVCellType')),
                ('dose_units', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ivexperiments', to='assessment.DoseUnits')),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ivexperiments', to='study.Study')),
            ],
        ),
        migrations.CreateModel(
            name='IVEndpointGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dose_group_id', models.PositiveSmallIntegerField()),
                ('dose', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('n', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('response', models.FloatField(blank=True, null=True)),
                ('variance', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('difference_control', models.CharField(choices=[('nc', 'no-change'), ('-', 'decrease'), ('+', 'increase'), ('nt', 'not-tested')], default='nc', max_length=2)),
                ('significant_control', models.CharField(choices=[('nr', 'not reported'), ('si', 'p ≤ 0.05'), ('ns', 'not significant'), ('na', 'not applicable')], default='nr', max_length=2)),
                ('cytotoxicity_observed', models.NullBooleanField(choices=[(None, 'not reported'), (False, 'not observed'), (True, 'observed')], default=None)),
                ('precipitation_observed', models.NullBooleanField(choices=[(None, 'not reported'), (False, 'not observed'), (True, 'observed')], default=None)),
                ('endpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='invitro.IVEndpoint')),
            ],
            options={
                'ordering': ('endpoint', 'dose_group_id'),
            },
            bases=(animal.models.ConfidenceIntervalsMixin, models.Model),
        ),
        migrations.AddField(
            model_name='ivendpoint',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='endpoints', to='invitro.IVEndpointCategory'),
        ),
        migrations.AddField(
            model_name='ivendpoint',
            name='chemical',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endpoints', to='invitro.IVChemical'),
        ),
        migrations.AddField(
            model_name='ivendpoint',
            name='experiment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endpoints', to='invitro.IVExperiment'),
        ),
        migrations.CreateModel(
            name='IVBenchmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benchmark', models.CharField(max_length=32)),
                ('value', models.FloatField()),
                ('endpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='benchmarks', to='invitro.IVEndpoint')),
            ],
        ),
    ]
