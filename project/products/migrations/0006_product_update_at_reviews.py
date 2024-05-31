# Generated by Django 4.2.6 on 2024-04-27 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_wishlist_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='update_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField(blank=True, null=True)),
                ('r_image', models.ImageField(blank=True, null=True, upload_to='reviews/')),
                ('date', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
