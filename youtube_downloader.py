from pytube import YouTube, Playlist


class YoutubeDownloader:
    """Class representing youtube download tool"""

    def __init__(self):
        pass

    def add_arguments(self, subparsers) -> None:
        """
        Add arguments to ArgParser, in order to build convenient menu

        Parameters :
        ----------
        subparsers : _SubParsersAction[ArgumentParser]
            The subparsers argument of the ArgParser.

        Returns
        -------
        None
        """

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
        """
        Function to download youtube video with highest resolution available

        Parameters :
        ----------
        url : str
            The URL of the YouTube video.
        folder_output : str, optional
            The folder where the downloaded file will be saved. The default is the current folder.

        Returns
        -------
        None
        """

        try:
            video = YouTube(url)
            print("downloading video...")
            video.streams.filter(progressive=True, file_extension="mp4").order_by(
                "resolution"
            )[-1].download(folder_output, video.title)
            print("download completed!")
        except Exception as _e:
            print(f"An error occurred: {str(_e)}")

    def download_video_playlist_highest_resolution(
        self, playlist: str, folder_output=""
    ) -> None:
        """
        Function to download youtube video playlist with highest resolution available

        Parameters :
        ----------
        playlist : str
            The URL of the YouTube playlist.
        folder_output : str, optional
            The folder where the downloaded files will be saved. The default is the current folder.

        Returns
        -------
        None
        """
        try:
            _p = Playlist(playlist)
            print("downloading playlist...")
            for _v in _p.videos:
                _v.streams.filter(progressive=True, file_extension="mp4").order_by(
                    "resolution"
                )[-1].download(folder_output, _v.title)
            print("download completed!")
        except Exception as _e:
            print(f"An error occurred: {str(_e)}")

    def download_only_sound(self, url: str, folder_output="") -> None:
        """
        Function to download youtube video sound with highest available audio bitrate
        and highest audio quality

        Parameters :
        ----------
        url : str
            The URL of the YouTube video.
        folder_output : str, optional
            The folder where the downloaded file will be saved. The default is the current folder.

        Returns
        -------
        None
        """

        try:
            video = YouTube(url)
            print("downloading video sound...")
            video.streams.filter(only_audio=True).order_by("abr")[-1].download(
                folder_output, video.title
            )
            print("download completed!")
        except Exception as _e:
            print(f"An error occurred: {str(_e)}")

    def download_only_sound_playlist(self, playlist: str, folder_output="") -> None:
        """
        Function to download youtube video playlist sound with highest available audio bitrate

        Parameters :
        ----------
        playlist : str
            The URL of the YouTube playlist.
        folder_output : str, optional
            The folder where the downloaded files will be saved. The default is the current folder.

        Returns
        -------
        None
        """

        try:
            _p = Playlist(playlist)
            print("downloading playlist sound...")
            for _v in _p.videos:
                _v.streams.filter(only_audio=True).order_by("abr")[-1].download(
                    folder_output, _v.title
                )
            print("download completed!")
        except Exception as _e:
            print(f"An error occurred: {str(_e)}")
