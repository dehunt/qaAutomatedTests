Test automation suite for DL QA.

This will fetch, install, test, and verify included products (currently PDF Alchemist, PDF Optimizer, and PDF Checker).

Windows installation includes working through the Windows installer GUI as though a user.

Requirements:
	pytest
	pytest-html

	Optimizer: diff-pdf-visually
			   PyPDF2
			   pdftocairo/Poppler 
			   		Windows: https://blog.alivate.com.au/tag/pdftocairo/ for windows binaries, add to PATH
			   		Linux: poppler-utils (via package manager)
			   ImageMagick
			   		Windows: https://imagemagick.org/index.php, Add to PATH
			   		Linux: ImageMagick (via package manager)

	Alchemist: zipfile

	Windows:   pywinauto     NOTE: Python 3.8.1 breaks pywinauto. Use 3.7 until pywinauto gets updated

	Linux:     keyboard