from PIL import Image, ImageDraw, ImageFont

START_FILE = 1166
NUM_OF_PAPERS = 1668
BOX_HEIGHT_ID, BOX_WIDTH_ID = 150, 150
BOX_HEIGHT, BOX_WIDTH = 175, 2170
IMAGE_WIDTH, IMAGE_HEIGHT = 2490, 3510
START_POINT = (150, 100)
DISTANCE = 225
DIST_TEXT_BOX = 90
NOTE = 'Chú ý: Viết đúng tất cả nội dung bao gồm các dấu câu, dấu chấm, dấu phẩy.\nNội dung viết từ sát lề bên trái, nằm trọn vẹn trong khung và trên cùng một dòng.'


patterns = ['*.txt']
text_lines_dir = '/home/trucly/Documents/DATASET/hw_collect/text_files/'
pdf_files_dir = '/home/trucly/Documents/DATASET/hw_collect/pdf_files/'


def get_data(data_path):
    with open(data_path, "r") as f:
        data = f.read()
    return data.split('\n')


if __name__ == '__main__':
    for i in range(START_FILE, NUM_OF_PAPERS + 1):
        index = '%04d' % i

        TEXT = get_data(text_lines_dir + str(index) + '.txt')

        # Create new image with A4 size
        image = Image.new(mode='RGB', size=(IMAGE_WIDTH, IMAGE_HEIGHT), color='white')

        image_draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('ArialUnicodeMS.ttf', 50)

        # Draw ID box
        shape = [START_POINT, (START_POINT[0] + BOX_WIDTH_ID, START_POINT[1] + BOX_HEIGHT_ID)]
        image_draw.rectangle(xy=shape, fill='white', outline='black', width=4)
        image_draw.text(xy=(170, 140), text=index, fill=(0, 0, 0), font=font)

        # Note
        image_draw.text((350, 105), NOTE, fill=(0, 0, 0), font=font)

        # Draw box to write
        top_left_x, top_left_y = START_POINT
        for j in range(10):
            text = TEXT[j]

            top_left_y += DISTANCE

            # Text
            image_draw.text((top_left_x, top_left_y), text, fill=(0, 0, 0), font=font)

            top_left_y += DIST_TEXT_BOX

            # Box
            shape = [(top_left_x, top_left_y), (top_left_x + BOX_WIDTH, top_left_y + BOX_HEIGHT)]
            image_draw.rectangle(shape, fill='white', outline='black', width=4)

        pdf = image.convert('RGB')
        pdf.save(pdf_files_dir + str(index) + '.pdf')
