import arcpy
import pythonaddins

class ComboBoxClass1(object):
    """Implementation for ComboBox_PointXY_addin.combobox (ComboBox)"""
    def __init__(self):
        self.items = ["CHOICE A", "CHOICE B", "CHOICE C", "CHOICE D"]
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'W1234567890123456789012345678901234567890'
        self.width = '1234567890'
    def onSelChange(self, selection):
        print "New Selection:",selection
    def onEditChange(self, text):
        print"Edit Change:",text
    def onFocus(self, focused):
        pass
    def onEnter(self):
        print "Current Value:",self.value
    def refresh(self):
        pass
