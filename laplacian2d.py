import numpy as np
import itk
import matplotlib.pyplot as plt

# Input file name
input_filename = './jenga_g_150.png'

# Set dimension
Dimension = 2

# Read input image
itk_image = itk.imread(input_filename)

# Setting for input image (Grayscale)
InputPixelType = itk.F
InputImageType = itk.Image[InputPixelType, Dimension]

# Setting for output image (Grayscale)
OutputPixelType = itk.F
OutputImageType = itk.Image[OutputPixelType, Dimension]

# Setting for save image (Grayscale)
SavePixelType = itk.UC
SaveImageType = itk.Image[SavePixelType, Dimension]

# Loading
reader = itk.ImageFileReader[InputImageType].New()
reader.SetFileName(input_filename)

# Apply a filter: Laplacian
laplacianFilter = itk.LaplacianImageFilter.New(reader)

# Convert data type
rescaler = itk.IntensityWindowingImageFilter[OutputImageType,OutputImageType].New()
rescaler.SetInput(laplacianFilter.GetOutput())
wincenter = 0.0
winwidth = 100000.0
min = float(wincenter - winwidth/2.0)
max = float(wincenter + winwidth/2.0)
rescaler.SetWindowMinimum(min)
rescaler.SetWindowMaximum(max)
rescaler.SetOutputMinimum(0)
rescaler.SetOutputMaximum(255)

castImageFilter = itk.CastImageFilter[OutputImageType, SaveImageType].New()
castImageFilter.SetInput(rescaler.GetOutput())

# Saving
writer = itk.ImageFileWriter[SaveImageType].New()
writer.SetFileName('./img/jenga_laplacian.png')
writer.SetInput(castImageFilter.GetOutput())

# Finally, update!
writer.Update()

# Plot the input and output images.
plt.subplot(1,2,1),plt.title("original"),plt.imshow(itk_image, cmap="gray")
plt.subplot(1,2,2),plt.title("output"),plt.imshow(castImageFilter.GetOutput(), cmap="gray")
plt.show()