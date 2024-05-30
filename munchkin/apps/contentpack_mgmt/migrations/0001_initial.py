# Generated by Django 4.2.7 on 2024-05-28 07:38

from django.db import migrations, models
import django.db.models.deletion
import django_minio_backend.models
import django_yaml_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotActionRule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='规则名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('prompt', models.TextField(blank=True, null=True, verbose_name='技能提示词')),
            ],
            options={
                'verbose_name': '动作规则',
                'verbose_name_plural': '动作规则',
            },
        ),
        migrations.CreateModel(
            name='ContentPack',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='扩展包名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '扩展包',
                'verbose_name_plural': '扩展包',
            },
        ),
        migrations.CreateModel(
            name='Intent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='意图名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('content_pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contentpack_mgmt.contentpack', verbose_name='扩展包')),
            ],
            options={
                'verbose_name': '意图',
                'verbose_name_plural': '意图',
            },
        ),
        migrations.CreateModel(
            name='RasaResponse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='回复名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('content_pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contentpack_mgmt.contentpack', verbose_name='扩展包')),
            ],
            options={
                'verbose_name': '回复',
                'verbose_name_plural': '回复',
            },
        ),
        migrations.CreateModel(
            name='RasaStories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='故事名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('story', django_yaml_field.fields.YAMLField(default={'steps': [{'intent': 'intent_name'}]}, verbose_name='故事')),
                ('content_pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contentpack_mgmt.contentpack', verbose_name='扩展包')),
            ],
            options={
                'verbose_name': '故事',
                'verbose_name_plural': '故事',
            },
        ),
        migrations.CreateModel(
            name='RasaSlots',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='槽位名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('slot', django_yaml_field.fields.YAMLField(default={'slot_name': {'influence_conversation': True, 'mappings': [{'type': 'custom'}], 'type': 'text'}}, verbose_name='槽位')),
                ('content_pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contentpack_mgmt.contentpack', verbose_name='扩展包')),
            ],
            options={
                'verbose_name': '槽位',
                'verbose_name_plural': '槽位',
            },
        ),
        migrations.CreateModel(
            name='RasaRules',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='规则名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('rule_steps', django_yaml_field.fields.YAMLField(default={'steps': [{'intent': 'intent_name'}]}, verbose_name='规则')),
                ('content_pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contentpack_mgmt.contentpack', verbose_name='扩展包')),
            ],
            options={
                'verbose_name': '规则',
                'verbose_name_plural': '规则',
            },
        ),
        migrations.CreateModel(
            name='RasaResponseCorpus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('corpus', models.TextField(verbose_name='语料')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contentpack_mgmt.rasaresponse', verbose_name='回复')),
            ],
            options={
                'verbose_name': '回复语料',
                'verbose_name_plural': '回复语料',
            },
        ),
        migrations.CreateModel(
            name='RasaModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='模型名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('model_file', models.FileField(blank=True, null=True, storage=django_minio_backend.models.MinioBackend(bucket_name='munchkin-private'), upload_to='rasa_models', verbose_name='文件')),
                ('train_data_file', models.FileField(blank=True, null=True, storage=django_minio_backend.models.MinioBackend(bucket_name='munchkin-private'), upload_to='rasa_train_data', verbose_name='训练数据')),
                ('pipeline_config', django_yaml_field.fields.YAMLField(default={'pipeline': [{'case_sensitive': True, 'name': 'KeywordIntentClassifier'}, {'ambiguity_threshold': 0.1, 'name': 'FallbackClassifier', 'threshold': 0.7}]}, verbose_name='模型配置')),
                ('policies_config', django_yaml_field.fields.YAMLField(default={'policies': [{'core_fallback_action_name': 'action_llm_fallback', 'core_fallback_threshold': 0.4, 'name': 'RulePolicy'}]}, verbose_name='策略配置')),
                ('content_packs', models.ManyToManyField(blank=True, null=True, to='contentpack_mgmt.contentpack', verbose_name='扩展包')),
            ],
            options={
                'verbose_name': '模型',
                'verbose_name_plural': '模型',
            },
        ),
        migrations.CreateModel(
            name='RasaForms',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='表单名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('form', django_yaml_field.fields.YAMLField(default={'form_name': {'required_slots': ['slot_name']}}, verbose_name='表单')),
                ('content_pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contentpack_mgmt.contentpack', verbose_name='扩展包')),
            ],
            options={
                'verbose_name': '表单',
                'verbose_name_plural': '表单',
            },
        ),
        migrations.CreateModel(
            name='RasaEntity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='实体名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('content_pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contentpack_mgmt.contentpack', verbose_name='扩展包')),
            ],
            options={
                'verbose_name': '实体',
                'verbose_name_plural': '实体',
            },
        ),
        migrations.CreateModel(
            name='IntentCorpus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('corpus', models.TextField(verbose_name='语料')),
                ('intent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contentpack_mgmt.intent', verbose_name='意图')),
            ],
            options={
                'verbose_name': '意图语料',
                'verbose_name_plural': '意图语料',
            },
        ),
        migrations.CreateModel(
            name='BotActions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('action_llm_fallback', '开放型对话'), ('action_external_utter', '人工介入')], max_length=255, verbose_name='动作名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('content_pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contentpack_mgmt.contentpack', verbose_name='扩展包')),
            ],
            options={
                'verbose_name': '动作',
                'verbose_name_plural': '动作',
            },
        ),
    ]
