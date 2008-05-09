"""Catalog index node adapters that only clear the index when
needed."""

from Products.GenericSetup.PluginIndexes.exportimport import PluggableIndexNodeAdapter as PluggableIndexBase

class PluggableIndexNodeAdapter(PluggableIndexBase):
    """Only clear the index when needed."""

    def _importNode(self, node):
        """Import the object from the DOM node.
        """
        indexed_attrs = []
        for child in node.childNodes:
            if child.nodeName == 'indexed_attr':
                indexed_attrs.append(
                                  child.getAttribute('value').encode('utf-8'))
        if getattr(self.context, 'indexed_attrs', None) != indexed_attrs:
            self.context.indexed_attrs = indexed_attrs
            self.context.clear()

    node = property(PluggableIndexBase._exportNode, _importNode)
