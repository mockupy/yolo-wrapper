## YOLO wrapper 
Open the comment lines in the **draw_detections_v3** function and run **Script.py**
> 392-396 lines in  [image.c](https://github.com/AlexeyAB/darknet/blob/master/src/image.c):
```mermaid
int b_x_center = (left + right) / 2;
int b_y_center = (top + bot) / 2;
int b_width = right - left;
int b_height = bot - top;
printf("BB - Bounding Box: id=%d, names=%s ,x_center=%d, y_center=%d, width=%d, height=%d\n", best_class_id,  names[best_class_id], b_x_center, b_y_center, b_width, b_height);
```