---
theme: default
paginate: true
header: 'August 25th 2022 - Simber workshop'
footer: 'Henrik Finsberg -  Introduction to the cardiac MPS database and analysis package'
marp: true
---
<!-- Global style -->
<style>
section {
  background: #E3E3E3;
}
h1 {
    color: #FF8000;
}
h2 {
    color: #FF8000;
}
</style>

# Introduction to the cardiac MPS database and analysis package

Henrik Finsberg 
Senior Research Engineer
Department of Computational Physiology (Simula)

![width:200px](figures/logo.png)

---

## Plan for this session

- Using the MPS database
    - what is it
    - how to set it up on your laptop
    - how to add data to the database
    - analysis functionality
    - results export
- Unraveling the analysis scripts
    - how to make simple scripts that do the same as the MPS database application

---


## Prerequisites

Software and data
- python version 3.6 or newer
- mps database binary : FIXME: 
- example dataset: FIXME

Skills
- Basic understanding of python programming


---

## Disclaimer

This application is developed by me and used by very few people (Sam / Verena / ?)
If you have suggestions for improving the user experience please let me know :)

---

## What is the MPS database?

* A graphical user interface for analyzing and organizing MPS data
* It was built to run on a server
* It connects to to a database
* It has a web frontend
* It also has a REST API
* It has been packaged into a single binary that can run on your laptop

![bg right](figures/architecture.png)

---

## How to start it?

* Double click on the binary executable
* This files comes with python bundled inside it
* It will take some time to start up
* It will open a small web browser window (Google chrome)
* If this window is not responding you can just open any web browser and go to the url <localhost:8004>

---

## Creating a user and logging in

* You need to create a user in order to use the database
* This is because it was intentionally made for several users
* The application has a authentication layer
* When running this on your laptop the user information will be stored in a local database in your home directory

![bg right:45% contain](figures/database_login_signup.png)

---

## Home page

- Once you have logged in you will be sent to a very simple home page
- There are two important links here: `Search` and `Upload`

![bg right:60% contain](figures/database_home.png)

---

## Adding some data to the database

I have some data that I want to add to the database for analysis.
Here I am looking the the folder tree inside the folder located at `/Users/finsberg/Dropbox/Simber/data`

![bg right:60% contain](figures/folder-tree.png)

---

## Adding root paths

* A root path is a path on your computer containing folders with experiments
* In my case this is `/Users/finsberg/Dropbox/Simber/data`
* You can have multiple root paths
* The app will search for potential experiments in all root paths

![bg right:60% contain](figures/database_upload_root_path1.png)

---

## Trying to add an invalid path

If you try to add a root path that doesn't exist, you will get an error

![bg right:60% contain](figures/database_upload_root_path_invalid.png)

---

## Adding the correct path should give a success message

![w:700 center](figures/database_upload_root_path_success.png)

---

## Now you should be able to add a new experiment

- You might need to refresh the page
- Clicking on "Directory path" under "Add experiment" should list all potential experiments

![bg right:60% contain](figures/database_upload_add_experiement_list_experiements.png)

---

## We need to provide a config file

- To add an experiment we need to tell the application what is the structure of this experiment
- This is why we add the `.yaml` in the root of the experiment folder

![bg right:60% contain](figures/folder-tree.png)

---

## The config file

We need to specify the patterns in the file structure
![h:150 center](figures/config_file.png)
![bg right:40% contain](figures/folder-tree.png)

---

## Special names

There are a few special names that will be mapped to columns in the database table.
Using these names are not required, but it will allow you to more easily find the data you need.
These names are

- dose
- media
- drug
- pacing_frequency
- run
- date
- channel
- cell_line

---

## Organizing your experiments

* Try to make a simple file structure with only one common pattern
* The program will loop through all files in the experiment folder and try to match the patterns
* If you need more that one pattern, the program with start with the first pattern (on the top) and continue until it finds a pattern that match. Note that one file might match several patterns. For example all files in the example folder will match the following pattern `{run}.tif`.
* If one file doesn't match any pattern you will get an error

---

## Excluding folders 

It is also possible to exclude folder from being added to the database.
Say that you have a folder called `failedChips` and `failedChips2`. Then you could write your config file as follows

```
patterns:
- '{dose}_{run}/{date}-{dye}-{drug}_Stream_B01_s1_{channel}-Strea.tif'
excludes:
- 'failedChips'
- 'failedChips2'
```

---

## Adding custom rules

Sometimes the file name doesn't contain the name you want to add to the database. Then you can add custom rules. Here is one real example

```
folder: "190804_Verap_Flec_SCVI20_std"
regexs:
  - "{date}_{dose}_{d1}_{pacing_frequency}/Point{chip}_{media}_{drug_}_Channel{channel}_VC_Seq{seq_nr}.nd2"
  - "{date}_{dose}_{d1}_Dose5_Verap_{pacing_frequency}/Point{chip}_{media}_{drug_}_Channel{channel}_VC_Seq{seq_nr}.nd2"
  - "{date}_{dose}_{pacing_frequency}/Point{chip}_{media}_{drug_}_Channel{channel}_VC_Seq{seq_nr}.nd2"
rules:
  - 'drug_dict = {"Ver": "Verapamil", "Fle": "Flecainide"}; drug = drug_dict[drug_]'

```

---

## Lets try to add the experiment

We will get an error message saying that there is no drug called omecamtive in the database

![bg right:60% contain](figures/database_upload_add_experiment_drug_does_not_exist.png)

---

## Adding a new drug to the database

* We will add a new drug called `Omecamtiv`
* You should also add a list of synonyms of the drug. This will be names appearing in the filenames
* You can also add info about the drug



![bg right:60% contain](figures/database_upload_add_omecamtiv.png)

---

## Now you should be able to add the experiment

![h:350 center](figures/database_upload_add_experiment_success.png)

---


## Relationships in the database

![center contain](figures/database_ER_diagram.png)

---

## If we go back to the `Search` panel we can search through several items

![h:350 center](figures/database_search_through.png)

---

## We can search through drugs

* We can also go back to the `Upload` panel and add info about the drug

![bg right:60% contain](figures/database_search_drug.png)

---


## We can search through experiments

![bg right:60% contain](figures/database_search_experiment1.png)

---


## We can search through the individual video files

* There are several options to filter the search
* I think it is easier to search for the experiment and then filter the results


![bg right:60% contain](figures/database_search_mps_data.png)

---

## Filtering the results


![h:250 center](figures/database_search_filter_results_trace_type.png)
![bg right:45% contain](figures/database_search_filter_results_dose.png)

---

## Selecting a single file will bring up a new section below the table


![bg right:65% contain](figures/database_select_one_file.png)

---


## Fluorescence analysis section

Here you can specify different options for analyzing the fluorescence 

![bg right:65% contain](figures/database_analysis_section.png)

---

## Motion analysis section

Here you can specify different options for analyzing the motion 

![bg right:65% contain](figures/database_analyze_motion.png)

---

## When plotting, you first select the trace and the what kind of plot you want

![h:300 center](figures/database_plot1.png)
![bg right:45% contain](figures/database_plot2.png)
