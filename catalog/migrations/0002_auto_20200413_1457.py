# Generated by Django 3.0.5 on 2020-04-13 14:57

from django.db import migrations
import json


def get_data_or_none(data, key):
    try:
        return data[key]
    except KeyError:
        return None


def json_to_models(apps, schema_editor):
    Mineral = apps.get_model('catalog', 'Mineral')
    with open('catalog/data/minerals.json') as jsonfile:
        minerals = json.load(jsonfile)
        for mineral in minerals:
            m = Mineral(
                name=get_data_or_none(mineral, 'name'),
                image_filename=get_data_or_none(mineral, 'image_filename'),
                image_caption=get_data_or_none(mineral, 'image_caption'),
                category=get_data_or_none(mineral, 'category'),
                formula=get_data_or_none(mineral, 'formula'),
                strunz_classification=get_data_or_none(
                    mineral, 'strunz_classification'),
                crystal_system=get_data_or_none(mineral, 'crystal_system'),
                unit_cell=get_data_or_none(mineral, 'unit_cell'),
                color=get_data_or_none(mineral, 'color'),
                crystal_symmetry=get_data_or_none(
                    mineral, 'crystal_symmetry'),
                cleavage=get_data_or_none(mineral, 'cleavage'),
                mohs_scale_hardness=get_data_or_none(
                    mineral, 'mohs_scale_hardness'),
                luster=get_data_or_none(mineral, 'luster'),
                streak=get_data_or_none(mineral, 'streak'),
                diaphaneity=get_data_or_none(mineral, 'diaphaneity'),
                optical_properties=get_data_or_none(
                    mineral, 'optical_properties'),
                refractive_index=get_data_or_none(
                    mineral, 'refractive_index'),
                crystal_habit=get_data_or_none(mineral, 'crystal_habit')
            )
            print(m.name)
            m.save()


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(json_to_models),
    ]
