import shutil
import subprocess
import uuid

# need ffmpeg installed (apt-get install ffmpeg)
def convert_movie(file, fileout='myvideo.mp4'):
    """Convert file to mp4. need ffmpeg installed (apt-get install ffmpeg)
    parameters:
    file: path to movie file
    fileout: filename of outfile (default is myvideo.mp4)"""
    unique_filename = str(uuid.uuid4())
    src_dir=file
    dst_dir='/tmp/{}.'.format(unique_filename)+file.split('.')[-1]
    filename = shutil.copy(src_dir,dst_dir)
    #filename2 = filename.replace(file.split('.')[-1],'mp4')
    #     with open(filename2, 'w') as fp:
    #         pass
    query = '''ffmpeg -i {} -vcodec libx264 -vf "fps=25" -vsync cfr -b:v 2300k -acodec aac -b:a 128k {} -y'''.format(filename, fileout.replace(' ','_'))
    subprocess.run(query, shell=True)
