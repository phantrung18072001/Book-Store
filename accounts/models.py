from django.core.checks.messages import Error
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, name, username, phone, email, password=None):
        if not email:
            raise ValueError('Email address is required')

        if not username:
            raise ValueError('User name is required')

        # Tạo đối tượng user mới
        user = self.model(
            email=self.normalize_email(email=email),    # Chuyển email về dạng bình thường
            username=username,
            name=name,
            phone=phone,
        )
        user.set_password(password)
        user.is_admin=True
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, phone, username, password):
        user = self.create_user(
            email=self.normalize_email(email=email),
            username=username,
            password=password,
            name=name,
            phone=phone,
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=500,null=True)
    birth = models.DateTimeField(null=True)
    image = models.ImageField(null=True)
    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'    # Trường quyêt định khi login
    REQUIRED_FIELDS = ['email', 'name', 'phone']    # Các trường yêu cầu khi đk tài khoản (mặc định đã có email), mặc định có password
    @property
    def is_staff(self):
        return self.is_admin

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin    # Admin có tất cả quyền trong hệ thống

    def has_module_perms(self, add_label):
        return True