import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', path='/Users/saugatsingh/Downloads/soccer_tracker-master/players_and_ball_detection/yolov5_players_and_ball.pt', force_reload=True)
print(model.names)
