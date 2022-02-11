import numpy as np
import itk
import matplotlib.pyplot as plt

# Input file name
input_filename = './jenga_g.png'

# Set dimension
Dimension = 2

# Read input image
itk_image = itk.imread(input_filename)

# Setting for input image (Grayscale)
InputPixelType = itk.UC
InputImageType = itk.Image[InputPixelType, Dimension]

# Setting for output image (Grayscale)
OutputPixelType = itk.UC
OutputImageType = itk.Image[OutputPixelType, Dimension]

# Loading
reader = itk.ImageFileReader[InputImageType].New()
reader.SetFileName(input_filename)

# Apply a filter: Gaussian
gaussFilter = itk.RecursiveGaussianImageFilter.New(reader)
gaussFilter.SetSigma(10.0)

# Saving
writer = itk.ImageFileWriter[OutputImageType].New()
writer.SetFileName('./img/jenga_gauss.png')
writer.SetInput(gaussFilter.GetOutput())

# Finally, update!
writer.Update()

# Plot the input and output images.
plt.subplot(1,2,1),plt.title("original"),plt.imshow(itk_image, cmap="gray")
plt.subplot(1,2,2),plt.title("grayscale"),plt.imshow(gaussFilter.GetOutput(), cmap="gray")
plt.show()