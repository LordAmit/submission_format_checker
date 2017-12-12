# Submission Format Checker
Something to automate checking the format of submissions by students.

## I/O

- Input: A directory containing zip files
- Output: A HTML file containing Report of submission status.

## Workflow

- Submit a folder
- script will check the zipped file formats
- if matched, unzip the zipped file to a submission_extracted directory
- if not, mark it as wrong_submission
- traverse through each extracted\_directory in submission_extracted to
    - check number of files,
    - check naming convention of files, and
    - check contents of files.
    - if found problem in any state, mark it as wrong_submission
- prepare a html table as Report
    - with each zipped file as a submission_entry
    - each submission_entry will contain one of the following statuses: 
        - okay
        - wrong submission
        - no submission

## Todo

The following are needed to be done to complete this.

### Required / Specification  files

- [x] Create a configuration template file, which will: 
- [ ] specify the names of zipped submission
- [ ] specify number of files to be present in submission,
- [ ] specify the files to be present in submission, 
- [ ] naming format of directories
- [ ] contain template for submitted file


### Traversing

- [ ] Traverse through each directory from the specified submission directory
- [ ] Traverse through each file from each directory to find each file

### Checking
 
- [ ] Check naming format of submitted zip file
- [ ] Check Number of files in each traversed directory, 
- [ ] Check naming format of submitted files
- [ ] Check if submitted file follows the specified template file

### I/O - Processing

- [ ] Take a folder containing zipped files
- [ ] Unzip all zipped files to a different folder, if the zip file format matches