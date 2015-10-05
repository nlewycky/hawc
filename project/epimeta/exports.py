from study.models import Study
from utils.helper import FlatFileExporter

from . import models


class MetaResultFlatComplete(FlatFileExporter):
    """
    Returns a complete export of all data required to rebuild the the
    epidemiological meta-result study type from scratch.
    """

    def _get_header_row(self):
        header = []
        header.extend(Study.flat_complete_header_row())
        header.extend(models.MetaProtocol.flat_complete_header_row())
        header.extend(models.MetaResult.flat_complete_header_row())
        header.extend(models.SingleResult.flat_complete_header_row())
        return header

    def _get_data_rows(self):
        rows = []
        for obj in self.queryset:
            ser = obj.get_json(json_encode=False)
            row = []
            row.extend(Study.flat_complete_data_row(ser['protocol']['study']))
            row.extend(models.MetaProtocol.flat_complete_data_row(ser['protocol']))
            row.extend(models.MetaResult.flat_complete_data_row(ser))

            if len(ser['single_results2']) == 0:
                # print one-row with no single-results
                rows.append(row)
            else:
                # print each single-result as a new row
                for sr in ser['single_results2']:
                    row_copy = list(row)  # clone
                    row_copy.extend(models.SingleResult.flat_complete_data_row(sr))
                    rows.append(row_copy)
        return rows


class MetaResultFlatDataPivot(FlatFileExporter):
    """
    Return a subset of frequently-used data for generation of data-pivot
    visualizations.
    """

    def _get_header_row(self):
        return [
            'Study',
            'Study URL',
            'Study HAWC ID',
            'Study Published?',

            'Protocol Primary Key',
            'Protocol URL',
            'Protocol Name',
            'Protocol Type',
            'Total References',
            'Identified References',

            'Row Key',
            'Result Primary Key',
            'Result URL',
            'Result Label',
            'Health Outcome',
            'Exposure',
            'Result References',
            'Statistical Metric',
            'Statistical Metric Abbreviation',
            'N',
            'Estimate',
            'Lower CI',
            'Upper CI',
            'CI units',
            'Heterogeneity'
        ]

    def _get_data_rows(self):
        rows = []
        for obj in self.queryset:
            ser = obj.get_json(json_encode=False)
            row = [
                ser['protocol']['study']['short_citation'],
                ser['protocol']['study']['url'],
                ser['protocol']['study']['id'],
                ser['protocol']['study']['published'],

                ser['protocol']['id'],
                ser['protocol']['url'],
                ser['protocol']['name'],
                ser['protocol']['protocol_type'],
                ser['protocol']['total_references'],
                ser['protocol']['total_studies_identified'],

                ser['id'],  # repeat for data-pivot key
                ser['id'],
                ser['url'],
                ser['label'],
                ser['health_outcome'],
                ser['exposure_name'],
                ser['number_studies'],
                ser['statistical_metric']['metric'],
                ser['statistical_metric']['abbreviation'],
                ser['n'],
                ser['estimate'],
                ser['lower_ci'],
                ser['upper_ci'],
                ser['ci_units'],
                ser['heterogeneity'],
            ]
            rows.append(row)

        return rows