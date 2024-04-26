import numpy as np

# Open the text file
with open('result_z_mult.txt', 'r') as file:
    lines = file.readlines()

# Initialize lists to store PSNR and SSIM values
psnr_values = []
ssim_values = []


for line in lines:
    values = line.split()
    if 'MEAN_PSNR:' in values and 'MEAN_SSIM:' in values:
        psnr_index = values.index('MEAN_PSNR:')
        ssim_index = values.index('MEAN_SSIM:')
        psnr_values.append(float(values[psnr_index + 1]))
        ssim_values.append(float(values[ssim_index + 1]))

# Calculate mean
mean_psnr = sum(psnr_values) / len(psnr_values)
mean_ssim = sum(ssim_values) / len(ssim_values)
std_dev_psnr = np.std(psnr_values, ddof=1)  # Using ddof=1 to use the sample standard deviation formula
std_dev_ssim = np.std(ssim_values, ddof=1)


print("Mean PSNR:", mean_psnr)
print("PSNR std:", std_dev_psnr)
print("Mean SSIM:", mean_ssim)
print("SSIM std:", std_dev_ssim)

