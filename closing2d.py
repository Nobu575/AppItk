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
InputPixelType = itk.UC
InputImageType = itk.Image[InputPixelType, Dimension]

# Loading
reader = itk.ImageFileReader[InputImageType].New()
reader.SetFileName(input_filename)

# Apply a filter: Thresholding
thresholdFilter = itk.BinaryThresholdImageFilter[InputImageType,InputImageType].New()
thresholdFilter.SetInput(reader.GetOutput())
thresholdFilter.SetUpperThreshold(200)
thresholdFilter.SetOutsideValue(1)
thresholdFilter.SetInsideValue(0)

StructuringElementType = itk.FlatStructuringElement[Dimension]
structuringElement = StructuringElementType.Ball(3)

# Apply Closing (dilation and erosion)
dilateFilter = itk.BinaryDilateImageFilter[InputImageType,InputImageType,StructuringElementType].New()
dilateFilter.SetInput(thresholdFilter.GetOutput())
dilateFilter.SetKernel(structuringElement)
dilateFilter.SetForegroundValue(1)

erodeFilter = itk.BinaryErodeImageFilter[InputImageType,InputImageType,StructuringElementType].New()
erodeFilter.SetInput(dilateFilter.GetOutput())
erodeFilter.SetKernel(structuringElement)
erodeFilter.SetForegroundValue(1)

erodeFilter.Update()

# Plot the input and output images.
plt.figure(figsize=(12, 4), dpi=50)
plt.subplot(1,3,1),plt.title("original"),plt.imshow(itk_image, cmap="gray")
plt.subplot(1,3,2),plt.title("threshold"),plt.imshow(thresholdFilter.GetOutput())
plt.subplot(1,3,3),plt.title("output"),plt.imshow(erodeFilter.GetOutput())
plt.savefig("./img/jenga_closing2d.png")