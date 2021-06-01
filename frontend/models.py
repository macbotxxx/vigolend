from helpers.common.basemodel import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class TeamMember (BaseModel):
    """
        Entity represents a team member
    """
    

    name = models.CharField(
        verbose_name=_("Team Member name"),
        max_length=50, 
        null=True, blank=True,
        help_text=_('Team member full name')
        )

    designation = models.CharField(
        verbose_name=_("Designation"),
        max_length=50, 
        null=True, blank=True,
        help_text=_('The position of the team member.') 
        )

    facebook = models.CharField(
        verbose_name=_("Facebook link"),
        max_length=50, 
        null=True, blank=True,
        help_text=_('The facebook link of the team member.')
        )

    twitter = models.CharField(
        verbose_name=_("Twitter Handle"),
        max_length=50, 
        null=True, blank=True,
        help_text=_('The twitter handle- without `@`.')
        )

    photo = models.ImageField(
        verbose_name=_("Profile Image"),
        null=True, blank=True,
        upload_to = 'images',
        help_text = _("Photo of the team member.")   
        )
    #Metadata
    class Meta :
        verbose_name = _("Team Member")
        verbose_name_plural = _("Team Member")

    #Methods
    #    def get_absolute_url(self):
    #        return reverse('url', args=[args])

    def __str__(self):
        return self.name
