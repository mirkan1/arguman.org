# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nouns', '0009_auto_20151102_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relation',
            name='from_noun',
        ),
        migrations.RemoveField(
            model_name='relation',
            name='to_noun',
        ),
        migrations.AddField(
            model_name='relation',
            name='source',
            field=models.ForeignKey(related_name='source', default=1, to='nouns.Noun', on_delete=models.CASCADE),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relation',
            name='target',
            field=models.ForeignKey(related_name='target', default=1, to='nouns.Noun', on_delete=models.CASCADE),
            preserve_default=False,
        ),
    ]
