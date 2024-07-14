from pathlib import Path
import sys

sys.path.append( '../MachineLearning/' )
contourvalues = Path
Path = "./MachineLearning/contourvalues.py"

contourvalues = contourvalues.__getattribute__

