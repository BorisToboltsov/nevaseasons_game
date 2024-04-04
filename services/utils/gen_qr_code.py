import qrcode
from PIL import Image
from qrcode.main import QRCode


async def gen_qr_code(link_list: list) -> list:
    logo_path = './static/images/logo.jpg'
    logo = Image.open(logo_path)

    # taking base width
    basewidth = 100

    # adjust image size
    wpercent = (basewidth / float(logo.size[0]))
    hsize = int((float(logo.size[1]) * float(wpercent)))
    logo = logo.resize((basewidth, hsize))
    qr_code = QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    image_path_list = []
    for link in link_list:
        # adding URL or text to QRcode
        qr_code.add_data(link)

        # generating QR code
        qr_code.make()

        # taking color name from user
        color = 'Blue'

        # adding color to QR code
        qr_img = qr_code.make_image(
            fill_color=color, back_color="white").convert('RGB')

        # set size of QR code
        pos = ((qr_img.size[0] - logo.size[0]) // 2,
               (qr_img.size[1] - logo.size[1]) // 2)
        qr_img.paste(logo, pos)

        uuid = link.split('=')[1]
        # save the QR code generated
        qr_img.save(f'./static/qr_codes/{uuid}.png')
        image_path_list.append(f'./static/qr_codes/{uuid}.png')

    return image_path_list
