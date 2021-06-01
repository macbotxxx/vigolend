from locations.models import Country
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils import timezone



class UserAddress(models.Model):

     # CHOICES
    ADDRESS_TYPE = (
        ('current', _('Current Address')),
        ('permanent', _("Permanent Address"))
    )

    id = models.UUIDField(
        default = uuid.uuid4,
        editable=False,
        primary_key=True,
        help_text=_("The unique identifier of the customer.")
    )

    type = models.CharField(
        choices=ADDRESS_TYPE,
        max_length=9,
        help_text=_("The type of address."),
        default='current',
        verbose_name=_("Address Type")
    )

    user = models.ForeignKey(
        'User',
        verbose_name=_("User Profile"),
        on_delete=models.PROTECT,
        help_text=_("The user for whom address belongs to")
    )

    address_line_1 = models.CharField(
        verbose_name=_("Address line 1"),
        null=True, blank=True,
        max_length=50,
        help_text='Address line 1 of the user')

    address_line_2 = models.CharField(
        verbose_name=_("Address line 2"),
        null=True, blank=True,
        max_length=50,
        help_text='Address line 2 of the user')

    state = models.CharField(
        verbose_name=_("State or Region"),
        null=True, blank=True,
        max_length=50,
        help_text='State or Region of the user')

    city = models.CharField(
        verbose_name=_("City"),
        max_length=50,
        null=True, blank=True,
        help_text=_("The city of the address of the user."))

    zip_post_code = models.CharField(
        verbose_name=_("Zip Post Code"),
        max_length=50,
        null=True, blank=True,
        help_text='Zip post code of the user address')

    country = models.ForeignKey(
        Country,
        verbose_name=_("Country"),
        null=True, blank=True,
        on_delete=models.PROTECT,
        help_text='Country of the user')

   
    #Metadata
    class Meta :
        verbose_name = _("User Address")
        verbose_name_plural = _("User Address")


    def __str__(self):
       return self.user.name


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError(_('The given email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Default user for VigoLend."""


    objects = UserManager()

    # USER CHOICES

    KYC_STATUS = (
        ('unverified', _('Unverified')),
        ('pending', _('Pending')),
        ('verified', _('Verified')),
        ('action_required', _('Action_required')),
        ('cancelled', _('Cancelled')),
        ('rejected', _('Rejected/Refused'))
    )

    ACCOUNT_TYPE = (
        ('borrower', _('Borrower')),
        ('investor', _('Investor')),
    )
  
    #: First and last name do not cover name patterns around the globe
    id = models.UUIDField(
        default = uuid.uuid4,
        editable=False,
        primary_key=True,
        help_text=_("The unique identifier of the customer.")
    )


    account_type = CharField(
        verbose_name=_("Name of User"),
        choices=ACCOUNT_TYPE,
        blank=True, max_length=8,
        help_text=_("Account type"))

    name = CharField(_("Name of User"), blank=True, max_length=255)

    email = models.EmailField(
        max_length=150,
        blank=True, null=True,
        unique=True,
        verbose_name=_("Email Address"),
        help_text=_("The email address of the customer.")
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    username = None

    first_name = models.CharField(
        verbose_name=_("First names"),
        max_length=50,
        blank=True,
        null=True,
        help_text=_("The first nammes of the customer.")
    )

    last_name = models.CharField(
        max_length=50,
        verbose_name=_("Last names"),
        blank=True,
        null=True,
        help_text=_("The last nammes of the customer.")
    )

    current_address = models.ForeignKey(
        UserAddress,
        verbose_name=_("Current address"),
        blank=True,null=True,
        on_delete=models.PROTECT,
        related_name= '+',
        help_text=_("The currently living address of the customer.")
    )

    permanent_address = models.ForeignKey(
        UserAddress,
        verbose_name=_("Permanent address"),
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name= '+',
        help_text=_("The current permanent address of the customer.")
    )

    contact_number = models.CharField(
        max_length=50,
        verbose_name=_("Contact number"),
        blank=True,
        null=True,
        help_text=_("The contact number of the customer.")
    )

    date_of_birth = models.DateField(
        verbose_name=_("Date of birth"),
        blank=True,
        null=True,
        help_text=_("The date of birth of the customer.")
    )

    kyc_complete = models.BooleanField(
        verbose_name=_("KYC complete"),
        default=False,
        help_text=_("Flag to determine if a cutomer have completed KYC verification")
    )

    kyc_complete_date = models.DateTimeField(
        verbose_name=_("KYC complete date"),
        blank=True,
        null=True,
        help_text=_("Timestamp when customer completed KYC verifiction process.")
    )

    kyc_status = models.CharField(
        max_length=15,
        verbose_name=_("KYC status"),
        choices=KYC_STATUS,
        default='Unverified',
        blank=True,
        null=True,
        help_text=_("The .")
    )

    on_boarding_complete = models.BooleanField(
        verbose_name=_("Completed Onboarding"),
        blank=True,null=True,
        help_text=_("Flag to determine if customer has completed onboarding.")
    )

    on_boarding_complete_date = models.DateField(
        verbose_name=_("Onboarding Complete date"),
        blank=True,
        null=True,
        help_text=_("Timestamp when customer completed onboarding process.")
    )

    kyc_submitted = models.BooleanField(
        verbose_name=_("KYC submitted"),
        blank=True,null=True,
        help_text=_("Flag to determine if customer has submitted a KYC verification.")
    )

    social_security_number = models.CharField(
        verbose_name=_("Social security number"),
        max_length=50,
        null=True, blank=True,
        help_text=_("The social security number of the customer. This helps to determine the credit score and also validates the identity of the customer. ")
    )

    place_of_birth = models.CharField(
        max_length=250,
        verbose_name=_("Place of birth"),
        blank=True, null=True,
        help_text=_("The place fo birth of the customer. This must match the place of birth as indicated in the cusomters photo Identification.")
    )

    verification_date = models.DateField(
        verbose_name=_("Verification date"),
        blank=True,
        null=True,
        editable=False,
        default=timezone.now,
        help_text=_("Timestamp when customer is been verified.")
    )

    registered_ip_address = models.GenericIPAddressField(
        verbose_name=_("Registered Ip Address"),
        blank=True, null=True,
        editable=False,
        help_text=_("The Ip address recorded at the time if registeration.")
    )

    country_of_residence = models.ForeignKey(
        Country,
        verbose_name=_("Country of Residence"),
        blank=True, null=True,
        on_delete=models.SET_NULL,
        help_text=_("The country residence of the customer. KYC verification will be applied to this country and customer must provide proof of such residence as relevant in the country of jurisdiction.")
    )

    job_title = models.CharField(
        max_length=250,
        verbose_name=_("Job title"),
        blank=True, null=True,
        help_text=_("The Job title of the customer. ")
    )

    default_currency_id = models.CharField(
        max_length=3,
        verbose_name=_("Default Currency ID"),
        blank=True, null=True,
        default='EUR',
        help_text=_("The default currency of the borrower. Currency will be sent against borrowers country of residence.")
    )

    # salutation
    # time_zone
    # pending_cash_balance
    # highest_qualification
    # passout_year
    # investment_limit
    # fund_committed
    # escrow_account_number
    # contact_number
    # tax_id

    class Meta:
        verbose_name = _("Register User")
        verbose_name_plural = _("Register Users")


    def __str__(self):
        return self.email 


    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.pk})
