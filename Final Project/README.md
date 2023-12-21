1. You need to clone the yolov5 Repository.

git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -r requirements.txt  # install

2. Now You would need to add your dataset and properly configure it. It needs to be in specific format to be read by the yolov5 model.
                datasets
                |      |
            images     labels
        |    |   |       |    |    |
    test train validate  test train validate

3. You must make sure that you have one-to-one image to txt file for each of the xray images.
- There is python code that I commented out, It can be used to make it easier to properly format the files.

4. Ensure that you have:
    1. Proper Dataset with: test, train, validate (Images AND Labels)
    2. dataset.yaml file that describes where yolov5v can find all the information it needs to train the data. (Place this file in yolov5 directory so the model can find it)

5. You need to train the model:
    - For best results use epochs > 15
    - Make sure that there are no images with two hands in the xray as the txt file only describes the locations of the joints one hand.
    Command: python train.py --img 640 --batch 16 --epochs 20 --data dataset.yaml --weights yolov5s.pt

6. After you have trained the model (it may take over 7 hours), you can test it with the iamge the model has not seen before:
    Command: python detect.py --source "C:/Users/alexs/Desktop/Final Project/datasets/images/test/9002116.jpg"(or your own img) --weights best.pt --save-txt --conf-thres 0.35 --iou-thres 0.1

Resources used:
https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data
Youtube Tutorial:
https://www.youtube.com/watch?v=80Q3HIBy7Qg