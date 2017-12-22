# Page extension imports:
from cms.extensions.toolbar import ExtensionToolbar
from cms.toolbar_pool import toolbar_pool

# Import our model from ``models.py``:
from .models import PageFieldExtension


@toolbar_pool.register
class PageFieldExtensionToolbar(ExtensionToolbar):

    # Loads the model from ``models.py``:
    model = PageFieldExtension

    def Populate(self):
        # Setup the extension toolbar with permissions and sanity checks:
        current_page_menu = self._setup_extension_toolbar()
        # If everything checks out:
        if current_page_menu:
            # Retrieves the instance of the current extension (if any) and
            # the toolbar item URL:
            page_extension, url = self.get_page_extension_admin()
            if url:
                # Adds a separator:
                current_page_menu.add_break()
                # Adds a toolbar item:
                current_page_menu.add_modal_item(
                    'Extra settings',
                    url=url,
                    disabled=not self.toolbar.edit_mode,
                )
