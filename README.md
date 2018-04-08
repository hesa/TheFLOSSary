# The FLOSSary

The FLOSSary is a free glossary of terms and definitions related to free/libre and open source software (FLOSS). It serves as a point of reference for the participants in the “Open Source and Intellectual Property in the Digital Society” the the Technical University of Berlin, and may be reused in other contexts like papers or presentations.
The FLOSSary is collectively edited by the participants and tutors of the course and distributed freely under the conditions of the CC BY 4.0 license.

## Creating the FLOSSary PDF file

The FLOSSary is edited using LaTeX. It builds with `latexmk`:

    > cd Glossaries/TheFLOSSary
    > latexmk -pdf

If everything works as expected, a file named *TheFLOSSary.pdf* should exist now. 

## Contributing

Everybody is invited to contribute to the FLOSSary by following the fork and merge requests contribution model. Contributions should be worded according to scientific standards and reference the relevant sources.

## Organisation

The glossary data is stored in the file *Data/Glossary-FOSS.tex*. Referenced sources should be added in the file *Data/Bibliography.bib*. These two files are meant to be reusable in 3rd party papers, and should only contain the glossary terms and definitions, and the cited sources.

The PDF document is generated from the LaTeX file *Glossaries/TheFLOSSary/TheFLOSSary.tex*. Regular contributions of terms and definitions should be added to the files under *Data/*. No changes to the main document should be required for that. To update the layout of the PDF file, edit the main document.

Have fun contributing!
