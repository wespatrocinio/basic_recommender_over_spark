# Remarks about the challenge

- I modeled the data aiming to use some MLLib features for generating the cosine similarity for all columns. But this data modeling is not good for runnning _in box_ solution ... and I saw it too late to restrucutre the data and adequate the application. Shame on me! Thus, I focused on finish the functionality of the application _end-to-end_ and not concerned about performance;

- The main performance issue is on scanning the RDD to calculate the similarities with the another arrays. Spark RDD does not allow nested transformations (example: a foreach within a map), so I had to make the loop outside the RDD - which means take an action and collect it. Now I see that a better approach is to use an indexed RDD, without pivot over the prodcut ID, to use _ByKey_ aggregations (reduce, fold, etc.);

- I runned the application on a standalone Spark on my notebook. So I got really impacted by the performance issues caused by myself. I generated a reduced version of the dataset to test the funcionality without fall in `java heap overflow` issues. This dataset is available at `project_root/data` directory;