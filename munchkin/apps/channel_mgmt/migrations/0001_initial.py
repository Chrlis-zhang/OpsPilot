# Generated by Django 4.2.7 on 2024-06-21 02:43

import apps.core.mixinx
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_yaml_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('channel_type', models.CharField(choices=[('enterprise_wechat', '企业微信'), ('enterprise_wechat_bot', '企业微信机器人'), ('ding_talk', '钉钉'), ('web', 'Web'), ('gitlab', 'GitLab')], max_length=100, verbose_name='类型')),
                ('channel_config', django_yaml_field.fields.YAMLField(blank=True, null=True, verbose_name='通道配置')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '消息通道',
                'verbose_name_plural': '消息通道',
            },
            bases=(models.Model, apps.core.mixinx.EncryptableMixin),
        ),
        migrations.CreateModel(
            name='ChannelUserGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channel_mgmt.channel', verbose_name='通道')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '消息通道用户组',
                'verbose_name_plural': '消息通道用户组',
                'unique_together': {('channel', 'name')},
            },
        ),
        migrations.CreateModel(
            name='ChannelUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=100, verbose_name='用户ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='名称')),
                ('channel_user_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channel_mgmt.channelusergroup', verbose_name='通道用户组')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '消息通道用户',
                'verbose_name_plural': '消息通道用户',
            },
        ),
    ]
