from django.http import HttpResponseRedirect
from django.db.models import F
from django.shortcuts import get_object_or_404
from mezzanine.generic.models import Keyword
from mezzanine.utils.views import render

from models import Entry


def entries_list(request, template="entries/list.html"):
    entries = Entry.objects.all()[:100]
    context = {}
    return render(request, template, context)


def entries_tag_list(request, keyword_slug, template="entries/tag_list.html"):
    keyword = get_object_or_404(Keyword, slug=keyword_slug)
    entries = Entry.objects.filter(tags_string__contains=keyword.title)
    return render(request, template, {'keyword': keyword, 'entries': entries})


def entries_redirect(request, entry_slug):
    """Increment the Dumps ``views`` count and redirect to the URL or 404."""
    entry = get_object_or_404(Entry, slug=entry_slug)
    Entry.objects.filter(slug=entry_slug).update(views=F('views') + 1)
    return HttpResponseRedirect(entry.link)