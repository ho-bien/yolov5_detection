# Write results
detects = {}
for *xyxy, conf, cls in reversed(det):
    xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
    c = int(cls)
                    
    if save_img or view_img:  # Add bbox to image
        label = None if hide_labels else (names[c] if hide_conf else f'{names[c]} {conf:.2f}')
        annotator.box_label(xyxy, label, color=colors(c, True))

    detects.setdefault(names[c], []).append(xywh)

sort_width = lambda val: val[2]
for d in detects.keys():
    detects[d].sort(reverse = True, key=sort_width)
situation(detects)

