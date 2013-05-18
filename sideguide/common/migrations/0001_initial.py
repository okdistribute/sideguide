# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Organization'
        db.create_table(u'common_organization', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'common', ['Organization'])

        # Adding M2M table for field owners on 'Organization'
        db.create_table(u'common_organization_owners', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organization', models.ForeignKey(orm[u'common.organization'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(u'common_organization_owners', ['organization_id', 'user_id'])

        # Adding M2M table for field members on 'Organization'
        db.create_table(u'common_organization_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organization', models.ForeignKey(orm[u'common.organization'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(u'common_organization_members', ['organization_id', 'user_id'])

        # Adding model 'Collection'
        db.create_table(u'common_collection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('org', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Organization'], null=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('points', self.gf('django.contrib.gis.db.models.fields.MultiPointField')()),
        ))
        db.send_create_signal(u'common', ['Collection'])

        # Adding model 'Stop'
        db.create_table(u'common_stop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('org', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Organization'], null=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('audio', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('collection', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Collection'], null=True)),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal(u'common', ['Stop'])

        # Adding M2M table for field coperanda on 'Stop'
        db.create_table(u'common_stop_coperanda', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_stop', models.ForeignKey(orm[u'common.stop'], null=False)),
            ('to_stop', models.ForeignKey(orm[u'common.stop'], null=False))
        ))
        db.create_unique(u'common_stop_coperanda', ['from_stop_id', 'to_stop_id'])


    def backwards(self, orm):
        # Deleting model 'Organization'
        db.delete_table(u'common_organization')

        # Removing M2M table for field owners on 'Organization'
        db.delete_table('common_organization_owners')

        # Removing M2M table for field members on 'Organization'
        db.delete_table('common_organization_members')

        # Deleting model 'Collection'
        db.delete_table(u'common_collection')

        # Deleting model 'Stop'
        db.delete_table(u'common_stop')

        # Removing M2M table for field coperanda on 'Stop'
        db.delete_table('common_stop_coperanda')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'common.collection': {
            'Meta': {'object_name': 'Collection'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'org': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Organization']", 'null': 'True'}),
            'points': ('django.contrib.gis.db.models.fields.MultiPointField', [], {})
        },
        u'common.organization': {
            'Meta': {'object_name': 'Organization'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'mem+'", 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'owners': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'own+'", 'symmetrical': 'False', 'to': u"orm['auth.User']"})
        },
        u'common.stop': {
            'Meta': {'object_name': 'Stop'},
            'audio': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Collection']", 'null': 'True'}),
            'coperanda': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'coperanda_rel_+'", 'to': u"orm['common.Stop']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'org': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Organization']", 'null': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['common']