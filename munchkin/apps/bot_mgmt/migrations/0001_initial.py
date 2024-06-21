# Generated by Django 4.2.7 on 2024-06-21 02:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_minio_backend.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('channel_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('assistant_id', models.CharField(default='', max_length=255, verbose_name='机器人ID')),
                ('enable_bot_domain', models.BooleanField(default=False, verbose_name='启用域名')),
                ('enable_ssl', models.BooleanField(default=False, verbose_name='启用SSL')),
                ('bot_domain', models.CharField(blank=True, max_length=255, null=True, verbose_name='域名')),
                ('enable_node_port', models.BooleanField(default=False, verbose_name='启用端口映射')),
                ('node_port', models.IntegerField(default=5005, verbose_name='端口映射')),
                ('online', models.BooleanField(default=False, verbose_name='是否上线')),
            ],
            options={
                'verbose_name': '机器人',
                'verbose_name_plural': '机器人',
            },
        ),
        migrations.CreateModel(
            name='BotConversationHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('conversation_role', models.CharField(choices=[('user', '用户'), ('bot', '机器人')], max_length=255, verbose_name='对话角色')),
                ('conversation', models.TextField(verbose_name='对话内容')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '对话历史',
                'verbose_name_plural': '对话历史',
            },
        ),
        migrations.CreateModel(
            name='RasaModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='模型名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('model_file', models.FileField(blank=True, null=True, storage=django_minio_backend.models.MinioBackend(bucket_name='munchkin-private'), upload_to='rasa_models', verbose_name='文件')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '模型',
                'verbose_name_plural': '模型',
            },
        ),
        migrations.CreateModel(
            name='BotSkillRule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='规则名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('prompt', models.TextField(blank=True, null=True, verbose_name='提示词')),
                ('bot_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot_mgmt.bot', verbose_name='机器人')),
                ('channel', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='channel_mgmt.channel', verbose_name='生效通道')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('rule_user', models.ManyToManyField(blank=True, to='channel_mgmt.channeluser', verbose_name='生效用户')),
                ('rule_user_groups', models.ManyToManyField(blank=True, to='channel_mgmt.channelusergroup', verbose_name='生效用户组')),
            ],
            options={
                'verbose_name': '动作规则',
                'verbose_name_plural': '动作规则',
            },
        ),
    ]
