from PIL import Image, ImageDraw, ImageFont

NUM_OF_PAPERS = 1
BOX_HEIGHT_ID, BOX_WIDTH_ID = 150, 150
BOX_HEIGHT, BOX_WIDTH = 175, 2170
IMAGE_WIDTH, IMAGE_HEIGHT = 2490, 3510
START_POINT = (150, 100)
DISTANCE = 225
DIST_TEXT_BOX = 90
NOTE = 'Chú ý: Viết đúng tất cả nội dung bao gồm các dấu câu, dấu chấm, dấu phẩy.\nNội dung viết từ sát lề bên trái, nằm trọn vẹn trong khung và trên cùng một dòng.'

TEXT = ['Xã Quỳnh Hồng, Quỳnh Phụ, Thái Bình',
        'Thị trấn Lịch Hội Thượng, Trần Đề, Sóc Trăng',
        'Xã Thượng Nhật, Nam Đông, Thừa Thiên Huế',
        'Thị trấn Gia Bình, Gia Bình, Bắc Ninh',
        'Xã Diễn Hồng, Diễn Châu, Nghệ An',
        'Phường 14, Phú Nhuận, Hồ Chí Minh',
        'Phường Trần Hưng Đạo, Thành phố Quảng Ngãi, Quảng Ngãi',
        'Xã Thanh Lương, Văn Chấn, Yên Bái',
        'Xã Liên Thủy, Lệ Thủy, Quảng Bình',
        'Phường Trần Phú, Thành phố Hải Dương, Hải Dương']


if __name__ == '__main__':
    for i in range(1, NUM_OF_PAPERS + 1):
        index = '%04d' % i

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

        image.show()
        pdf = image.convert('RGB')
        pdf.save('pdf_files/' + str(index) + '.pdf')
