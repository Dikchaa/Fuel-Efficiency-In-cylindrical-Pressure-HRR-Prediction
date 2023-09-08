# Fuel Efficiency In-Cylindrical Pressure & HRR Prediction

## Objective:

Our Objective is to Identify the Best Fuel Efficiency,In Cylindrical Pressure and Heat Release Rate Prediction. We intend to achieve this by using Formula method and Machine Learning algorithms and to Visualise it. 

In this project we have 20 + Fuels and its combination of Fuels.We are going to find which amount of fuel combination gives best Efficiency with Various Loads and Various Brake powers. Our parent Fuel is **CNSL(Cashew Nut Shell Oil)** combined with other Fuels like Diesel,Methanol etc.By using the Calculated Efficiency we are going to predict InCylindrical Pressure for 720 Angles and Predict HRR.

### Different Brake Powers:
* 5.2 Brake Power Equivalent Load 18.25 Kg
* 4.16 Brake Power Equivalent Load 14.6 Kg
* 3.12 Brake Power Equivalent Load 10.95 Kg
* 2.08 Brake Power Equivalent Load 7.30 Kg
* 1.04 Brake Power Equivalent Load 3.65 Kg

### Conversion Brake Power to Equivalent Load Formula:
●	Brake Power =(2*pi*n*t) / 60000   n=1500,r=0.185,t=w*r*9.81
  
### List of Fuels :
* Butanol 10
* Butanol 20
* Butanol 30
* Butanol 40
* Diesel 10
* Diesel 20
* Diesel 30
* Diesel 40
* Diesel
* CNSOME 
* CNSL (Cashew Nut Shell Oil)
* Methanol 10
* Methanol 20
* Methanol 30
* Methanol 40
* Ethanol 10
* Ethanol 20
* Ethanol 30
* Ethanol 40
* Orange Peel Oil 10
* Orange Peel Oil 20
* Orange Peel Oil 30
* Orange Peel Oil 40
* Cotton Seed Oil 10
* Cotton Seed Oil 20
* Cotton Seed Oil 30
* Cotton Seed Oil 40
* Camphour Oil 10
* Camphour Oil 20
* Camphour Oil 30
* Camphour Oil 40
* Coconut Seed Oil 10
* Coconut Seed Oil 20
* Coconut Seed Oil 30
* Coconut Seed Oil 40
* Di Ethyl Ether 10
* Di Ethyl Ether 20
* Di Ethyl Ether 30
* Di Ethyl Ether 40
* Di Methyl Carbonate 10
* Di Methyl Carbonate 20
* Di Methyl Carbonate 30
* Di Methyl Carbonate 40

## Methodology:

### Efficiency Calculation by using Formula Method:
#### Factors Influencing Efficiency :
* Calorific value
* Density
* Load
* Brake Power
* Mass of Fuel
* Heat Input.
  
 #### Formula:
 - Mass of fuel 1 = ((amount of fuel 1  * 0.000001) / 60) * density of fuel 1
 - Mass of fuel 2 =((amount of fuel 2  * 0.000001) / 60) * density of fuel 2
 - Heat input = mass of fuel 1 * calorific value of fuel 1 + mass of fuel 2 * calorific value of fuel 2
 - Efficiency = Brake Power / Heat input

### InCylindrical Pressure Prediction:
In Cylindrical Pressure Prediction for all 720 angles for the best Efficiency Fuel combinations for all 20+ fuels and for all loads.

#### Factors Influencing Pressure:
* Volume
* Mass of Fuel
* Cetane
* Angle (720)
* Density
* Visocity
* Calorific Value.

### Models Used:
We are using Different Machine Learning Models such as Multiple Linear Regression,Random Forest Regressor,Decision Tree Regressor,Gradient Boosting Regressor.Out of these models tested Random Forest Regressor and Decision Tree Regressor gives best result.

### Performance Matrix:
* #### Random Forest Regressor:
  - Mean Square Error: 0.234809795
  - Root Mean Square Error: 0.484571765
  - R Square: 0.998782242
* #### Decision Tree Regressor:
  - Mean Square Error: 0.33849539
  - Root Mean Square Error: 0.58180357
  - R Square: 0.998244513
* #### Gradient Boosting Regressor:
  - Mean Square Error: 0.840088763  
  - Root Mean Square Error: 0.916563562
  - R Square: 0.995643176
* #### Linear Regression:
  - Mean Square Error: 151.1745303
  - Root Mean Square Error: 12.29530522
  - R Square: 0.215986548

 ### Visualization:
 <img width="632" alt="image" src="https://github.com/santhanalakshmi21/Fuel-Efficiency-In-cylindrical-Pressure-HRR-Prediction/assets/104186416/09c31f16-36e7-4388-ab07-7b568be7d5b4">

### Heat Release Rate:
#### Formula:
HRR = (((1.35 / (1.35 - 1)) * (Pressure * ((Volume - dV) / 1))) + ((1 / (1.35 - 1)) * (Volume * ((Pressure - dP) / 1))))

## Challenges Faced:
As we are working on Real time data ,due to insufficient data our Machine Learning model got under fit after removing outliers.so we used Formula method to find Best Efficiency.

## Purpose:
Meet both the ends of the most practical energy conversion device.One side is diesel engines is needed in various sectors like industry and transport since its most reliable.Other side we have biofuels that are on par with diesel but they have some drawbacks if directly used.Through this project we can find which fuel combination at which load give best performance.Since Mechanical engineers don't know ML and Data Analytics difficult for them to work with huge datasets and precision.The  main aim is to predict engine performance without running the engines in the labs.Hence saves time,money spent on the engines.The energy of the technical workers would be saved and hence can be invested to better places.

## Innovation:
Project will predict behaviours/performance of diesel engine when filled with various combinations of biofuels Therefore it saves time and money spent on testing engine with biofuels.This will finally help in saving the harmful pollution elements released by the automobiles in the air

## Scope:
Since the results would be comparable with practically obtained results i.e experimental result.Hence we can rely on result and go for actual experiment with best performing point saving the time and money.These results can be used for validation since the precision rate would be higher.

## Contributors:
  - Santhana Lakshmi
  - Dikcha Singh
    
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  









