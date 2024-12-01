import torch
print(torch.__version__)

print(torch.cuda.is_available())  # Should return True if CUDA is available
print(torch.version.cuda)  # This will return the CUDA version PyTorch is using

if torch.cuda.is_available():
    print("GPU is available")
else:
    print("GPU is not available")

