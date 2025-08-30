from ._anvil_designer import IFrameTemplate
from anvil import *

class IFrame(IFrameTemplate):
    def __init__(self, **properties):
        self.shown = False
        self._url = None

        # You must call self.init_components() before doing anything else in this function
        self.init_components(**properties)

    # Any code you write here will run when the form opens.

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, u):
        self._url = u
        if self.shown:
            self.form_show()

    def form_show(self, **event_args):
        """This method is called when the HTML panel is shown on the screen"""
        self.shown = True
        if self._url is not None and self._url != "":
            self.call_js('setURL', self._url)

