def crop(img, roi):
    img.croped_data = img.data[roi.x:roi.x+roi.width, roi.y:roi.y+roi.length]

def find_rescaling_parameters(a, b):
    m = (b["value"]-a["value"]) / (b["pixel"]-a["pixel"])
    x0 = a["value"] - m*a["pixel"]
    return m, x0

def linear(m, x0, x):
    return m*x + x0

def rescale(final_data, para_x, para_y, roi):
    x = [linear(para_x[0], para_x[1], _+roi.x) for _ in final_data[0]]
    y = [linear(para_y[0], para_y[1], _+roi.y) for _ in final_data[1]]
    return (x,y)

def rescale_final_data(final_data, coordinates, roi):
    para_x = find_rescaling_parameters(coordinates.x1, coordinates.x2)
    para_y = find_rescaling_parameters(coordinates.y1, coordinates.y2)
    return rescale(final_data, para_x, para_y)