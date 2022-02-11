import numpy as np
import itk
import matplotlib.pyplot as plt

# Input file name
input_filename = './jenga.png'

# Set dimension
Dimension = 2

# Read input image
itk_image = itk.imread(input_filename)

# Setting for input image (RBG color)
ComponentType = itk.UC
InputPixelType = itk.RGBPixel[ComponentType]
InputImageType = itk.Image[InputPixelType, Dimension]

# Setting for output image (Grayscale)
OutputPixelType = itk.UC
OutputImageType = itk.Image[OutputPixelType, Dimension]

# Loading
reader = itk.ImageFileReader[InputImageType].New()
reader.SetFileName(input_filename)

# Apply a filter: Convert to grayscale
rgbFilter = itk.RGBToLuminanceImageFilter.New(reader)

# Saving
writer = itk.ImageFileWriter[OutputImageType].New()
writer.SetFileName('./jenga_g.png')
writer.SetInput(rgbFilter.GetOutput())

# Finally, update!
writer.Update()

# Plot the input and output images.
plt.subplot(1,2,1),plt.title("original"),plt.imshow(itk_image)
plt.subplot(1,2,2),plt.title("grayscale"),plt.imshow(rgbFilter.GetOutput(), cmap="gray")
plt.show()