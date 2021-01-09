ROI_pixels = []
arr_row = 0
for y in range(27, 40):
    ROI_pixels.append([])
    for x in range(567, 595):
        r,g,b,a = n[x,y]
        if a == 0:
            ROI_pixels[arr_row].append(0)
        else:
            ROI_pixels[arr_row].append(1)
    arr_row += 1

print(ROI_pixels)