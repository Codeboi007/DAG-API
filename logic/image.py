from PIL import Image
import torchvision.transforms as transforms


def augment(file_path, method):
    img = Image.open(file_path).convert('RGB')

    if method == "rotate":
        transform = transforms.RandomRotation(45)
    elif method == "flip":
        transform = transforms.RandomHorizontalFlip(p=1.0)
    elif method == "brightness":
        transform = transforms.ColorJitter(brightness=0.5)
    else:
        transform = transforms.Compose([])

    img = transform(img)
    output_path = file_path.replace(".", "_augmented.")
    img.save(output_path)
    return output_path
