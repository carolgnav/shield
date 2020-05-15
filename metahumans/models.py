from django.db import models

# Create your models here.

class Power(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=300)
    level = models.IntegerField(default=50)

    def __str__(self):
        return f'{self.name}: {self.description}'


COUNTRIES = [
    ('US', 'United states'),
    ('ES', 'Spain'),
    ('UK', 'United Kingdom'),
    ('OT', "Others"),
    ]


class Team(models.Model):

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

    name = models.CharField(max_length=220)
    description = models.TextField(max_length=4000)
    headquarter =  models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class MetaHuman(models.Model):
    
    class Meta:
        verbose_name = "Metahumano"
        verbose_name_plural = "Metahumanos"

    name = models.CharField(max_length=42)
    country = models.CharField(max_length=2, choices=COUNTRIES)
    level = models.IntegerField(default=10)
    active = models.BooleanField(default=True, editable=False)
    ally = models.BooleanField(default=True)
    powers = models.ManyToManyField(Power)
    last_update = models.DateTimeField(auto_now=True)
    team = models.ForeignKey(
            Team,
            on_delete=models.PROTECT,
            blank=True,
            null=True,
            default=None,
        )

    def __str__(self):
        return self.name














