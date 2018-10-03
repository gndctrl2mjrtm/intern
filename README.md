# Python Intern
Scripts for Office Automation Tasks

## Compress files within folder to zip files

Select a folder and compress all of its contents according to flags sent to the script:

### Usage:

`python make_zip.py --d /test --m pdf`

The `--d` flag is for the target directory and the `--m` flag is for the file 'mode' (ex: pdf, pptx). When left blank, the mode is 'all', which compresses all of the contents. Another option is to pass `--m !pdf` which will compress all of the files that are not pdf as an example.

#### Mode Flags:

| Mode Flags    | Types            | 
| --------------|:----------------:| 
| <blank>	    | all files        | 
| pdf	        | pdf files only   | 
| /	            | directories only | 
| \!pdf.        | not pdf files   |  
| \!/           | not directories |  
