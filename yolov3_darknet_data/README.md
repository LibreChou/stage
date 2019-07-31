Training YOLOv3 Object Detector - HTML Drawings

`cd darknet`

1. Create the train-test split

`python3 splitTrainAndTest.py JPEGImages`

The 'labels' folder should be in the same directory as the 'JPEGImages' folder.

2. Compile darknet, the framework already installed from https://github.com/pjreddie/darknet

```
make clean
make
```
You can modify 'Makefile' to set GPU to 1 if you have a GPU.

3. Get the pretrained model

```
wget https://pjreddie.com/media/files/yolov3-tiny.weights
./darknet partial cfg/yolov3-tiny.cfg yolov3-tiny.weights yolov3-tiny.conv.15 15
```

4. Fill in correct paths in the 'darknet.data' file

5. Start the training as below, by giving the correct paths to all the files being used as arguments

```
mkdir weights
./darknet detector train darknet.data yolov3-tiny-data.cfg yolov3-tiny.conv.15 > train.log
python3 plotTrainLoss.py train.log
```

6. Evaluate your model

```
mkdir results
./darknet detector valid darknet.data yolov3-tiny-data.cfg weights/yolov3-tiny-data_final.weights
./darknet detector recall darknet.data yolov3-tiny-data.cfg weights/yolov3-tiny-data_final.weights
mkdir data_val
jupyter notebook fill_data_val.ipynb
./mean_average_precision.sh
```
mAP results are stored in 'mAP.txt'

7. Test your model 

```
./darknet detector train darknet.data yolov3-tiny-data.cfg weights/yolov3-tiny-data_final.weights imageToTest.jpg -out Yolo_files/predictions
```

8. Now use your model on your webcam

```
./darknet detector demo darknet.data yolov3-tiny-data.cfg weights/yolov3-tiny-data_final.weights
```
Predictions are stored in 'yolo_predictions'

9. While predicting frames from your webcam, run YOLOProject.ipynb to generate 'index.html' 

```
jupyter notebook YOLOProject.ipynb
npm install -g browser-sync
browser-sync start --server -w index.html
```

10. To augment the dataset artificially

`jupyter notebook augmentation.ipynb`

11. You can also augment it manually by moving new pictures to an 'Images/001' folder and then labelling them

```
sudo apt-get install python3-tk
sudo apt-get install python3-pil python3-pil.imagetk
mkdir Labels
python3 labelling.py
```