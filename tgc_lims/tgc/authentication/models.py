from django.models import models
from django.contrib.auth.models import PermissionsMixin , User
from .validators import UnicodeUsernameValidator
from django.apps import apps
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.contrib import auth
from django.db.models.query_utils import Q
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):
    use_in_migrations = True

    def get_hospital_info(self, id):
        if not id:
            raise ValueError('The user id does not exist')
        user = User.objects.get(id = id)
        hospital_info = user.user_hospitalInfo
        return hospital_info

    def get_all_doctors(self, id):
        if not id:
            raise ValueError("The User Id doesnot exist")
        user = User.objects.get(id = id)

    def get_full_name(self, user):
        """
        Return the First Name + Last Name with a space in between 

        Args:
            user (_type_): _description_
        """
        user = User.objects.get(id = user)
        first_name = user.user_employee.first_name
        last_name = user.user_employee.last_name
        full_name = f"{first_name} {last_name}"
        return full_name.strip()

    def get_all_employees(self):
        """
        Get Only Employee of TGC
        """
        all_employees = User.objects.filter(Q(is_admin = True) | Q(is_user = True), is_active = True).order_by('id')
        return all_employees

    def get_employee_id(self, id):
        if not id:
            raise ValueError("The User id does not exist")
        user = User.objects.get(id = id)
        employee_id = user.user_employee.id
        return employee_id

    def _create_user(self, username, password, **extra_fields):
        """Create and save a user with the given username and password

        Args:
            username (_type_): _description_
            password (_type_): _description_
        """
        if not username :
            raise ValueError("The given username must be set")

        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("SuperUser must have is_staff = True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser =True")
        return self._create_user(username, password, **extra_fields)

    def with_perm(self, perm, is_active = True, include_superusers =True, backend=None, obj=None):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)

            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError("You have multiple authentication backends configured "
                " Therefore must provide the backend argument")
        elif not isinstance(backend, str):
            raise TypeError("backend mustbe a dotted impot path string got %r"%backend)