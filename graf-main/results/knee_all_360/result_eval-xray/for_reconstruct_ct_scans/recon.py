import numpy as np
import astra
import matplotlib.pyplot as plt
import imageio  # to load image files

# Load your X-ray images
def load_xray_images(directory, num_images):
    projections = []
    for i in range(num_images):
        image_path = f"{directory}/image_{i+1}.png"
        image = imageio.imread(image_path)
        if image.ndim == 3:  # Convert RGB to grayscale by averaging channels if needed
            image = image.mean(axis=2)
        projections.append(image.astype(float))
    projections = np.stack(projections, axis=0)
    # Transpose the stack to fit ASTRA's expected input shape: (num_angles, detector_rows, detector_cols)
    projections = np.transpose(projections, (1, 0, 2))
    return projections

# Set up geometry with real parameters
def setup_real_geometry(num_images, SOD, SDD, detector_size):
    angles = np.linspace(0, 2 * np.pi, num_images, endpoint=False)
    detector_rows = detector_size[0]  # Update this with your image height
    detector_cols = detector_size[1]  # Update this with your image width
    proj_geom = astra.create_proj_geom('cone', 1.0, 1.0, detector_rows, detector_cols, angles, SOD, SDD)
    vol_geom = astra.create_vol_geom(detector_cols, detector_cols, detector_cols)

    # proj_geom = astra.create_proj_geom('parallel3d', 1.0, detector_cols, angles)
    # vol_geom = astra.create_vol_geom(detector_cols, detector_cols, detector_rows)

    return vol_geom, proj_geom

# Perform reconstruction
def reconstruct(proj_id, vol_geom, proj_geom):
    cfg = astra.astra_dict('FDK_CUDA')
    cfg['ReconstructionDataId'] = astra.data3d.create('-vol', vol_geom)
    cfg['ProjectionDataId'] = proj_id
    alg_id = astra.algorithm.create(cfg)
    astra.algorithm.run(alg_id, 100)
    rec = astra.data3d.get(cfg['ReconstructionDataId'])
    astra.algorithm.delete(alg_id)
    astra.data3d.delete(proj_id)
    astra.data3d.delete(cfg['ReconstructionDataId'])
    return rec

# Main execution function
def main():
    directory = 'dataset'  # specify your directory path
    num_images = 360  # total number of X-ray images
    SOD = 350   # source-to-object distance in mm
    SDD = 455 # source-to-detector distance in mm, assume larger than SOD
    detector_size = (128, 128)  # Update this based on your image dimensions
    
    # Load real X-ray images
    projections = load_xray_images(directory, num_images)

    # Setup geometry
    vol_geom, proj_geom = setup_real_geometry(num_images, SOD, SDD, detector_size)
    
    # Create projection data in ASTRA format
    proj_id = astra.data3d.create('-proj3d', proj_geom, projections)
    
    # Perform reconstruction
    rec = reconstruct(proj_id, vol_geom, proj_geom)

    # Visualization of one slice
    # Assuming 'rec' is your 3D reconstructed volume
    for i in range(128):  # Loop from slice 0 to 128 inclusive
        slice_data = rec[i, :, :]  # Extract the ith slice
        plt.imsave(f'slice_{i:03d}.png', slice_data, cmap='gray')  # Save each slice as a PNG file
    

if __name__ == '__main__':
    main()