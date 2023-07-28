# CLI YouTube Downloader and PDF Toolkit

This is a Python command-line interface (CLI) program that allows you to download YouTube videos and playlists with various options. Additionally, it provides a PDF toolkit to easily manipulate PDF files, including rotating PDFs and merging PDFs from a folder.

## Requirements

To run this CLI program, you need to have the required Python packages installed. You can install them using the `requirements.txt` file provided in the project.

### Install Required Packages

To install the required packages, run the following command:

```bash
pip install -r requirements.txt
```


## Usage

1. Download YouTube Videos or Playlists:
```css
python main.py yt --type video <URL> --folder_output <output_folder>
```

- Replace `<URL>` with the YouTube video URL or playlist URL.
- Replace `<output_folder>` with the folder where the downloaded files will be saved.
- Use `--type sound` to download only the audio of the video.

2. Rotate a PDF clockwise:

```css
python main.py pdf rotate <pdf_path> --out_folder <output_folder> --name <output_name> --degrees <rotation_degrees>
```

- Replace `<pdf_path>` with the path to the PDF file to rotate.
- Use `--out_folder` to specify the folder where the rotated PDF will be saved. (Optional)
- Use `--name` to specify the output file name for the rotated PDF. (Optional, default: "out.pdf")
- Use `--degrees` to specify the rotation angle: 90, 180, or 270 degrees. (Optional, default: 90)

3. Merge PDFs from a folder:

```css
python main.py pdf merge <folder_path> --out_folder <output_folder>
```

- Replace <folder_path> with the path to the folder containing the PDFs to merge.
- Use --out_folder to specify the folder where the merged PDF will be saved. (Optional)

## Examples

1. Download a YouTube video with the highest resolution:
```css
python main.py yt --type video https://www.youtube.com/watch?v=<video_id> --folder_output /path/to/output
```

2. Download a YouTube playlist as audio files:
```css
python main.py yt --playlist --type sound https://www.youtube.com/playlist?list=<playlist_id> --folder_output /path/to/output
```

3. Rotate a PDF clockwise by 180 degrees:
```css
python main.py pdf rotate /path/to/input.pdf --out_folder /path/to/output --name rotated.pdf --degrees 180
```

4. Merge PDFs from a folder:
```css
python main.py pdf merge /path/to/pdf_folder --out_folder /path/to/output
```