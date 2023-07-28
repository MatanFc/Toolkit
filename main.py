import argparse
from youtube_downloader import YoutubeDownloader
from simple_pdf import simplePDF


def main():
    youtube_downloader = YoutubeDownloader()
    simple_pdf = simplePDF()

    parser = argparse.ArgumentParser(description="Options:")

    subparsers = parser.add_subparsers(dest="command", help="Commands")
    youtube_downloader.add_arguments(subparsers)
    simple_pdf.add_arguments(subparsers)

    args = parser.parse_args()

    if args.command == "yt":
        if args.playlist:
            if args.type == "video":
                youtube_downloader.download_video_playlist_highest_resolution(
                    args.url, folder_output=args.folder_output
                )
            elif args.type == "sound":
                youtube_downloader.download_only_sound_playlist(
                    args.url, folder_output=args.folder_output
                )
        else:
            if args.type == "video":
                youtube_downloader.download_highest_video_with_sound(
                    args.url, folder_output=args.folder_output
                )
            elif args.type == "sound":
                youtube_downloader.download_only_sound(
                    args.url, folder_output=args.folder_output
                )
    elif args.command == "pdf":
        if args.subcommand == "rotate":
            simple_pdf.rotate_clockwise(
                args.pdf_path,
                out_folder=args.out_folder,
                name=args.name,
                degrees=args.degrees,
            )
        elif args.subcommand == "merge":
            simple_pdf.merge_from_folder(args.folder_path, out_folder=args.out_folder)


if __name__ == "__main__":
    main()
