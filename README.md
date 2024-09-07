
# README Advanced Simulation

This README file was generated on: 22-03-2024

### Authors:
Created by: EPA133a Group 07

|        Name         | Student Number |
|:-------------------:|:---------------|
|    Claudio Prosperini     | 6084931        |
|    Juliëtte van Alst    | 5402409        |
|  Gerben Bultema  | 5309247        |
|   Roelof Kooijman   | 5389437        |


## Institution:

Delft University of Technology : Faculty Technology, Policy and Management.

### Purpose:

The data and the model are created for a project in the course EPA133a - Advanced Simulation of the TU Delft. 
The project aims to examine the vulnerability and criticality of Bangladesh's bridge infrastructure to better prepare the country for natural disasters. 

### General information:

The model takes data from the N1 and N2 road in Bangladesh, together with its intersecting side N-roads that are longer than 25 km. 
The beginning and endpoints of these roads function as SourceSinks. This means that they can both send and receive vehicles. 
In each timestep, vehicles (trucks) are created at the SourceSinks. Consequently, the vehicles are assigned a path through the road and bridge network. 
The paths can be assigned through three different ways, namely a straight routing type, a random routing type and a shortest path routing type.  The preferred routing type that is used within a model run can be set as a model parameter.
The bridges within the network can have different conditions, in accordance to the Bridge Condition Survey (BCS) of the Bangladesh government. The table below shows an overview of these bridge conditions. 

| Bridge condition | Explanation                  |
|:----------------:|:-----------------------------|
|        A         | No damage                    |
|        B         | Minor damage                 |
|        C         | Major elemental damage       |
|        D         | Major structural damage      |

Each bridge condition can be assigned a collapse chance. If a bridge is collapsed, vehicles that drive over the bridge will experience a delay time due to repairs. This delay time follows certain distributions based on the length of a bridge. 
The collapse chances for bridge conditions can be set as model parameters. 

Key KPI's that are used include: 
- Average driving time [min]: the average time it takes for a vehicle to travel to its destination.
- Average delay time [min]: the average time that vehicles are delayed. 
- Average speed [km]: the average speed for a vehicle to travel to its destination. 
- Bride breakdowns [dmnl] : the amount of bridges of each condition that break down during a simulation. 

### Technologies used

The code is written and tested for Python 3.11.8. The specific packages used are given in the requirement.txt file. To use the code an environment for Python should be created and the packages stated in the requirements.txt should be installed. The data used is stored in .xlsx and .csv formats, so a viewer that can read this format is required if only interested in data.

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
        ├── data/
        ├── experiment/
        ├── img/
        ├── model/
        ├── notebook/
        └── report/

The data folder contains the data files needed and produced by the .py files and should look like:

    data/
     ├── gis/
     ├── bridges.xlsx
     ├── bridges_cleaned.csv
     ├── bridges_intersected.csv
     ├── bridges_intersected_linked.csv
     ├── intersections.csv
     ├── intersections_bonus.csv
     ├── intersections_main.csv
     ├── roads.csv
     └── scenarios.csv

The experiment folder contains the scenario results in CSV-format and should look like:

    experiment/
     ├── scenario0.csv
     ├── scenario1.csv
     ├── scenario2.csv
     ├── scenario3.csv
     ├── scenario4.csv
     

The image folder contains all the images generated by the visualisation.ipynb file. These images show and compare the scenario results and should look like: 

    img/
     ├── barplot_avg_delay_time.png
     ├── barplot_avg_driving_time.png
     ├── bonus_bar.png
     ├── bonus_plot.png
     ├── intersect_img.png
     ├── lineplot_avg_speed.png
     └── road_network.png

The model folder contains all the code files required to run the model and should look like this:

    model/
        ├── ContinuousSpace/
        │   └── simple_continuous_canvas.js
        │   └── SimpleContinuousModule.py
        ├── bonus_assignment.py
        ├── components.py
        ├── data_alignment.py
        ├── data_bridges.py
        ├── intersections.py
        ├── links.py
        ├── model.py
        ├── model_batch.py
        ├── model_run.py
        └── model_viz.py

The notebook folder includes the jupyter notebook which visualises the experimental outcomes. 

    notebook/
        ├── data_cleaning.ipynb
        ├── network.ipynb
        └── visualisation.ipynb


Lastly, the report folder contains the report that provides detailed information on the analysis conducted for the Bangladesh case. 

    report/
     └── report.pdf

### Usage

If the file structuring is similar to the one given above the model_batch.py, model_run.py and model_viz.py files are enough to access all the functionalities of the project code. The "Purpose code files" define what the files do. If one wants to clean the raw Bangladesh bridge data the data_bridges.py file can be used. Afterwards, intersections can be retrieved using the intersections.py file. The data_alignment.py file aligns the cleaned bridges with intersections. The links.py can be used to create the bridges_intersected_linked.csv dataset. Lastly, the bonus_assignment.py includes the bonus assignment for this project.


### Assistance during code creation

Instructor:

-   Y. Huang - [Y.Huang@tudelft.nl](mailto:Y.Huang@tudelft.nl)
-   Prof.dr.ir. A. Verbraeck - [A.Verbraeck@tudelft.nl](mailto:A.Verbraeck@tudelft.nl)

Teaching assistant:

-   Angela Camarena Barba - [A.CamarenaBarba@student.tudelft.nl](mailto:A.CamarenaBarba@student.tudelft.nl)

### Contact

All questions about the code, project, or anything else can be sent to the following email:

[n.a.augustinus@tudelft.nl](mailto:n.a.augustinus@tudelft.nl)
