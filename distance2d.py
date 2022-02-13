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
InputPixelType = itk.F
InputImageType = itk.Image[InputPixelType, Dimension]

# Setting for output image (Grayscale)
OutputPixelType = itk.F
OutputImageType = itk.Image[OutputPixelType, Dimension]

# Loading
reader = itk.ImageFileReader[InputImageType].New()
reader.SetFileName(input_filename)

# Apply a filter: Thresholding
thresholdFilter = itk.BinaryThresholdImageFilter[InputImageType,InputImageType].New()
thresholdFilter.SetInput(reader.GetOutput())
thresholdFilter.SetUpperThreshold(200)
thresholdFilter.SetOutsideValue(1)
thresholdFilter.SetInsideValue(0)

connectedFilter = itk.SignedDanielssonDistanceMapImageFilter[InputImageType,InputImageType].New()
connectedFilter.SetInput(thresholdFilter.GetOutput())
connectedFilter.InsideIsPositiveOn()
connectedFilter.Update()

# Plot the input and output images.
plt.figure(figsize=(12, 4), dpi=50)
plt.subplot(1,3,1),plt.title("original"),plt.imshow(itk_image, cmap="gray")
plt.subplot(1,3,2),plt.title("threshold"),plt.imshow(thresholdFilter.GetOutput())
plt.subplot(1,3,3),plt.title("output"),plt.imshow(connectedFilter.GetOutput())
plt.savefig("./img/distance2d.png")