# 导入moviepy编辑视频的模块
from moviepy.editor import VideoFileClip

# 指定输入视频的路径
input_video_path = "E:/sun/CrossRound.mp4"
# 指定输出视频的路径
output_video_path = "E:/sun/zbl.mp4"

# 读取视频文件
clip = VideoFileClip(input_video_path)

# 计算视频的总时长（以秒为单位）
video_duration = clip.duration

# 定义截取的开始时间和结束时间
start_time = 1 * 60 + 50  # 1分15秒转换为秒
end_time = video_duration - 5  # 总时长减去5秒

# 截取指定时间段的视频片段
subclip = clip.subclip(start_time, end_time)

# 将截取的片段保存为新的视频文件
subclip.write_videofile(output_video_path, codec="libx264", audio_codec="aac")

# 释放资源
clip.close()
subclip.close()