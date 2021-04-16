import argparse
import SimpleITK as sitk

def build_parser():
    """ A simple command line interface """
    description = "Easy management of dicom files "
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('dicom_dir', help="Dicom directory")
    parser.add_argument('--output', help='Output file')
    return parser

class DicomFile:
    """Class to manage Dicom files. """
    def __init__(self, dicom_folder):
        self.dicom_folder = dicom_folder
        self.read_dicom_series()

    def read_dicom_series(self):
        """ Read a dicom series from a folder

        Returns
        -------
        SimpleITK.Image
            The image as a volume
        """

        reader = sitk.ImageSeriesReader()
        dicom_names = reader.GetGDCMSeriesFileNames(self.dicom_folder)
        reader.SetFileNames(dicom_names)
        self.image = reader.Execute()

    def save(self, output_filename):
        """ Save the image to a file.
        Parameters
        ----------
        output_filename: str
            the name of the output file
        """

        writer = sitk.ImageFileWriter()
        writer.SetFileName(output_filename)
        writer.Execute(self.image)

    def to_numpy(self):
        image_array =  sitk.GetArrayFromImage(self.image)
        return image_array

if __name__ == "__main__":
    ARGS = build_parser().parse_args()
    DicomFile(ARGS.dicom_dir).save(ARGS.output)

