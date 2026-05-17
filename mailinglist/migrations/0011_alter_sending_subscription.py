from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailinglist', '0010_alter_mailinglist_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sending',
            name='subscription',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='mailinglist.subscription',
            ),
        ),
    ]
