from ij import IJ
from ij.io import OpenDialog,DirectoryChooser
od = OpenDialog("Choose a file", None)
filename = od.getFileName()
folder = od.getDirectory()
filepath = folder+filename
imp = IJ.run("Movie (FFMPEG)...", "choose= filepath use_virtual_stack first_frame=0 last_frame=-1")
IJ.run("Set Measurements...", "integrated redirect=None decimal=3")
IJ.run(imp, "Measure Stack...", "")
