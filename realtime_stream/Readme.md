### Server setup

    sudo apt-get update
    sudo apt-get install supervisor
    
    sudo apt-get install ffmpeg

    sudo nano /etc/supervisor/conf.d/ffmpeg.conf
    
copy the file content of supervisor_conf to here then save it and close

    sudo mkdir -p /var/log/supervisor

    sudo supervisorctl reread
    sudo supervisorctl update
    sudo supervisorctl restart ffmpeg

Check status

    sudo supervisorctl status ffmpeg

### NGinx

    sudo apt-get install nginx

    sudo nano /etc/nginx/sites-available/default

copy the file content of nginx_for_stream_video to here then save it and close

    sudo systemctl restart nginx
