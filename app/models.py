from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import EmailField
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(UserManager):
    """Define a model manager for User model with mandatory email field."""

    # The function is basically the same. I added only the if statement
    # to check whether email is present

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    """User model."""

    # Email field has to be unique since it will be used to login.

    email = EmailField(
        _('email address'),
        unique=True,
        help_text=_('Required.'),
        error_messages={
            'unique': _("A user with that email address already exists."),
        },
    )

    # Email is already required as the USERNAME_FIELD

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()
