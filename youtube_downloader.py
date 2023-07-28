from pytube import YouTube, Playlist


class YoutubeDownloader:
    def __init__(self):
        pass

    def add_arguments(self, subparsers) -> None:
        parser = subparsers.add_parser(
            "yt", help="Download YouTube videos or playlists with various options."
        )

        parser.add_argument(
            "url",
            type=str,
            help="The URL of the YouTube video or playlist.",
        )
        parser.add_argument(
            "--playlist",
            action="store_true",
            help="Specify if the provided URL is a playlist.",
            default=False,
        )
        parser.add_argument(
            "--type",
            action="store",
            help="Specify if the provided URL is for a video or a sound.",
            type=str,
            choices=["video", "sound"],
            default="video",
        )
        parser.add_argument(
            "--folder_output",
            type=str,
            default="",
            help="Specify the folder where the downloaded files will be saved.",
        )

    def download_highest_video_with_sound(self, url: str, folder_output="") -> None:
        try:
            video = YouTube(url)
            print("downloading video...")
            video.streams.filter(progressive=True, file_extension="mp4").order_by(
                "resolution"
            )[-1].download(folder_output, video.title)
            print("download completed!")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def download_video_playlist_highest_resolution(
        self, playlist: str, folder_output=""
    ) -> None:
        try:
            p = Playlist(playlist)
            print("downloading playlist...")
            for v in p.videos:
                v.streams.filter(progressive=True, file_extension="mp4").order_by(
                    "resolution"
                )[-1].download(folder_output, v.title)
            print("download completed!")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def download_only_sound(self, url: str, folder_output="") -> None:
        try:
            video = YouTube(url)
            print("downloading video sound...")
            video.streams.filter(only_audio=True).order_by("abr")[-1].download(
                folder_output, video.title
            )
            print("download completed!")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def download_only_sound_playlist(self, playlist: str, folder_output="") -> None:
        try:
            p = Playlist(playlist)
            print("downloading playlist sound...")
            for v in p.videos:
                v.streams.filter(only_audio=True).order_by("abr")[-1].download(
                    folder_output, v.title
                )
            print("download completed!")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
