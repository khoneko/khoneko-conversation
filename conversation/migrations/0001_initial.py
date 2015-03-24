# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

from compat import USER_MODEL

class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Conversation'
        db.create_table(u'conversation_conversation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'conversation', ['Conversation'])

        # Adding M2M table for field users on 'Conversation'
        m2m_table_name = db.shorten_name(u'conversation_conversation_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('conversation', models.ForeignKey(orm[u'conversation.conversation'], null=False)),
            ('user', models.ForeignKey(USER_MODEL['orm_label'], null=False))
        ))
        db.create_unique(m2m_table_name, ['conversation_id', 'user_id'])

        # Adding model 'Message'
        db.create_table(u'conversation_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='messages', to=USER_MODEL['orm_label'])),
            ('conversation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='messages', to=orm['conversation.Conversation'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=2048)),
        ))
        db.send_create_signal(u'conversation', ['Message'])


    def backwards(self, orm):
        # Deleting model 'Conversation'
        db.delete_table(u'conversation_conversation')

        # Removing M2M table for field users on 'Conversation'
        db.delete_table(db.shorten_name(u'conversation_conversation_users'))

        # Deleting model 'Message'
        db.delete_table(u'conversation_message')


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
        USER_MODEL['model_label']: {
            'Meta': {'object_name': USER_MODEL['object_name']},
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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'conversation.conversation': {
            'Meta': {'object_name': 'Conversation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'conversations'", 'symmetrical': 'False', 'to': u"orm['%s']" % USER_MODEL['orm_label']})
        },
        u'conversation.message': {
            'Meta': {'object_name': 'Message'},
            'conversation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'messages'", 'to': u"orm['conversation.Conversation']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '2048'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'messages'", 'to': u"orm['%s']" % USER_MODEL['orm_label']})
        }
    }

    complete_apps = ['conversation']
