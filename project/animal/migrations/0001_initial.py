# Generated by Django 2.2 on 2019-04-20 04:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='\n            Name should be: sex, common strain name, species (plural) and use Title Style\n            (e.g. Male Sprague Dawley Rat, Female C57BL/6 Mice, Male and Female\n            C57BL/6 Mice). For developmental studies, include the generation before\n            sex in title (e.g., F1 Male Sprague Dawley Rat or P0 Female C57 Mice)\n            ', max_length=80)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('C', 'Combined'), ('R', 'Not reported')], max_length=1)),
                ('animal_source', models.CharField(blank=True, help_text='Source from where animals were acquired', max_length=128)),
                ('lifestage_exposed', models.CharField(blank=True, help_text='Definitions: <strong>Developmental</strong>: Prenatal and perinatal exposure in dams or postnatal exposure in offspring until sexual maturity (~6 weeks in rats and mice). Include studies with pre-mating exposure <em>if the endpoint focus is developmental</em>. <strong>Adult</strong>: Exposure in sexually mature males or females. <strong>Adult (gestation)</strong>: Exposure in dams duringpregnancy. <strong>Multi-lifestage</strong>: includes both developmental and adult (i.e., multi-generational studies, exposure that start before sexual maturity and continue to adulthood)', max_length=32, verbose_name='Exposure lifestage')),
                ('lifestage_assessed', models.CharField(blank=True, help_text='Definitions: <b>Developmental</b>: Prenatal and perinatal exposure in dams or postnatal exposure in offspring until sexual maturity (~6 weeks in rats and mice). Include studies with pre-mating exposure if the endpoint focus is developmental. <b>Adult</b>: Exposure in sexually mature males or females. <b>Adult (gestation)</b>: Exposure in dams during pregnancy. <b>Multi-lifestage</b>: includes both developmental and adult (i.e., multi-generational studies, exposure that start before sexual maturity and continue to adulthood)', max_length=32)),
                ('generation', models.CharField(blank=True, choices=[('', 'N/A (not generational-study)'), ('P0', 'Parent-generation (P0)'), ('F1', 'First-generation (F1)'), ('F2', 'Second-generation (F2)'), ('F3', 'Third-generation (F3)'), ('F4', 'Fourth-generation (F4)'), ('Ot', 'Other')], default='', max_length=2)),
                ('comments', models.TextField(blank=True, help_text='Copy paste animal husbandry information from materials and methods, use quotation marks around all text directly copy/pasted from paper.', verbose_name='Animal Source and Husbandry')),
                ('diet', models.TextField(blank=True, help_text='Describe diet as presented in the paper (e.g., "soy-protein free 2020X Teklad," "Atromin 1310", "standard rodent chow").')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DoseGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dose_group_id', models.PositiveSmallIntegerField()),
                ('dose', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('dose_units', 'dose_group_id'),
            },
        ),
        migrations.CreateModel(
            name='DosingRegime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_of_exposure', models.CharField(choices=[('OR', 'Oral'), ('OC', 'Oral capsule'), ('OD', 'Oral diet'), ('OG', 'Oral gavage'), ('OW', 'Oral drinking water'), ('I', 'Inhalation'), ('IG', 'Inhalation - gas'), ('IR', 'Inhalation - particle'), ('IA', 'Inhalation - vapor'), ('D', 'Dermal'), ('SI', 'Subcutaneous injection'), ('IP', 'Intraperitoneal injection'), ('IV', 'Intravenous injection'), ('IO', 'in ovo'), ('P', 'Parental'), ('W', 'Whole body'), ('M', 'Multiple'), ('U', 'Unknown'), ('O', 'Other')], help_text='Primary route of exposure. If multiple primary-exposures, describe in notes-field below', max_length=2)),
                ('duration_exposure', models.FloatField(blank=True, help_text='Length of exposure period (fractions allowed), used for sorting in visualizations. For single-dose or multiple-dose/same day gavage studies, 1.', null=True, verbose_name='Exposure duration (days)')),
                ('duration_exposure_text', models.CharField(blank=True, help_text='Length of time between start of exposure and outcome assessment, in days when &lt;7 (e.g., 5d), weeks when &ge;7 days to 12 weeks (e.g., 1wk, 12wk), or months when &gt;12 weeks (e.g., 15mon). For repeated measures use descriptions such as "1, 2 and 3 wk".  For inhalations studies, also include hours per day and days per week, e.g., "13wk (6h/d, 7d/wk)." This field is commonly used in visualizations, so use abbreviations (h, d, wk, mon, y) and no spaces between numbers to save space. For reproductive and developmental studies, where possible instead include abbreviated age descriptions such as "GD1-10" or "GD2-PND10". For gavage studies, include the number of doses, e.g. "1wk (1dose/d, 5d/wk)" or "2doses" for a single-day experiment.', max_length=128, verbose_name='Exposure duration (text)')),
                ('duration_observation', models.FloatField(blank=True, help_text='Optional: Numeric length of time between start of exposure and outcome assessment in days. This field may be used to sort studies which is why days are used as a common metric.', null=True, verbose_name='Exposure-outcome duration')),
                ('num_dose_groups', models.PositiveSmallIntegerField(default=4, help_text='Number of dose groups, plus control', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Number of Dose Groups')),
                ('positive_control', models.NullBooleanField(choices=[(True, 'Yes'), (False, 'No'), (None, 'Unknown')], default=False, help_text='Was a positive control used?')),
                ('negative_control', models.CharField(choices=[('NR', 'Not-reported'), ('UN', 'Untreated'), ('VT', 'Vehicle-treated'), ('B', 'Untreated + Vehicle-treated'), ('N', 'No')], default='VT', help_text='Description of negative-controls used', max_length=2)),
                ('description', models.TextField(blank=True, help_text='Cut and paste from methods, use quotation marks around all text directly copy/pasted from paper. Also summarize results of any analytical work done to confirm dose, stability, etc. This can be a narrative summary of tabular information, e.g., "Author\'s present data on the target and actual concentration (Table 1; means &plusmn; SD for entire 13-week period) and the values are very close." ')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
