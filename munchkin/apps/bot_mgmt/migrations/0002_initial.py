# Generated by Django 4.2.7 on 2024-08-01 02:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('channel_mgmt', '0001_initial'),
        ('model_provider_mgmt', '0001_initial'),
        ('bot_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='botskillrule',
            name='llm_skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='model_provider_mgmt.llmskill', verbose_name='LLM技能'),
        ),
        migrations.AddField(
            model_name='botskillrule',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='botskillrule',
            name='rule_user',
            field=models.ManyToManyField(blank=True, to='channel_mgmt.channeluser', verbose_name='生效用户'),
        ),
        migrations.AddField(
            model_name='botskillrule',
            name='rule_user_groups',
            field=models.ManyToManyField(blank=True, to='channel_mgmt.channelusergroup', verbose_name='生效用户组'),
        ),
        migrations.AddField(
            model_name='botconversationhistory',
            name='bot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot_mgmt.bot', verbose_name='机器人'),
        ),
        migrations.AddField(
            model_name='botconversationhistory',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='botconversationhistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channel_mgmt.channeluser', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='bot',
            name='channels',
            field=models.ManyToManyField(blank=True, to='channel_mgmt.channel', verbose_name='通道'),
        ),
        migrations.AddField(
            model_name='bot',
            name='integration',
            field=models.ManyToManyField(blank=True, to='bot_mgmt.integration', verbose_name='集成'),
        ),
        migrations.AddField(
            model_name='bot',
            name='llm_skills',
            field=models.ManyToManyField(blank=True, to='model_provider_mgmt.llmskill', verbose_name='LLM技能'),
        ),
        migrations.AddField(
            model_name='bot',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bot',
            name='rasa_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot_mgmt.rasamodel', verbose_name='模型'),
        ),
        migrations.AddField(
            model_name='automationskill',
            name='integration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot_mgmt.integration', verbose_name='集成'),
        ),
        migrations.AddField(
            model_name='automationskill',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL),
        ),
    ]
