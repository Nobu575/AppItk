import numpy as np
import itk
import matplotlib.pyplot as plt

def distance_transform_3d(input_vol) :
    # Set dimension
    Dimension = 3

    # Setting for input image
    InputPixelType = itk.D
    InputImageType = itk.Image[InputPixelType, Dimension]

    input_vol = itk.image_from_array(input_vol)
    print(itk.template(input_vol))

    # Apply a filter: Distance transform
    distanceFilter = itk.SignedDanielssonDistanceMapImageFilter[InputImageType,InputImageType].New()
    distanceFilter.SetInput(input_vol)
    distanceFilter.InsideIsPositiveOn()
    distanceFilter.Update()

    output_vol = itk.array_from_image(distanceFilter.GetOutput())
    output_vol = np.where(output_vol<0,0,output_vol)

    return output_vol

def main() :
    print("This is a three-dimensional distance transform filter using ITK.")

if __name__ == "__main__":
    main()