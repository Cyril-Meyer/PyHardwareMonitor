from PIL import Image, ImageDraw

def create_icon(width=48, height=48, shape='circle', color='white', text=None):
    if not width == height:
        raise NotImplementedError
    
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    dc = ImageDraw.Draw(image)
    
    if shape == 'circle':
        dc.ellipse(
            (0, 0, width, height),
            fill=color)
    if shape == 'square':
        dc.rectangle(
            (1 * (width // 10), 1 * (height // 10), 9 * (width // 10), 9 * (height // 10)),
            fill=color)
    elif shape == 'thermometer':
        dc.ellipse(
            (1 * (width // 4), height // 2, 3 * (width // 4), height),
            fill=color)
        dc.rectangle(
            (3 * (width // 8), 0, 5 * (width // 8), 4 * (height // 5)),
            fill=color)
    else:
        raise NotImplementedError
    
    if text is not None:
        dc.text(
            (width // 2, height // 2),
            text,
            fill='black',
            anchor='mm',
            stroke_width=1*(width // 10),
            stroke_fill='white',
            font_size=9*(width // 10))

    return image
