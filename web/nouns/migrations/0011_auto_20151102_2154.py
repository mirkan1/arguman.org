# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nouns', '0010_auto_20151102_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation',
            name='source',
            field=models.ForeignKey(related_name='out_relations', to='nouns.Noun', on_delete=models.CASCADE),
        ),
        migrations.AlterField(
            model_name='relation',
            name='target',
            field=models.ForeignKey(related_name='in_relations', to='nouns.Noun', on_delete=models.CASCADE),
        ),
    ]
