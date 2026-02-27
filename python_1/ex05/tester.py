from load_image import ft_load
from pimp_image import (ft_invert, ft_red, ft_green, ft_blue, ft_grey,
                        display_images)


def main():
    array = ft_load("landscape.jpg")
    inverted = ft_invert(array)
    red_filtered = ft_red(array)
    green_filtered = ft_green(array)
    blue_filtered = ft_blue(array)
    grey_filtered = ft_grey(array)
    print(ft_invert.__doc__)

    # Affichage des images
    display_images(array, inverted, red_filtered,
                   green_filtered, blue_filtered, grey_filtered)


if __name__ == "__main__":

    main()
