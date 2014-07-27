from django.contrib import admin
from models import Entry

class EntryAdmin(admin.ModelAdmin):
    def _Creator_Name(self, entry):
        return entry.creator_avatar.name
    def _Owner_Name(self, entry):
        return entry.owner_avatar.name
    def _Region_Name(self, entry):
        return entry.region.name
    def _Keywords(self, entry):
        keywords = entry.keywords
        #assert isinstance(keywords, KeywordsField)
        print keywords.__dict__
        return ', '.join([str(k) for k in keywords.all()])

    list_display = ("title", "_Owner_Name", "_Creator_Name",
                    "_Region_Name", "_Keywords",
                    "mv_perm_next_copy", "mv_perm_next_mod", "mv_perm_next_trans")
    #list_filter = ("title",)
    search_fields = ("title", "owner_avatar__name", "creator_avatar__name",
                     "region__name", "keywords_string",
                     "mv_perm_next_copy", "mv_perm_next_mod", "mv_perm_next_trans")
    date_hierarchy = "created"

admin.site.register(Entry, EntryAdmin)