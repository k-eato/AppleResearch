# Apple Detection and Classification
This project was developed to train a neural network to locate apples in images, as well as a second neural network to classify them between healthy and rotten apples. In order to do this, TensorFlow and its Object Detection API need to be installed and used. The following sections will walk through the various aspects of the project leading to the working solution. The goal is to demonstrate the work accomplished and also explain how to do it for those curious of working with the TensorFlow tools on a similar project.

### Datasets
Over the course of the project's work, three different datasets were gathered for each portion of the project, leading to six in total. 

##### Object Detection
For the object detection prtion, the first one captured consists of pictures of actual apples from an organic farm. These apples had lots of defects from brown spots to mold, helping to gather images of rotten apples since these would be the harder to find than images of healthy apples. Most of the pictures are various angles of a single apple against a blank piece of paper. However, a couple images at the end include multiple apples with other objects to provide a greater challenge to the neural network. Some samples from the data are shown below, while the rest can be found following the directory structure "Object Detection/Data/Actual Photos"<br/>
![Detection Dataset 1](https://github.com/k-eato/AppleResearch/blob/master/Object%20Detection/Data/Actual%20Photos/0.jpg)
![Detection Dataset 1](https://github.com/k-eato/AppleResearch/blob/master/Object%20Detection/Data/Actual%20Photos/101.jpg)<br/>

The issue with this approach is the difficulty in creating a large enough dataset, so the other two datasets were created with augmented images. A single Python script (dc.py) was used to create both by changing the inputs. It randomly places a number of apples on a backdrop meant to look like a conveyor belt due to the project goal of helping food processing plants. One dataset is meant for training while the other is for testing the model afterwords. The script also creates XML files for each new image, since they are needed later to tell where the apples are located in each. Pictures from each are shown below.<br/>
![Detection Dataset 2](https://github.com/k-eato/AppleResearch/blob/master/Object%20Detection/Data/Training/200.jpg)
![Detection Dataset 3](https://github.com/k-eato/AppleResearch/blob/master/Object%20Detection/Data/Testing/19.jpg)<br/>

##### Classification
The three datsets used with the classification model are split for the purposes of training, validation, and testing. The training dataset features images of healthy and rotten apples against the background of the belt from the training dataset of the Object Detection portion. Likewise, the testing dataset uses the blue belt background of the object detection test dataset. All of the images used for this come from data of rotten and fresh fruits found on [Kaggle](https://www.kaggle.com/sriramr/fruits-fresh-and-rotten-for-classification). For the validation dataset, the images are used as found in this dataset to hopefully provide better contrast to the train and test datasets in order to fight overfitting. To increase the size of the datasets, two Python scripts (rotate.py and brighten.py) are used to rotate and affect the brightness of all the images passed to them. This effectively creates 11 new images from the original. Sample results of this are shown below.<br/>
![Classification Data](https://github.com/k-eato/AppleResearch/blob/master/Classification/Data/augmentation_results.JPG)<br/>

