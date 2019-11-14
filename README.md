# The FLOSSary

The FLOSSary is a free glossary of terms and definitions related to
free/libre and open source software (FLOSS). It serves as a point of
reference for the participants in the “Open Source and Intellectual
Property in the Digital Society” the the Technical University of
Berlin, and may be reused in other contexts like papers or
presentations.  The FLOSSary is collectively edited by the
participants and tutors of the course and distributed freely under the
conditions of the CC BY 4.0 license.

## Creating the FLOSSary PDF file

The FLOSSary is edited using LaTeX. It builds with `latexmk`:

    > cd Glossaries/TheFLOSSary
    > latexmk -pdf

When building the FLOSSary for the first time, it is necessary to create
the *contributers.tex* file first. The file can be created using the
*builder.sh* script located in the `scripts/` subdirectory (note that
the file has to be executed from the root directory):

    > ./scripts/builder.sh
	...

If everything works as expected, a file named *TheFLOSSary.pdf* should
exist now. The builder script also watches the input files and
continuously updates the final PDF.

## Prerequisites

### Required LaTeX installation

Building the FLOSSary PDF requires a number of LaTeX packages. This
example lists the dependencies for Ubuntu systems:

    > apt-get install -y python3 python3-pip \
		texlive-full make python-pygments \
		golang curl texlive-latex-extra latexmk texlive-bibtex-extra \
		fonts-lmodern cm-super texlive-fonts-recommended texlive-fonts-extra \
		xindy xpdf curl inotify-tools perl pandoc biber git


### Minimum LaTeX installation (experimental)

If you don't want to install the whole *texlive* environment (which
is about 4.5 GB in size), you may install *texlive-basic* and only
install the needed pacakges using *texliveonfly*:

	> apt-get install -y python3 python3-pip \
		texlive-base make python-pygments \
		golang curl texlive-latex-recommended latexmk texlive-bibtex-extra \
		fonts-lmodern cm-super texlive-fonts-recommended \
		xindy xpdf curl inotify-tools perl pandoc biber git
	> tlmgr init-usertree && tlmgr update --self && tlmgr update --all && \
		tlmgr install texliveonfly

*Note:* The builder-script will automatically run *texliveonfly*
before running *latexmk*, if the *texliveonfly* command is availabe.
So the build-process remains the same as described above.

### Python Packages

Python3 is required in order to successfully build the *contributers.tex*.
The relevant python packages can be installed from the python package
index using pip:

	>  pip3 install -r requirements.pip

## Using the FLOSSary in LaTeX documents

To use the FLOSSary, the data files need to be included in the place
where glossary data is usually placed. The FLOSSary entries sometimes
reference bibliography entries that are define in the
[Bibliography](Data/Bibliography.bib). The [FLOSSary main
document](Glossaries/TheFLOSSary/TheFLOSSary.tex) is a good starting
point for how to include the definitions and the required packages.

The FLOSSary entries use the prefix ```fsry```. For example, the
reference the definition of "free and open source software" should
look like this: ```\gls{fsry:FOSS}```. Similarly, the bibliography
entries use the same prefix like this: ```\cite{fsry:benkler-2002}```.

Please keep in mind that because of the collaborative editing process,
the individual entries in the FLOSSary vary in quality and in what
sort and quality of references or evidence is provided. Always check
the definitions pulled into your own documents. It is always possible
to submit a merge request to improve definitions where necessary.

To avoid changes in your own papers because of updated or added
definitions in the FLOSSary, it may be useful to specify the concrete
version of the FLOSSary used in the project. The authors aim at
tagging a new version at the end of every semester, as for example in
```18.10``` or ```19.04``` (the naming scheme is borrowed from
the
[Ubuntu release schedule](https://en.wikipedia.org/wiki/Ubuntu_version_history). The
FLOSSary Git repository can be included in a project as a submodule
explicitly using one of these versions.

## Contributing

Everybody is invited to contribute to the FLOSSary by following the
fork and merge requests contribution model. Contributions should be
worded according to scientific standards and reference the relevant
sources.

## Organisation

The glossary data is stored in the file
*Data/Glossary-FOSS.tex*. Referenced sources should be added in the
file *Data/Bibliography.bib*. These two files are meant to be reusable
in 3rd party papers, and should only contain the glossary terms and
definitions, and the cited sources.

The PDF document is generated from the LaTeX file
*Glossaries/TheFLOSSary/TheFLOSSary.tex*. Regular contributions of
terms and definitions should be added to the files under *Data/*. No
changes to the main document should be required for that. To update
the layout of the PDF file, edit the main document.

Have fun contributing!
