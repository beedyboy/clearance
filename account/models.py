from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager)
from django.db import models
from system.models import SemesterData, DepartmentData
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, user_id, first_name, last_name, password= None):

        if not user_id:
            raise ValueError("Users must have a valid identification number")

        user_obj = self.model(
          user_id=user_id
        )
        # check if the password is passed
        if not password:
            raise ValueError("User must have a password")

        user_obj.set_password(password)
        user_obj.first_name = first_name
        user_obj.last_name = last_name
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self,user_id, first_name, last_name, password= None):

        user = self.create_user(
            user_id,
            first_name = first_name,
            last_name = last_name,
            password = password

        )

        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, first_name, last_name, password=None):

        user = self.create_user(
            user_id,
            first_name=first_name,
            last_name=last_name,
            password=password

        )

        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    # add additional fields here
    user_id = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    active = models.BooleanField(default=True)# can login
    staff = models.BooleanField(default=False)  # staff user non superuser
    admin = models.BooleanField(default=False)  # superuser

    USER_TYPE_CHOICES = (
        (1, 'student'),
        (2, 'lecturer'),
        (3, 'bursary'),
        (4, 'system'),
        (5, 'admin'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'user_type']

    objects = UserManager()

    def __str__(self):
        return self.user_id

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_user_type(self):
            return self.user_type

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    @property
    def is_active(self):
        return self.active


class StudentProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    semester = models.ForeignKey(SemesterData, on_delete=models.SET_NULL, null=True)
    dept_name = models.ForeignKey(DepartmentData, on_delete=models.SET_NULL, null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.user.first_name


# @receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.admin:
            pass
        else:
            data = StudentProfile.id
            print(data)
            StudentProfile.objects.create(user=instance)
    # else:
    #     instance.StudentProfile.save()


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()