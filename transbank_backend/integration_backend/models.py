from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Usuario (models.Model):
    id_usuario = models.AutoField(primary_key = True)
    primer_nombre = models.CharField(max_length= 50, default= "")
    segundo_nombre = models.CharField(max_length= 50, default= "", null = True)
    apellido_paterno = models.CharField(max_length= 50, default= "")
    apellido_materno = models.CharField(max_length= 50, default= "", null = True)
    email = models.EmailField(default= "", null = True)
    rut = models.CharField(max_length=12, null = True)
    fecha_nacimiento = models.DateField(default= None, null = True)
    auth_user_id = models.ForeignKey(User, null = False, on_delete = models.DO_NOTHING, db_column = 'auth_user_id')

    def __str__ (self):
        return str(self.id_usuario)

    class Meta:
        ordering = ['id_usuario']
        db_table = 'MAESTRO_USUARIOS'

class Perfiles (models.Model):
    id_perfil = models.AutoField(primary_key= True)
    nombre_perfil = models.CharField(max_length= 75)

    def __str__ (self):
        return str(self.id_perfil)

    class Meta:
        ordering = ['id_perfil']
        db_table = 'MAESTRO_PERFILES'

class PerfilesUsuario (models.Model):
    id_registro = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, null= False, on_delete= models.DO_NOTHING, db_column = 'id_usuario')
    id_perfil = models.ForeignKey(Perfiles, null = False, on_delete= models.DO_NOTHING, db_column = 'id_perfil')

    class Meta:
        ordering = ['id_usuario', 'id_perfil']
        db_table = 'MAESTRO_ASOC_USUARIO_PERFILES'

class ModulosPerfiles (models.Model):
    id_registro = models.AutoField(primary_key=True)
    id_perfil = models.ForeignKey(Perfiles, null = False, on_delete= models.DO_NOTHING, db_column = 'id_perfil')
    id_modulo = models.ForeignKey('Modulos', null = False, on_delete= models.DO_NOTHING, db_column = 'id_modulo')

    class Meta:
        ordering = ['id_perfil', 'id_modulo']
        db_table = 'MAESTRO_ASOC_MODULO_PERFILES'