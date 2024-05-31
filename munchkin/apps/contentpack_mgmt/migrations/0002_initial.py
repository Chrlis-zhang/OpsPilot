# Generated by Django 4.2.7 on 2024-05-28 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('channel_mgmt', '0001_initial'),
        ('model_provider_mgmt', '0001_initial'),
        ('contentpack_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='botactions',
            name='llm_skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='model_provider_mgmt.llmskill', verbose_name='大模型技能'),
        ),
        migrations.AddField(
            model_name='botactionrule',
            name='bot_action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contentpack_mgmt.botactions', verbose_name='动作'),
        ),
        migrations.AddField(
            model_name='botactionrule',
            name='channel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='channel_mgmt.channel', verbose_name='生效通道'),
        ),
        migrations.AddField(
            model_name='botactionrule',
            name='rule_user',
            field=models.ManyToManyField(blank=True, null=True, to='channel_mgmt.channeluser', verbose_name='生效用户'),
        ),
        migrations.AddField(
            model_name='botactionrule',
            name='rule_user_groups',
            field=models.ManyToManyField(blank=True, null=True, to='channel_mgmt.channelusergroup', verbose_name='生效用户组'),
        ),
    ]