import os
import time
import ultralytics
from dotenv import load_dotenv
from roboflow import Roboflow
from IPython import display
from ultralytics import YOLO
from IPython.display import display, Image

# start_time = time.time()

HOME = os.getcwd()
display.clear_output()
load_dotenv()
ultralytics.checks()

api_key = os.getenv("ROBOFLOW_API_KEY")
workspace_id = os.getenv("WORKSPACE_ID")
project_id = os.getenv("PROJECT_ID")

model = YOLO(f'{HOME}/yolov8n.pt')
# results = model.predict(source='https://media.roboflow.com/notebooks/examples/dog.jpeg', conf=0.25)

rf = Roboflow(api_key=api_key)
project = rf.workspace(workspace_id).project(project_id)
dataset = project.version(1).download("yolov8")

finish_time = time.time()

# print("Training time: ", start_time - finish_time, "s")