# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Exhibition'
        db.create_table('exhibitions_exhibition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('slug', self.gf('apps.slugify.fields.SlugifyField')(max_length=50, populate_from=('name',))),
        ))
        db.send_create_signal('exhibitions', ['Exhibition'])

        # Adding M2M table for field artists on 'Exhibition'
        db.create_table('exhibitions_exhibition_artists', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('exhibition', models.ForeignKey(orm['exhibitions.exhibition'], null=False)),
            ('artist', models.ForeignKey(orm['artists.artist'], null=False))
        ))
        db.create_unique('exhibitions_exhibition_artists', ['exhibition_id', 'artist_id'])

        # Adding model 'ExhibitionPhoto'
        db.create_table('exhibitions_exhibitionphoto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('exhibition', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['exhibitions.Exhibition'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('exhibitions', ['ExhibitionPhoto'])


    def backwards(self, orm):
        # Deleting model 'Exhibition'
        db.delete_table('exhibitions_exhibition')

        # Removing M2M table for field artists on 'Exhibition'
        db.delete_table('exhibitions_exhibition_artists')

        # Deleting model 'ExhibitionPhoto'
        db.delete_table('exhibitions_exhibitionphoto')


    models = {
        'artists.artist': {
            'Meta': {'ordering': "['last_name', 'first_name']", 'unique_together': "(('first_name', 'last_name'),)", 'object_name': 'Artist'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'resume': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('apps.slugify.fields.SlugifyField', [], {'max_length': '50', 'populate_from': "('first_name', 'last_name')"}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'exhibitions.exhibition': {
            'Meta': {'ordering': "['-start_date']", 'object_name': 'Exhibition'},
            'artists': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'exhibitions'", 'symmetrical': 'False', 'to': "orm['artists.Artist']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slug': ('apps.slugify.fields.SlugifyField', [], {'max_length': '50', 'populate_from': "('name',)"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'exhibitions.exhibitionphoto': {
            'Meta': {'ordering': "['position']", 'object_name': 'ExhibitionPhoto'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'exhibition': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['exhibitions.Exhibition']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['exhibitions']