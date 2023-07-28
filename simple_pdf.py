"""
A simple script to merge and rotate PDF files.
"""

import os
from pypdf import PdfMerger, PdfWriter, PdfReader


class SimplePdf:
    """
    Class representing a pdf tool to manipulate files
    """

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

        pdf_parser = subparsers.add_parser(
            "pdf", help="PDF toolkit to easily manipulate files"
        )
        pdf_subparsers = pdf_parser.add_subparsers(dest="command", help="PDF commands")

        # Command for rotating PDF
        rotate_parser = pdf_subparsers.add_parser(
            "rotate", help="Rotate a PDF clockwise."
        )
        rotate_parser.add_argument(
            "pdf_path", type=str, help="Path to the PDF file to rotate."
        )
        rotate_parser.add_argument(
            "--out_folder",
            type=str,
            default="",
            help="Specify the folder where the rotated PDF will be saved.",
        )
        rotate_parser.add_argument(
            "--name",
            type=str,
            default="out.pdf",
            help="Specify the output file name for the rotated PDF.",
        )
        rotate_parser.add_argument(
            "--degrees",
            type=int,
            default=90,
            choices=[90, 180, 270],
            help="Specify the rotation angle: 90, 180, or 270 degrees.",
        )

        # Command for merging PDFs
        merge_parser = pdf_subparsers.add_parser(
            "merge", help="Merge PDFs from a folder."
        )
        merge_parser.add_argument(
            "folder_path",
            type=str,
            help="Path to the folder containing the PDFs to merge.",
        )
        merge_parser.add_argument(
            "--out_folder",
            type=str,
            default="",
            help="Specify the folder where the merged PDF will be saved.",
        )

    def rotate_clockwise(
        self, pdf_path: str, out_folder="", name="out.pdf", degrees=90
    ) -> None:
        """
        Function to rotate pdf files clockwise

        Parameters :
        ----------
        pdf_path : str
            Path to the PDF file to
        out_folder : str
            Specify the folder where the rotated PDF will be saved.
        name : str
            Specify the output file name for the rotated PDF.
        degrees : int
            Specify the rotation angle: 90, 180, or 270 degrees.

        Returns
        -------
        None
        """

        reader = PdfReader(pdf_path)
        writer = PdfWriter()

        for _p in reader.pages:
            writer.add_page(_p)
            writer.pages[len(writer.pages) - 1].rotate(degrees)

        with open(os.path.join(out_folder, name), "wb") as _fp:
            writer.write(_fp)

    def merge_from_folder(self, folder_path: str, out_folder="") -> None:
        """
        Function to merge multiple pdf files from given folder
        
        Parameters :
        ----------
        folder_path : str
            Path to the folder containing the PDFs to merge.
        out_folder : str
            Specify the folder where the merged PDF will be saved.

        Returns
        -------
        None
        """

        files = os.listdir(folder_path)
        files.sort()
        full_path_pdfs = [
            os.path.join(folder_path, i) for i in files if i.endswith(".pdf")
        ]
        merger = PdfMerger()

        for pdf in full_path_pdfs:
            merger.append(pdf)

        merger.write(os.path.join(out_folder, "result.pdf"))
        merger.close()
