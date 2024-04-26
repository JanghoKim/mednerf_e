@echo off
FOR /L %%G IN (1,1,30) DO (
    python render_xray_G_Z.py configs/knee.yaml --xray_img_path ./data/mednerf_drr_dataset/knee_xrays --save_dir ./renderings/knee --model model_best_original.pt --save_every 10000 --psnr_stop 1000 

)