from rest_framework import serializers

from .models import Category, ParameterDataType, BlockType, Block, BlockParameter


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'sort_order',
        ]


class ParameterDataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParameterDataType
        fields = [
            'id',
            'name',
        ]


class BlockTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockType
        fields = [
            'id',
            'name',
        ]


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = [
            'id',
            'blocktype',
            'name',
            'categories',
            'initial_explicit_input_ports',
            'initial_implicit_input_ports',
            'initial_explicit_output_ports',
            'initial_implicit_output_ports',
            'initial_control_ports',
            'initial_command_ports',
            'initial_display_parameter',
        ]


class BlockParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockParameter
        fields = [
            'id',
            'block',
            'p000',
            'p000_type',
            'p000_value_initial',
            'p001',
            'p001_type',
            'p001_value_initial',
            'p002',
            'p002_type',
            'p002_value_initial',
            'p003',
            'p003_type',
            'p003_value_initial',
            'p004',
            'p004_type',
            'p004_value_initial',
            'p005',
            'p005_type',
            'p005_value_initial',
            'p006',
            'p006_type',
            'p006_value_initial',
            'p007',
            'p007_type',
            'p007_value_initial',
            'p008',
            'p008_type',
            'p008_value_initial',
            'p009',
            'p009_type',
            'p009_value_initial',
            'p010',
            'p010_type',
            'p010_value_initial',
            'p011',
            'p011_type',
            'p011_value_initial',
            'p012',
            'p012_type',
            'p012_value_initial',
            'p013',
            'p013_type',
            'p013_value_initial',
            'p014',
            'p014_type',
            'p014_value_initial',
            'p015',
            'p015_type',
            'p015_value_initial',
            'p016',
            'p016_type',
            'p016_value_initial',
            'p017',
            'p017_type',
            'p017_value_initial',
            'p018',
            'p018_type',
            'p018_value_initial',
            'p019',
            'p019_type',
            'p019_value_initial',
            'p020',
            'p020_type',
            'p020_value_initial',
            'p021',
            'p021_type',
            'p021_value_initial',
            'p022',
            'p022_type',
            'p022_value_initial',
            'p023',
            'p023_type',
            'p023_value_initial',
            'p024',
            'p024_type',
            'p024_value_initial',
            'p025',
            'p025_type',
            'p025_value_initial',
            'p026',
            'p026_type',
            'p026_value_initial',
            'p027',
            'p027_type',
            'p027_value_initial',
            'p028',
            'p028_type',
            'p028_value_initial',
            'p029',
            'p029_type',
            'p029_value_initial',
            'p030',
            'p030_type',
            'p030_value_initial',
            'p031',
            'p031_type',
            'p031_value_initial',
            'p032',
            'p032_type',
            'p032_value_initial',
            'p033',
            'p033_type',
            'p033_value_initial',
            'p034',
            'p034_type',
            'p034_value_initial',
            'p035',
            'p035_type',
            'p035_value_initial',
            'p036',
            'p036_type',
            'p036_value_initial',
            'p037',
            'p037_type',
            'p037_value_initial',
            'p038',
            'p038_type',
            'p038_value_initial',
            'p039',
            'p039_type',
            'p039_value_initial',
        ]
