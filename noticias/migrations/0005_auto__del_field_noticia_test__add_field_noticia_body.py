# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'noticia.test'
        db.delete_column(u'noticias_noticia', 'test')

        # Adding field 'noticia.body'
        db.add_column(u'noticias_noticia', 'body',
                      self.gf('django.db.models.fields.TextField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'noticia.test'
        db.add_column(u'noticias_noticia', 'test',
                      self.gf('django.db.models.fields.TextField')(default=1),
                      keep_default=False)

        # Deleting field 'noticia.body'
        db.delete_column(u'noticias_noticia', 'body')


    models = {
        u'noticias.noticia': {
            'Meta': {'object_name': 'noticia'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['noticias']