from akagi.datasource import Datasource
from akagi.data_file_bundles import S3DataFileBundle
from akagi.iterator import FileFormat


class S3Datasource(Datasource):
    '''S3Datasource replesents a set of files on Amazon S3 bucket.
    '''

    @classmethod
    def for_prefix(cls, bucket_name, prefix, file_format=FileFormat.BINARY):
        bundle = S3DataFileBundle(
                bucket_name,
                prefix,
                file_format
                )

        return S3Datasource(bundle)

    @classmethod
    def for_key(cls, bucket_name, key, file_format=FileFormat.BINARY):
        return S3Datasource.for_prefix(bucket_name, key, file_format)

    def __init__(self, bundle):
        self.bundle = bundle

    def __iter__(self):
        return iter(self.bundle)