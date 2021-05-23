from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils import timezone


class User(AbstractUser):
    """Default user for VigoLend."""


    # USER CHOICES

    KYC_STATUS = (
        ('unverified', _('Unverified')),
        ('pending', _('Pending')),
        ('verified', _('Verified')),
        ('action_required', _('Action_required')),
        ('cancelled', _('Cancelled')),
        ('rejected', _('Rejected/Refused'))
    )
  
    #: First and last name do not cover name patterns around the globe
    id = models.UUIDField(
        default = uuid.uuid4,
        editable=False,
        primary_key=True,
        help_text=_("The unique identifier of the customer.")
    )

    name = CharField(_("Name of User"), blank=True, max_length=255)

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

    current_address = models.CharField(
        max_length=250,
        verbose_name=_("Current address"),
        blank=True,
        null=True,
        help_text=_("The currently living address of the customer.")
    )

    permanent_address = models.CharField(
        max_length=250,
        verbose_name=_("Permanent address"),
        blank=True,
        null=True,
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

    country_of_residence = models.CharField(
        max_length=250,
        verbose_name=_("Country of Residence"),
        blank=True, null=True,
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
