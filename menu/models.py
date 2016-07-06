from django.db import models
from wagtail.wagtailcore.models import Orderable
from modelcluster.fields import ParentalKey
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from modelcluster.models import ClusterableModel


@register_snippet
class Menu(ClusterableModel):
    menu_name = models.CharField(max_length=255, null=False, blank=False)

    @property
    def items(self):
        return self.menu_items.all()

    def __unicode__(self):
        return self.menu_name

    class Meta:
        verbose_name = "Navigation menu"

Menu.panels = [
    FieldPanel('menu_name', classname='full title'),
    InlinePanel('menu_items', label="Menu Items", help_text='Set the menu items for the current menu.')
]


class MenuItem(Orderable):
    link_external = models.URLField(
        "External link",
        blank=True,
        null=True,
        help_text='Set an external link if you want the link to point somewhere outside the CMS.'
    )
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        related_name='+',
        help_text='Choose an existing page if you want the link to point somewhere inside the CMS.'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        related_name='+',
        help_text='Choose an existing document if you want the link to open a document.'
    )

    text = models.TextField(
        'Menu option text',
        blank=False,
        null=False,
        default="menu option",
        help_text='Set the text that will be shown in your menu'
    )

    menu = ParentalKey(to='Menu', related_name='menu_items', null=True)

    @property
    def url(self):
        return self.link

    def __unicode__(self):
        if self.link_external:
            title = self.link_external
        elif self.link_page:
            title = self.link_page.title
        elif self.link_document:
            title = self.link_document.title
        return title

    class Meta:
        verbose_name = "Menu item"
