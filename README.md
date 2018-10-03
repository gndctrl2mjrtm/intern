![alt text](https://ei.marketwatch.com/Multimedia/2013/08/30/Photos/MG/MW-BH721_pf_10t_20130830201010_MG.jpg?uuid=c4aed170-11d1-11e3-b648-002128040cf6)


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
