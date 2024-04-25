from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class Move(models.Model) :
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=100)
    generation_id = models.IntegerField()
    type_id = models.IntegerField()
    power = models.IntegerField()
    pp = models.IntegerField()
    priority = models.IntegerField()
    target_id = models.IntegerField()
    damage_class_id = models.IntegerField()
    effect_id = models.IntegerField()
    effect_chance = models.IntegerField()
    contest_type_id = models.IntegerField()
    contest_effect_id = models.IntegerField()
    super_contest_effect_id = models.IntegerField()

    class Meta :
        db_table = 'moves'



class Pokemon(models.Model) :
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=100)
    species_id = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    base_experience = models.IntegerField()
    order = models.IntegerField()
    is_default = models.IntegerField()


    class Meta :
        db_table = 'pokemon'



class Pokemon_Types(models.Model) :
    pokemon_id = models.IntegerField(primary_key=True)
    type_id = models.IntegerField()
    slot = models.IntegerField()


    class Meta :
        db_table = 'pokemon_types'



class Types(models.Model) :
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=100)
    generation_id = models.IntegerField()
    damage_class_id = models.IntegerField()


    class Meta :
        db_table = 'types'



class Item(models.Model):
    identifier = models.CharField(max_length=100)

    class Meta:
        db_table = 'items'







class CustomUserManager(BaseUserManager):
    def create_user(self, pseudo, password=None, **extra_fields):
        if not pseudo:
            raise ValueError('Le pseudo doit être défini')
        
        user = self.model(
            pseudo=pseudo,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, pseudo, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(pseudo, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    pseudo = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=250)
    last_login = models.DateTimeField(default=timezone.now) 
    is_superuser = models.BooleanField(default=False) 

    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'pseudo'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'user'

class Bag(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pokemon_id = models.IntegerField()

    class Meta:
        db_table = 'bag'
