# Cat_Dog_Image_Classifier
A simple image classifier using keras and tensorflow  

#Description  
used CNNs to make a deep learning model which classifies an image as a cat or a dog 
images used for training the model were taken from kaggle dataset - https://www.kaggle.com/competitions/dogs-vs-cats/data.     
Also used streamlit library to deploy the deep learning model in a website which allows the user to upload  
a JPG image of a cat or a dog and predicts the outcome.


#Dependencies  
streamlit==1.13.0  
tensorflow==2.11.0  
matplotlib==3.6.2  
numpy==1.24.1  
opencv_python==4.7.0.68  
keras==2.11.0
imghdr


#How To Run
1) install all the above dependencies using pip or another method.  
2) download the "train.zip" zip file from the link given above and extract all images.  
3) make two folders "cat" and "dog" inside the "train-data" folder in the repository and push all cat and dog images into their respective folders.
4) Now you are free to run the python notebook to go through the codes.  
5) To test the model in the website, use the following command  

```
streamlit run website.py
```
