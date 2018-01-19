import imgaug
from imgaug import augmenters as iaa

seq_affine = iaa.Sequential([
    iaa.Affine(translate_px=(-2, 2),
               rotate=(-12, 12),
               scale=(0.95, 1.05),
               shear=(-4, 4),
               mode='edge')
])

seq_color = iaa.Sequential([
    iaa.GaussianBlur(sigma=(0.6, 1.2)),
    iaa.Multiply((0.4, 1.2)),
    iaa.Multiply((0.9, 1.1), per_channel=0.2),
])

seq_brighten = iaa.Sequential([
    iaa.Multiply((1.4, 1.4))
])

seq = iaa.Sequential([
    seq_affine,
    seq_color
])