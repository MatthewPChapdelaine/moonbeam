from django.db import models
from django.utils.translation import ugettext_lazy as _

class WithPermissionsBase(models.Model):
    class Meta:
        abstract = True
    mv_perm_own_copy = models.BooleanField(verbose_name=_('Copy'))
    mv_perm_own_mod = models.BooleanField(verbose_name=_('Modify'))
    mv_perm_own_trans = models.BooleanField(verbose_name=_('Transfer'))
    mv_perm_next_copy = models.BooleanField(verbose_name=_('Copy'))
    mv_perm_next_mod = models.BooleanField(verbose_name=_('Modify'))
    mv_perm_next_trans = models.BooleanField(verbose_name=_('Transfer'))

class WithPosition(models.Model):
    class Meta:
        abstract = True
    position_x = models.FloatField(verbose_name=_('Position X'))
    position_y = models.FloatField(verbose_name=_('Position Y'))
    position_z = models.FloatField(verbose_name=_('Position Z'))

class AvatarBase(models.Model):
    uuid = models.CharField(max_length=36, verbose_name=_('UUID'), unique=True)
    name = models.CharField(max_length=255, verbose_name=_('Name'), unique=True)
    dob = models.DateTimeField(verbose_name=_('Date of Birth'))

    def __unicode__(self):
        return self.name

class RegionBase(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'), unique=True)

    def __unicode__(self):
        return self.name

class WithPermissions(WithPermissionsBase):
    class Meta:
        abstract = True
    pass

class Avatar(AvatarBase):
    pass

class Region(RegionBase):
    pass