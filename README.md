# 安装环境

```sh
#python>=3.6
pip install -r requirements.txt
```

# 运行

## 1. 对YouTube视频评论进行爬虫

```sh
#若要爬取多个视频的评论，可在youtube_video_ids.txt中添加视频id，每一行一个视频id
python fixed_full_comment_scrap_codes.py
```

## 2. 对评论进行分析

### 2.1 使用LDA模型对评论进行Topic提取

```sh
python campus_PC_topic_modelling_codes.py
#也可以通过topic_num参数指定分析的topic数量，默认为2
python campus_PC_topic_modelling_codes.py --topic_num 2
```

### 2.2 使用flair模型对评论进行情感分析

```sh
python sentiment_analysis_with_flair_codes.py
```