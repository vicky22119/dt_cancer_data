## utils file
import pickle
import json
import pandas as pd
import numpy as np
#import config
import os


class Cancer():
    def __init__(self,mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity,
                 mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error, 
                 perimeter_error,area_error,smoothness_error,compactness_error,concavity_error, 
                 concave_points_error,symmetry_error,fractal_dimension_error,worst_radius, 
                 worst_texture,worst_perimeter,worst_area,worst_smoothness,worst_compactness, 
                 worst_concavity,worst_concave_points,worst_symmetry,worst_fractal_dimension):
        self.mean_radius = mean_radius
        self.mean_texture = mean_texture
        self.mean_perimeter = mean_perimeter
        self.mean_area = mean_area
        self.mean_smoothness = mean_smoothness
        self.mean_compactness = mean_compactness
        self.mean_concavity = mean_concavity
        self.mean_concave_points = mean_concave_points
        self.mean_symmetry = mean_symmetry
        self.mean_fractal_dimension = mean_fractal_dimension
        self.radius_error = radius_error
        self.texture_error = texture_error
        self.perimeter_error = perimeter_error
        self.area_error = area_error
        self.smoothness_error = smoothness_error
        self.compactness_error = compactness_error
        self.concavity_error = concavity_error
        self.concave_points_error = concave_points_error
        self.symmetry_error = symmetry_error
        self.fractal_dimension_error = fractal_dimension_error
        self.worst_radius = worst_radius
        self.worst_texture = worst_texture
        self.worst_perimeter = worst_perimeter
        self.worst_area = worst_area
        self.worst_smoothness = worst_smoothness
        self.worst_compactness = worst_compactness
        self.worst_concavity = worst_concavity
        self.worst_concave_points = worst_concave_points
        self.worst_symmetry = worst_symmetry
        self.worst_fractal_dimension = worst_fractal_dimension
        
    def load_model(self):
        
            
        with open(os.path.join("models","prundecisiontree.pkl"), "rb") as f:
            self.model = pickle.load(f)    
            
        with open(os.path.join("models","columns.json") ,"r") as f:
            self.json_data = json.load(f)
    

    def cancer_get_prediction(self):

        self.load_model()  # Calling load_model method to get model and json_data
        array = np.zeros(len(self.json_data['columns']))

        array[0]=self.mean_radius
        array[1]=self.mean_texture
        array[2]=self.mean_perimeter
        array[3]=self.mean_area
        array[4]=self.mean_smoothness
        array[5]=self.mean_compactness
        array[6]=self.mean_concavity
        array[7]=self.mean_concave_points
        array[8]=self.mean_symmetry
        array[9]=self.mean_fractal_dimension
        array[10]=self.radius_error
        array[11]=self.texture_error
        array[12]=self.perimeter_error
        array[13]=self.area_error
        array[14]=self.smoothness_error
        array[15]=self.compactness_error
        array[16]=self.concavity_error
        array[17]=self.concave_points_error
        array[18]=self.symmetry_error
        array[19]=self.fractal_dimension_error
        array[20]=self.worst_radius
        array[21]=self.worst_texture
        array[22]=self.worst_perimeter
        array[23]=self.worst_area
        array[24]=self.worst_smoothness
        array[25]=self.worst_compactness
        array[26]=self.worst_concavity
        array[27]=self.worst_concave_points
        array[28]=self.worst_symmetry
        array[29]=self.worst_fractal_dimension


        print("Test Array -->\n",array)
        prediction = self.model.predict([array])[0]
        if prediction==1:
            return "You Have The Breast Cancer TC"
        else:
            return "You Are Not Having Breast Cancer"
        


if __name__ == "__main__":
    mean_radius = 7.760000
    mean_texture = 24.540000
    mean_perimeter = 47.920000
    mean_area = 181.000000
    mean_smoothness = 0.052630
    mean_compactness = 0.043620
    mean_concavity = 0.000000
    mean_concave_points = 0.000000
    mean_symmetry = 0.158700
    mean_fractal_dimension = 0.058840
    radius_error = 0.385700
    texture_error = 1.428000
    perimeter_error = 2.548000
    area_error = 19.150000
    smoothness_error = 0.007189
    compactness_error = 0.004660
    concavity_error = 0.000000
    concave_points_error = 0.000000
    symmetry_error = 0.026760
    fractal_dimension_error = 0.002783
    worst_radius = 9.456000
    worst_texture = 30.370000
    worst_perimeter = 59.160000
    worst_area = 268.600000
    worst_smoothness = 0.089960
    worst_compactness = 0.064440
    worst_concavity = 0.000000
    worst_concave_points = 0.000000
    worst_symmetry = 0.287100
    worst_fractal_dimension = 0.070390

    cancer_obj= Cancer(mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity,
                 mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error, 
                 perimeter_error,area_error,smoothness_error,compactness_error,concavity_error, 
                 concave_points_error,symmetry_error,fractal_dimension_error,worst_radius, 
                 worst_texture,worst_perimeter,worst_area,worst_smoothness,worst_compactness, 
                 worst_concavity,worst_concave_points,worst_symmetry,worst_fractal_dimension)
    detection = cancer_obj.cancer_get_prediction()
    print(f"{detection}")