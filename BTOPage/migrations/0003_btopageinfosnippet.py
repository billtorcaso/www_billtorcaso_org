# Generated by Django 3.0.6 on 2020-05-24 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('BTOPage', '0002_btoinfosnippet_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='BTOPageInfoSnippet',
            fields=[
                ('btoinfosnippet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='BTOPage.BTOInfoSnippet')),
                ('link_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page')),
            ],
            bases=('BTOPage.btoinfosnippet',),
        ),
    ]
