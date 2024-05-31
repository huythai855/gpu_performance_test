#!/bin/bash

start_time=$(date +%s)

echo "Running pip install -r requirements.txt..."
pip install -r requirements.txt

echo "Running YOLO training..."
yolo task=detect mode=train model=yolov8s.pt data={dataset.location}/data.yaml epochs=50 imgsz=800 plots=True

end_time=$(date +%s)
elapsed_time=$(($end_time - $start_time))
echo "Time taken: $elapsed_time seconds"
