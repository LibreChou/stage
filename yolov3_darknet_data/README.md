Training YOLOv3 Object Detector - HTML Drawings

1. Install awscli

`sudo pip3 install awscli` 

2. Get the relevant OpenImages files needed to locate images of our interest

`wget https://storage.googleapis.com/openimages/2018_04/class-descriptions-boxable.csv`

`wget https://storage.googleapis.com/openimages/2018_04/train/train-annotations-bbox.csv`

3. Download the images from OpenImagesV4

`python3 getDataFromOpenImages_snowman.py`

4. Create the train-test split

`python3 splitTrainAndTest.py JPEGImages`

The 'labels' folder should be in the same directory as the JPEGImages folder.

5. Install Darknet and compile it.
```
cd ~
git clone https://github.com/pjreddie/darknet
cd darknet
make
```
6. Get the pretrained model
```
wget https://pjreddie.com/media/files/yolov3-tiny.weights
./darknet partial cfg/yolov3-tiny.cfg yolov3-tiny.weights yolov3-tiny.conv.15 15
```
7. Fill in correct paths in the darknet.data file

8. Start the training as below, by giving the correct paths to all the files being used as arguments

```
./darknet detector train darknet.data yolov3-tiny-data.cfg yolov3-tiny.conv.15 > train.log
python3 plotTrainLoss.py train.log
```

9. Give the correct path to the modelConfiguration and modelWeights files in object_detection_yolo.py and test any image or video for snowman detection, e.g.

`python3 object_detection_yolo.py --image=imageToDetect.jpg`
`python3 object_detection_yolo.py --video=videoToDetect.mp4`

