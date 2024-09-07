
# README SEN9110 Simulation Masterclass Group 14

Announcements

This README file was generated on: 22-03-2024

### Authors:
Created by: SEN9110 Simulation Masterclass Group 14

|        Name         | Student Number |
|:-------------------:|:---------------|
|    Claudio Prosperini     | 6084931        |
|    Juliëtte van Alst    | 5402409        |
|  Gerben Bultema  | 5309247        |
|   Roelof Kooijman   | 5389437        |


## Institution:

Delft University of Technology : Faculty Technology, Policy and Management.

### Purpose:

The data and the model are created for a project in the cSEN9110 Simulation Masterclass course of the TU Delft. Code is created to fulfill the paper assignment and the simulation assignments.

### General information:

#### MUST STILL BE DONE

### Technologies used

The code is written and tested for Python XXXXXXXX. The specific packages used are given in the requirement.txt file. To use the code an environment for Python should be created and the packages stated in the requirements.txt should be installed. The data used is stored in XXXXXXX formats, so a viewer that can read this format is required if only interested in data.

### Purpose code files

Various Python files are included. Each has its purpose which will be briefly explained in the table underneath.

| File             | Purpose                                                                                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| model.py         | Contains the model class which can use the components.py file in combination with the data produced by the different data files,  links.py and intersections.py to simulate the roads. |
| components.py    | Contains the used classes for the model, except the model class itself.                                                                                                                |
| links.py         | Creates the links based on the cleaned bridge dataset which is produced by the data.py file.                                                                                           |
| intersections.py | Creates the intersections between roads, using road data.                                                                                                                              |
| data_alignment.py | Aligns the bridge data with the intersection data created in the intersections.py file.                                                                                                |
| data_bridges.py  | Contains the data cleaning process with regard to the bridge data.                                                                                                                     |
| model_run.py     | Runs the model.py file once and stores the data produced by running the model.                                                                                                         |
| model_batch.py   | Will run the model.py file multiple times but with different model configurations. Used to get the data per scenario.                                                                  |
| model_viz.py     | Runs the model.py and creates a visualisation of the model dynamics in a separate window.                                                                                              |
| visualisation.py | Creates visualisations of the experimental output.                                                                                                                                     |

### File structuring
The folder has a specific structure that is as follows:

    EPA133a-G07-A3/
        ├── .idea/
        ├── DBFiles/
        ├── Data/
        ├── ImagePlots/
        └── model/

### Usage

If the file structuring is similar to the one given above the XXXXX files are enough to access all the functionalities of the project code. The "Purpose code files" define what the files do.
#### ADD MORE


### Assistance during code creation

Instructor:
-   Prof.dr.ir. A. Verbraeck - [A.Verbraeck@tudelft.nl](mailto:A.Verbraeck@tudelft.nl)

Teaching assistant:


### Contact

All questions about the code, project, or anything else can be sent to the following email:

[R.Kooijman-1@student.tudelft.nl](mailto:R.Kooijman-1@student.tudelft.nl)
