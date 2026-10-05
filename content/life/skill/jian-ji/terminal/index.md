---
title: Terminal 剪辑
date: 2026-09-19
---

## ffmpeg

### 查看视频信息

```bash
ffmpeg -i test.mp4
```

输出信息为 json

```bash
ffprobe -v quiet -print_format json -show_format -show_streams test.MP4 > info.json
```

json 转 md，写入 script.py
```python
import json

with open("info.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 取视频流、音频流
video_stream = next(s for s in data["streams"] if s["codec_type"] == "video")
audio_stream = next(s for s in data["streams"] if s["codec_type"] == "audio")
fmt = data["format"]

md = f"""# 视频素材信息
|项目|值|
| ---- | ---- |
|文件名|{fmt["filename"]}|
|容器格式|{fmt["format_name"]}|
|总时长|{fmt["duration"]} s|
|总码率|{int(fmt["bit_rate"])/1000:.2f} kbps|

## 视频流
|项目|值|
| ---- | ---- |
|编码|{video_stream["codec_name"]}|
|分辨率|{video_stream["width"]} × {video_stream["height"]}|
|帧率|{video_stream["r_frame_rate"]}|
|像素格式|{video_stream["pix_fmt"]}|
|色域原色|{video_stream.get("color_primaries","N/A")}|
|色彩传递|{video_stream.get("color_trc","N/A")}|
|色彩矩阵|{video_stream.get("color_space","N/A")}|
|视频码率|{int(video_stream["bit_rate"])/1000:.2f} kbps|

## 音频流
|项目|值|
| ---- | ---- |
|编码|{audio_stream["codec_name"]}|
|采样率|{audio_stream["sample_rate"]} Hz|
|声道|{audio_stream["channels"]}|
|音频码率|{int(audio_stream["bit_rate"])/1000:.2f} kbps|
"""

with open("info.md","w",encoding="utf-8") as out:
    out.write(md)

    print("✅ 已生成 info.md")

"
```

运行
```bash
python script.py
```

## 添加标题

生成 标题
```bash
ffmpeg -f lavfi -i color=c=black:s=3840x2160:r=25 -t 5 \
-vf "drawtext=fontfile=$HOME/.fonts/LoveSong.ttf:\
text='Love Song':fontsize=200:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2" \
-c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p title.mp4 -y
```

拼接
```bash
# 2. 拼接标题视频和原视频
echo "file 'title.mp4'" > list.txt
echo "file 'test.MP4'" >> list.txt

ffmpeg -f concat -safe 0 -i list.txt -c copy output_漫歌.mp4
```

标题淡入淡出
```bash
ffmpeg -i test.MP4 \
-vf "\
drawtext=fontfile=$HOME/.fonts/LoveSong.ttf:\
text='Love Song':fontsize=200:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2:\
enable='lte(t,5)':\
alpha='if(lt(t,1),t,if(gt(t,4),5-t,1))'" \
-c:v libx264 -crf 18 -preset medium \
-color_primaries bt2020 -color_trc arib-std-b67 -colorspace bt2020nc \
-c:a pcm_s16be output_LoveSong_fade.mp4
```

图片生成视频
```bash
ffmpeg -loop 1 -i title_base.png -t 5 \
-vf "fade=in:st=0:d=0.8,fade=out:st=4.2:d=0.8" \
-c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -r 25 -y title.mp4
```

## 1.33 圆角

```bash
ffmpeg -i test.MP4 \
-f lavfi -i "color=white:s=1280x960,geq=lum='if(gt(abs(X-640),590)*gt(abs(Y-480),430),0,255)'" \
-filter_complex \
"[0:v]crop=ih*1.3333:ih,scale=1280:960[v1];\
[v1]drawtext=font=Sans:text='Love Song':fontsize=160:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2:enable='lte(t,5)':alpha='if(lt(t,1),t,if(gt(t,4),5-t,1))'[v2];\
[1:v]negate[mask];\
[v2][mask]overlay=0:0" \
-c:v libx264 -crf 18 -preset medium \
-color_primaries bt2020 -color_trc arib-std-b67 -colorspace bt2020nc \
-c:a pcm_s16be output_43_round_title.mp4 -y
```
