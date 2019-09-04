# Assignment 1 - Designing Models and Analyzing Data (Template)
(remove: **text between brackets to be removed**)

> * Participant name: Rhyse Bendell
> * Project Title: HW1

# General Introduction

The first part of this assignment explores designing models (and basic Python/Git features). 

We will look at **subway model in a city** system. A **subway system** is an underground, tube, or metro, underground railway system used to transport large numbers of passengers within urban and suburban areas - modern subways use different types of electronic data collection sensors to supply information which is used to manage assets and resources efficiently. 

The second part of the assignment explores data analysis. Data analysis and visualization is key to both the input and output of simulations. This assignment explores different random number generators, distributions, visualizations, and statistics. Additionally, it will look at getting you accustomed to specifying input and output variables to a system. We will also practice working with real data.

# Part 1: Designing a Model - Subway System

Mass transit is already a vital component for cities hosting large populations, and as populations continue to increase the importance of optimizing the capability of transit systems will only increase. Although the potential for remote work opportunities may somewhat mitigate the demand for mass transit options, the reality of climate change and the cost of personal transportation (vehicles, road maintanence, fuel transport, repair, etc.) will necessitate expansion of mass transit systems: the more we can understand about their design and use now may help to reduce negative reactions to the transition to reliance on mass transit such as subways and trains.

Some nations have already begun to feel the strain of populations that have grown beyond the capabilities of mass transit. Many videos captured in Japan and portions of China show passengers literally packed into underground transport cars by the force of several individuals, and while those snapshots may be amusing from the outside that discomfort is not a far off reality for cities such as New York or Washington D.C.

The problem of human transportation is, of course, not a new one, and with the rapid technological advancements witnessed in the last century we may be equipped to handle developing challenges. While engineers work to achieve game-changing tech such as bullet trains and their ilk, it is up to researchers on the human-factors and modeling side of the equation to explore how best to leverage any new and existing systems. Fortunately, we exist in an age of data abundance: models and simulations which previously may have been based on speculation, or a single researcher's afternoon at the stairs of the Tube may now be replaced by empirical data regarding passaenger loads, behaviors, preferences, and more which can inform models which may be used to improve both the structural and social engineering associated with our transit technologies.


![Image of Subway City System](images/subway_model.png)

## (Part 1.1): Requirements (Experimental Design) **(10%)**

(remove: You should start by specifying a set of requirements. I specified a topic a Subway escalator. What exactly does that mean - practice formulating your own set of requirements and an experiment. Define problems cities face and hypothesize how a subway system could help alleviate these issue. This helps you think about your problem communication and system objectives inputs, functions, and outputs - they should be clearly specified.)

IDS6145: Requirements Definition

What is the User’s Need? 
At the highest level, the need of individuals utilizing the subway system is to get from point A to point B. Although it may not be the highest priority of all users, it seems reasonable to assume that minimizing the time in transit is a shared goal of the majority. 

![Subway-HighLevelRequirements.PNG](\images\Subway-HighLevelRequirements.PNG)



What is the Simuland? 
What needs to be learned about it? 
What are the measures of effectiveness to be produced?

## (Part 1.2) Subway (My Problem) Model **(10%)**

(remove: add a high-level overview of your model, the part below should link to the model directory markdown files)
(remove: Look at the [**Object Diagram**](model/object_diagram.md) for how to structure this part of Part 2 for each diagram. Only the Object diagram has the template, the rest are blank. )

* [**Object Diagram**](model/object_diagram.md) - provides the high level overview of components
* [**Class Diagram**](model/class_diagram.md) - provides details of (what are you providing details of)
* [**Behavior Diagram**](model/behavior_diagram.md) - provides details of (what are you providing details of)
* [**Agent / User case** (if appropriate)](model/agent_usecase_diagram.md) - provides details of (what are you providing details of)

## (Part 1.3) Subway (My Problem) Simulation **(10%)**

(remove: Describe how you would simulate this - including type of simulation, rough details, inputs, outputs, and how it will help you analyze your experimental hypothesis, or nullify your null hypothesis.)


## (Part 1.4) Subway City (My Problem) Model **(10%)**
[**Code template**](code/README.md) - Starting coding framework for the (insert your exact problem here.)
You are expected to create the python files - the code should run without errors, create and object(s) for your system, but not provide function detail.



## (Part 1.5) Specifying the Inputs to a System **(10%)**

(remove the below points once ideas are satisfied)
* Specify the independent and dependent input variables of your subway esclator model
* Specify where the data will come from measured subset of real data (empirical) or synthetic data
* What kind of statistics are important to capture this input data
* How do you plan to analyze the output of your model?
* What ways will you visualize your data - charts, and graphs you will create?
* What clever way will you visualize your output with a useful infographic?



# Part 2: Creating a Model from Code

## (Part 2.1) **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model **(10%)**
Here [**we provide an overview**](code/POTS_system/README.md) of the **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model and provide a source code template for the code found in  [**the following folder**](code/POTS_system/). Please create a **class** diagram of this model (replace the placeholder diagram). (you can use paper and pencil or a digital tool).



# Part 3: Data Analysis

## (Part 3.1) - Real Data **(10%)**

Find a datasource that looks at part of this model - subway stations locations / escalator number, heights, widths / volume of passangers - ridership numbers   (*fits* - we are pretty loose here, it can be anything.)

* Write up a paragraph that describes the data and how it fits into your system.
* Load the data into Python
* Calculate a few useful statistic on the data - keep it simple- STD, means, etc..., this is just designed * to get used to working with real data. Explain the insights you derive from these statistics.
* Visualize the raw data - visualize a few critical aspects of the data to better describe what it is, what it is showing, and why its useful to your system.
* Calculate and plot some summary statistics that better describe the data.

(Add your plots and visualization here)
(Put your data into the data directory)


## (Part 3.2) -  Plotting 2D Random Number Generators **(15%)**

This portion of the assignment looks at generating random numbers in Python and understanding how to properly plot them. Plot two different random numbers, pseudo random and quasi random, for five different N values. There should be 10 subplots, all properly formatted 2D plots. Note, each of the N points will have two coordinates, an x and a y, therefore you will need to generate two random numbers for each point. You should replace the image with your results in a simalar format. Discuss how the patterns differ. Feel free to change the N values from the suggested N values in the image to state your case.

![Image of 2d template City](images/2Dtemplate.png)


## (Part 3.3) -  Plotting 1D Random Distributions **(15%)**

Now, choose three different distributions to plot in 1D, or as a histogram. Choose a pseudo-random generator and generate three different distributions. Example distributions are Uniform (part 8), Normal, Exponential, Poisson, and Chi-Squared, but feel free to use any three distributions of your choice. Again, plot each distribution for five different Ns. This will result in 15 different subplots, formatted similar to the image in Part 8. Include your properly formmated 1D plots below and breifly describe what we are looking at and how things change as N is changed.

Repeat the above using a quasi-random generator. Discuss the similarities and differences.
