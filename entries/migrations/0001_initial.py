# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Entry'
        db.create_table(u'entries_entry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'keywords_string', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('_meta_title', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gen_description', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('short_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('in_sitemap', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'entrys', to=orm['auth.User'])),
            ('mv_perm_own_copy', self.gf('django.db.models.fields.BooleanField')()),
            ('mv_perm_own_mod', self.gf('django.db.models.fields.BooleanField')()),
            ('mv_perm_own_trans', self.gf('django.db.models.fields.BooleanField')()),
            ('mv_perm_next_copy', self.gf('django.db.models.fields.BooleanField')()),
            ('mv_perm_next_mod', self.gf('django.db.models.fields.BooleanField')()),
            ('mv_perm_next_trans', self.gf('django.db.models.fields.BooleanField')()),
            ('position_x', self.gf('django.db.models.fields.FloatField')()),
            ('position_y', self.gf('django.db.models.fields.FloatField')()),
            ('position_z', self.gf('django.db.models.fields.FloatField')()),
            ('tex_uuid', self.gf('django.db.models.fields.CharField')(max_length=36)),
            ('for_sale', self.gf('django.db.models.fields.BooleanField')()),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['metaverse.Region'])),
            ('owner_avatar', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entries_owner', to=orm['metaverse.Avatar'])),
            ('creator_avatar', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entries_creator', to=orm['metaverse.Avatar'])),
            ('rez_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'entries', ['Entry'])


    def backwards(self, orm):
        # Deleting model 'Entry'
        db.delete_table(u'entries_entry')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'entries.entry': {
            'Meta': {'ordering': "['-updated']", 'object_name': 'Entry'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'creator_avatar': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries_creator'", 'to': u"orm['metaverse.Avatar']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'for_sale': ('django.db.models.fields.BooleanField', [], {}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'mv_perm_next_copy': ('django.db.models.fields.BooleanField', [], {}),
            'mv_perm_next_mod': ('django.db.models.fields.BooleanField', [], {}),
            'mv_perm_next_trans': ('django.db.models.fields.BooleanField', [], {}),
            'mv_perm_own_copy': ('django.db.models.fields.BooleanField', [], {}),
            'mv_perm_own_mod': ('django.db.models.fields.BooleanField', [], {}),
            'mv_perm_own_trans': ('django.db.models.fields.BooleanField', [], {}),
            'owner_avatar': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries_owner'", 'to': u"orm['metaverse.Avatar']"}),
            'position_x': ('django.db.models.fields.FloatField', [], {}),
            'position_y': ('django.db.models.fields.FloatField', [], {}),
            'position_z': ('django.db.models.fields.FloatField', [], {}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'rez_time': ('django.db.models.fields.DateTimeField', [], {}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['metaverse.Region']"}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'tex_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'entrys'", 'to': u"orm['auth.User']"})
        },
        u'metaverse.avatar': {
            'Meta': {'object_name': 'Avatar', '_ormbases': [u'metaverse.AvatarBase']},
            u'avatarbase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['metaverse.AvatarBase']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'metaverse.avatarbase': {
            'Meta': {'object_name': 'AvatarBase'},
            'dob': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36'})
        },
        u'metaverse.region': {
            'Meta': {'object_name': 'Region', '_ormbases': [u'metaverse.RegionBase']},
            u'regionbase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['metaverse.RegionBase']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'metaverse.regionbase': {
            'Meta': {'object_name': 'RegionBase'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['entries']