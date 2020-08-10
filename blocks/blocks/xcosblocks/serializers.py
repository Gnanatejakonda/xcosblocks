from rest_framework import serializers
from . import models


class CategorySerializers(serializers.ModelSerializers):
    class Meta:
        model = models.Category
        fields = [
            'id',
            'name',
            'sort_order',
        ]


class BlockDataTypeSerializers(serializers.ModelSerializers):
    class Meta:
        model = models.BlockDataType
        fields = [
            'id',
            'name',
        ]


class BlockSerializers(serializers.ModelSerializers):
    class Meta:
        model = models.Block
        fields = [
            'id',
            'name',
            'categories',
            'initial_explicit_input_ports',
            'initial_implicit_input_ports',
            'initial_explicit_output_ports',
            'initial_implicit_output_ports',
            'initial_control_ports',
            'initial_command_ports',
            'initial_display_parameter',
            'variable_explicit_input_ports',
            'variable_implicit_input_ports',
            'variable_explicit_output_ports',
            'variable_implicit_output_ports',
            'variable_control_ports',
            'variable_command_ports',
            'variable_display_parameter',
            'p000',
            'p000_type',
            'p001',
            'p001_type',
            'p002',
            'p002_type',
            'p003',
            'p003_type',
            'p004',
            'p004_type',
            'p005',
            'p005_type',
            'p006',
            'p006_type',
            'p007',
            'p007_type',
            'p008',
            'p008_type',
            'p009',
            'p009_type',
            'p010',
            'p010_type',
            'p011',
            'p011_type',
            'p012',
            'p012_type',
            'p013',
            'p013_type',
            'p014',
            'p014_type',
            'p015',
            'p015_type',
            'p016',
            'p016_type',
            'p017',
            'p017_type',
            'p018',
            'p018_type',
            'p019',
            'p019_type',
            'p020',
            'p020_type',
            'p021',
            'p021_type',
            'p022',
            'p022_type',
            'p023',
            'p023_type',
            'p024',
            'p024_type',
            'p025',
            'p025_type',
            'p026',
            'p026_type',
            'p027',
            'p027_type',
            'p028',
            'p028_type',
            'p029',
            'p029_type',
            'p030',
            'p030_type',
            'p031',
            'p031_type',
            'p032',
            'p032_type',
            'p033',
            'p033_type',
            'p034',
            'p034_type',
            'p035',
            'p035_type',
            'p036',
            'p036_type',
            'p037',
            'p037_type',
            'p038',
            'p038_type',
            'p039',
            'p039_type',
        ]
