## Unsupervised Clustering

California Housing clustering

- Some Data cleaning is performed: outliers and null values removed
- A brief EDA is performed, geopandas is used to plot over a map and crs is used to project the data
- Some Data is generated, distance to coast is calculated with multiprocessing to ease the computing time
- A Pearson correlation is performed to review the linear relationship between variables.
- Scaling is performed, a brief comparison is performed to select a proper scaling method
- Kmeans models are trained and Inertia and silhouette scores are compared to select hyperparameters
- The selected Kmeans model is fitted into the data and some conclusions are drawn 
- In order to perform DBSCAN models, the distance between points is calculated and a preliminary exploratory analysis in performed to select DBSCAN hyperparameters
- DBSCAN is performed with the parameters selected, silhouette scores and noise level is computed to compare models
- The selected DBSCAN model is fitted into the data and some conclusions are drawn 

There is an explination in spanish about every plot and codecell, with some thoughts, conclussion and possible improvements.
