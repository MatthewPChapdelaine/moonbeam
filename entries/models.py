from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from metaverse.models import Avatar, Region, WithPosition, WithPermissions

from mezzanine.core.models import Orderable, TimeStamped, Displayable, Ownable

class HasPreview(models.Model):
    class Meta:
        abstract = True
    tex_uuid = models.CharField(max_length=36,verbose_name=_('Texture UUID'))

class Entry(HasPreview, Displayable, Ownable, WithPosition, WithPermissions):
    class Meta:
        ordering = ['-updated', ]
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'
    # Title inherited from Displayable
    for_sale = models.BooleanField(verbose_name=_('For Sale'))
    region = models.ForeignKey(Region, verbose_name=_('Region'))
    owner_avatar = models.ForeignKey(Avatar, verbose_name=_('Owner Avatar'), related_name='entries_owner')
    creator_avatar = models.ForeignKey(Avatar, verbose_name=_('Creator Avatar'), related_name='entries_creator')
    rez_time = models.DateTimeField(_('Rez Time'))

    def get_absolute_url(self):
        """Return the redirecting URL."""
        return reverse("entry.views.entry_redirect", kwargs={'entry_slug': self.slug})

    def __unicode__(self):
        return self.title

