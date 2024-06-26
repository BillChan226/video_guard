#!/bin/bash

# Define the directories and files
ADS_GAME_VIDEOS="ads_game_videos"
ADS_GAME_VIDEOS_2="ads_game_videos_2"
VIDEO_DOWNLOAD="video_download"
VIDEO_DOWNLOAD_2="video_download_2"
VIDEO_DOWNLOAD_3="video_download_3"
VIDEO_DOWNLOAD_4="video_download_4"
VIDEO_DOWNLOAD_5="video_download_5"

# Unzip all the necessary files
echo "Unzipping files..."
unzip ads_game_videos.zip
unzip ads_game_videos_2.zip
unzip video_download.zip
unzip video_download_2.zip
unzip video_download_3.zip
unzip video_download_4.zip
unzip video_download_5.zip

# Merge ads_game_videos and ads_game_videos_2 into one folder
echo "Merging ads_game_videos folders..."
mkdir -p merged_ads_game_videos
cp -r $ADS_GAME_VIDEOS/* merged_ads_game_videos/
cp -r $ADS_GAME_VIDEOS_2/* merged_ads_game_videos/

# Merge video_download folders into one folder
echo "Merging video_download folders..."
mkdir -p merged_video_download
cp -r $VIDEO_DOWNLOAD/* merged_video_download/
cp -r $VIDEO_DOWNLOAD_2/* merged_video_download/
cp -r $VIDEO_DOWNLOAD_3/* merged_video_download/
cp -r $VIDEO_DOWNLOAD_4/* merged_video_download/
cp -r $VIDEO_DOWNLOAD_5/* merged_video_download/

# Inform the user that the script has completed
echo "All files have been processed and are ready for use."
